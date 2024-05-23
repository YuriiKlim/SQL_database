from sqlalchemy import create_engine, MetaData, func, and_, or_, select
from sqlalchemy.orm import sessionmaker
import json
from datetime import date


with open('config.json', 'r') as f:
    data = json.load(f)
    db_user = data['user']  # postgres
    db_password = data['password']

db_url = f'postgresql+psycopg2://{db_user}:{db_password}@localhost:5432/hospital'
engine = create_engine(db_url)

metadata = MetaData()
metadata.reflect(bind=engine)

Session = sessionmaker(bind=engine)
session = Session()


docs = metadata.tables['doctors']
specs = metadata.tables['specializations']
docsspecs = metadata.tables['doctorsspecializations']
vacations = metadata.tables['vacations']
wards = metadata.tables['wards']
departments = metadata.tables['departments']
donations = metadata.tables['donations']
sponsors = metadata.tables['sponsors']


def report_doctor_specializations():
    result = session.query(docs.c.name.label('doctorname'),
                           docs.c.surname,
                           specs.c.name.label('specialization_name')) \
             .join(docsspecs, docsspecs.c.doctor_id == docs.c.id) \
             .join(specs, docsspecs.c.specialization_id == specs.c.id).all()

    if result:
        for row in result:
            print(f"{row.doctorname} {row.surname} with specialization {row.specialization_name}")


def report_doctors_not_on_vacation():
    today = date.today()

    subquery = session.query(vacations.c.doctor_id).filter(
        and_(
            vacations.c.start_date <= today,
            vacations.c.end_date >= today
        )
    ).subquery()
    subquery = select(subquery)

    result = session.query(docs.c.surname,
                           (docs.c.salary + docs.c.premium).label('total_salary')) \
        .filter(~docs.c.id.in_(subquery)).all()

    if result:
        for row in result:
            print(f"{row.surname}: {row.total_salary}")


def report_wards_department(department_id):
    result = session.query(wards.c.name) \
             .filter(wards.c.department_id == department_id).all()

    if result:
        for row in result:
            print(f"{row.name}")


def report_donations_of_month(year, month):
    result = session.query(departments.c.name.label('department_name'),
                           sponsors.c.name.label('sponsor_name'),
                           donations.c.amount,
                           donations.c.date) \
             .join(departments, donations.c.department_id == departments.c.id) \
             .join(sponsors, donations.c.sponsor_id == sponsors.c.id) \
             .filter(func.extract('year', donations.c.date) == year,
                     func.extract('month', donations.c.date) == month).all()

    if result:
        for row in result:
            print(f"{row.department_name}, {row.sponsor_name}, {row.amount}, {row.date}")


def report_departments_by_sponsor(sponsor_name):
    result = session.query(departments.c.name.label('department_name')) \
             .join(donations, donations.c.department_id == departments.c.id) \
             .join(sponsors, donations.c.sponsor_id == sponsors.c.id) \
             .filter(sponsors.c.name == sponsor_name).distinct().all()

    if result:
        for row in result:
            print(f"{row.department_name}")

while True:
    print("1. Вивести повні імена лікарів та їх спеціалізації")
    print("2. Вивести прізвища та зарплати лікарів, які не перебувають у відпустці")
    print("3. Вивести назви палат, які знаходяться у певному відділенні;")
    print("4. Вивести усі пожертвування за вказаний місяць у вигляді: відділення, спонсор, сума пожертвування, дата пожертвування;")
    print("5. Вивести назви відділень без повторень, які спонсоруються певною компанією.")
    print("0. Вийти")

    choice = input("Оберіть опцію: ")

    if choice == "1":
        report_doctor_specializations()
    elif choice == "2":
        report_doctors_not_on_vacation()
    elif choice == "3":
        department_id = int(input("Введіть ID відділення: "))
        report_wards_department(department_id)
    elif choice == "4":
        year = int(input("Введіть рік: "))
        month = int(input("Введіть місяць: "))
        report_donations_of_month(year, month)
    elif choice == "5":
        sponsor_name = input("Введіть назву компанії: ")
        report_departments_by_sponsor(sponsor_name)
    elif choice == "0":
        break
    else:
        print("Невірний вибір. Будь ласка, оберіть знову.")

# Закриваємо сесію
session.close()
