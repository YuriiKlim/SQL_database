from sqlalchemy import create_engine, MetaData, func, and_, or_, insert
from sqlalchemy.orm import sessionmaker
import json


with open('config.json', 'r') as f:
    data = json.load(f)
    db_user = data['user']  # postgres
    db_password = data['password']

db_url = f'postgresql+psycopg2://{db_user}:{db_password}@localhost:5432/academy'
engine = create_engine(db_url)

metadata = MetaData()
metadata.reflect(bind=engine)

Session = sessionmaker(bind=engine)
session = Session()


curators = metadata.tables['curators']
departments = metadata.tables['departments']
faculties = metadata.tables['faculties']
groups = metadata.tables['groups']
groupslectures = metadata.tables['groupslectures']
lectures = metadata.tables['lectures']
subjects = metadata.tables['subjects']
teachers = metadata.tables['teachers']


def insert_row(table_name):
    table = metadata.tables[table_name]
    values = {}
    for column in table.columns:
        if column.name != 'id':  # Assuming 'id' is an auto-increment column
            value = input(f"Введіть значення для {column.name} ({column.type}): ")
            values[column.name] = value
    insert_stmt = table.insert().values(values)
    session.execute(insert_stmt)
    session.commit()


def update_row(table_name):
    table = metadata.tables[table_name]
    row_id = input("Введіть ID рядка для оновлення: ")
    values = {}
    for column in table.columns:
        if column.name != 'id':
            value = input(f"Введіть нове значення для {column.name} ({column.type}) або залиште порожнім, щоб не змінювати: ")
            if value:
                values[column.name] = value
    update_stmt = table.update().where(table.c.id == row_id).values(values)
    session.execute(update_stmt)
    session.commit()



def delete_row(table_name):
    table = metadata.tables[table_name]
    row_id = input("Введіть ID рядка для видалення: ")
    delete_stmt = table.delete().where(table.c.id == row_id)
    session.execute(delete_stmt)
    session.commit()


def report_all_groups():
    result = session.query(groups).all()
    for row in result:
        print(row)


def report_all_teachers():
    result = session.query(teachers).all()
    for row in result:
        print(row)


def report_all_departments():
    result = session.query(departments.c.name).all()
    for row in result:
        print(row.name)


def report_teachers_in_group(group_name):
    result = session.query(teachers.c.name, teachers.c.surname) \
                    .join(lectures, teachers.c.id == lectures.c.teacher_id) \
                    .join(groupslectures, lectures.c.id == groupslectures.c.lecture_id) \
                    .join(groups, groupslectures.c.group_id == groups.c.id) \
                    .filter(groups.c.name == group_name).all()
    for row in result:
        print(f"{row.name} {row.surname}")


def report_departments_and_groups():
    result = session.query(departments.c.name.label('department_name'), groups.c.name.label('group_name')) \
                    .join(groups, departments.c.id == groups.c.department_id).all()
    for row in result:
        print(f"{row.department_name} - {row.group_name}")


def report_department_with_max_groups():
    result = session.query(departments.c.name) \
                    .join(groups, departments.c.id == groups.c.department_id) \
                    .group_by(departments.c.name) \
                    .order_by(func.count(groups.c.id).desc()).first()
    print(result.name)


def report_department_with_min_groups():
    result = session.query(departments.c.name) \
                    .join(groups, departments.c.id == groups.c.department_id) \
                    .group_by(departments.c.name) \
                    .order_by(func.count(groups.c.id).asc()).first()
    print(result.name)


def report_subjects_by_teacher(teacher_name):
    result = session.query(subjects.c.name) \
                    .join(lectures, subjects.c.id == lectures.c.subject_id) \
                    .join(teachers, lectures.c.teacher_id == teachers.c.id) \
                    .filter(teachers.c.name == teacher_name).all()
    for row in result:
        print(row.name)


def report_departments_by_subject(subject_name):
    result = session.query(departments.c.name) \
                    .join(groups, departments.c.id == groups.c.department_id) \
                    .join(groupslectures, groups.c.id == groupslectures.c.group_id) \
                    .join(lectures, groupslectures.c.lecture_id == lectures.c.id) \
                    .join(subjects, lectures.c.subject_id == subjects.c.id) \
                    .filter(subjects.c.name == subject_name).all()
    for row in result:
        print(row.name)


def report_groups_by_faculty(faculty_name):
    result = session.query(groups.c.name) \
                    .join(departments, groups.c.department_id == departments.c.id) \
                    .join(faculties, departments.c.faculty_id == faculties.c.id) \
                    .filter(faculties.c.name == faculty_name).all()
    for row in result:
        print(row.name)


def report_subjects_and_teachers_with_most_lectures():
    result = session.query(subjects.c.name.label('subject_name'), teachers.c.name.label('teacher_name'), teachers.c.surname.label('teacher_surname')) \
                    .join(lectures, subjects.c.id == lectures.c.subject_id) \
                    .join(teachers, lectures.c.teacher_id == teachers.c.id) \
                    .group_by(subjects.c.name, teachers.c.name, teachers.c.surname) \
                    .order_by(func.count(lectures.c.id).desc()).all()
    for row in result:
        print(f"{row.subject_name} - {row.teacher_name} {row.teacher_surname}")


def report_subject_with_least_lectures():
    result = session.query(subjects.c.name) \
                    .join(lectures, subjects.c.id == lectures.c.subject_id) \
                    .group_by(subjects.c.name) \
                    .order_by(func.count(lectures.c.id).asc()).first()
    print(result.name)


def report_subject_with_most_lectures():
    result = session.query(subjects.c.name) \
                    .join(lectures, subjects.c.id == lectures.c.subject_id) \
                    .group_by(subjects.c.name) \
                    .order_by(func.count(lectures.c.id).desc()).first()
    print(result.name)


def authenticate(username, password):
    user = session.query(metadata.tables['users']).filter_by(username=username, password=password).first()
    if user:
        return user.access_level
    else:
        return None


def check_access(access_level, required_level):
    levels = {
        'read': 1,
        'write': 2,
        'full': 3
    }
    return levels.get(access_level, 0) >= levels.get(required_level, 0)


def main():
    username = input("Введіть ім'я користувача: ")
    password = input("Введіть пароль: ")
    access_level = authenticate(username, password)

    if not access_level:
        print("Невірний логін або пароль.")
        return

    while True:
        if check_access(access_level, 'write'):
            print("1. Вставити рядок")
        if check_access(access_level, 'write'):
            print("2. Оновити рядок")
        if check_access(access_level, 'write'):
            print("3. Видалити рядок")
        print("4. Звіт: Всі навчальні групи")
        print("5. Звіт: Всі викладачі")
        print("6. Звіт: Всі кафедри")
        print("7. Звіт: Викладачі у конкретній групі")
        print("8. Звіт: Кафедри та групи")
        print("9. Звіт: Кафедра з найбільшою кількістю груп")
        print("10. Звіт: Кафедра з найменшою кількістю груп")
        print("11. Звіт: Предмети, які викладає конкретний викладач")
        print("12. Звіт: Кафедри, де викладається конкретна дисципліна")
        print("13. Звіт: Групи конкретного факультету")
        print("14. Звіт: Предмети та викладачі з найбільшою кількістю лекцій")
        print("15. Звіт: Предмет з найменшою кількістю лекцій")
        print("16. Звіт: Предмет з найбільшою кількістю лекцій")
        print("0. Вийти")

        choice = input("Оберіть опцію: ")

        if choice == "1":
            if check_access(access_level, 'write'):
                table_name = input("Введіть назву таблиці: ")
                insert_row(table_name)
            else:
                print("Недостатньо прав доступу.")
        elif choice == "2":
            if check_access(access_level, 'write'):
                table_name = input("Введіть назву таблиці: ")
                update_row(table_name)
            else:
                print("Недостатньо прав доступу.")
        elif choice == "3":
            if check_access(access_level, 'write'):
                table_name = input("Введіть назву таблиці: ")
                delete_row(table_name)
            else:
                print("Недостатньо прав доступу.")
        elif choice == "4":
            if check_access(access_level, 'read'):
                report_all_groups()
            else:
                print("Недостатньо прав доступу.")
        elif choice == "5":
            if check_access(access_level, 'read'):
                report_all_teachers()
            else:
                print("Недостатньо прав доступу.")
        elif choice == "6":
            if check_access(access_level, 'read'):
                report_all_departments()
            else:
                print("Недостатньо прав доступу.")
        elif choice == "7":
            if check_access(access_level, 'read'):
                group_name = input("Введіть назву групи: ")
                report_teachers_in_group(group_name)
            else:
                print("Недостатньо прав доступу.")
        elif choice == "8":
            if check_access(access_level, 'read'):
                report_departments_and_groups()
            else:
                print("Недостатньо прав доступу.")
        elif choice == "9":
            if check_access(access_level, 'read'):
                report_department_with_max_groups()
            else:
                print("Недостатньо прав доступу.")
        elif choice == "10":
            if check_access(access_level, 'read'):
                report_department_with_min_groups()
            else:
                print("Недостатньо прав доступу.")
        elif choice == "11":
            if check_access(access_level, 'read'):
                teacher_name = input("Введіть ім'я викладача: ")
                report_subjects_by_teacher(teacher_name)
            else:
                print("Недостатньо прав доступу.")
        elif choice == "12":
            if check_access(access_level, 'read'):
                subject_name = input("Введіть назву дисципліни: ")
                report_departments_by_subject(subject_name)
            else:
                print("Недостатньо прав доступу.")
        elif choice == "13":
            if check_access(access_level, 'read'):
                faculty_name = input("Введіть назву факультету: ")
                report_groups_by_faculty(faculty_name)
            else:
                print("Недостатньо прав доступу.")
        elif choice == "14":
            if check_access(access_level, 'read'):
                report_subjects_and_teachers_with_most_lectures()
            else:
                print("Недостатньо прав доступу.")
        elif choice == "15":
            if check_access(access_level, 'read'):
                report_subject_with_least_lectures()
            else:
                print("Недостатньо прав доступу.")
        elif choice == "16":
            if check_access(access_level, 'read'):
                report_subject_with_most_lectures()
            else:
                print("Недостатньо прав доступу.")
        elif choice == "0":
            break
        else:
            print("Невірний вибір. Будь ласка, оберіть знову.")


session.close()

if __name__ == "__main__":
    main()

