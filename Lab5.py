from sqlalchemy import create_engine, Column, Integer, String, Sequence, Date
from sqlalchemy import or_
from sqlalchemy.orm import sessionmaker
from sqlalchemy.orm import declarative_base
from sqlalchemy.sql import text
import json

with open('config.json', 'r') as f:
    data = json.load(f)
    db_user = data['user']
    db_password = data['password']

db_url = f'postgresql+psycopg2://{db_user}:{db_password}@localhost:5432/People'
engine = create_engine(db_url)

Base = declarative_base()


class Person(Base):
    __tablename__ = 'person'
    id = Column(Integer, Sequence('person_id_seq'), primary_key=True)
    firs_name = Column(String(256))
    surrname = Column(String(256))
    city = Column(String(256))
    country = Column(String(256))
    birthd_date = Column(Date)


# створення таблиці
Base.metadata.create_all(bind=engine)

# створення сесії
Session = sessionmaker(bind=engine)
session = Session()

valid_tables = ["person"]

while True:
    print("Введіть команду")
    print("1. виконати запит")
    print("2. вивести всіх людей")
    print("3. вивести всіх людей з певного міста")
    print("4. вивести всіх людей з певного міста або країни")
    print("5. вивести всіх людей ім'я яких починається з певної літери")
    print("6. добавити нову людину")
    print("7. змінити данні")
    print("8. видалити запис")

    command = input()

    if command == "":
        break
    elif command == "1":
        user_query = input('Введіть запит: ')

        query_words = user_query.split()
        table_name = query_words[3] if len(query_words) > 2 else ""
        if table_name not in valid_tables:
            print(f"Помилка: неправильна назва таблиці '{table_name}'")
            continue

        if user_query.strip().upper().startswith("DELETE") or user_query.strip().upper().startswith("UPDATE"):
            if "WHERE" not in user_query.upper():
                print("Помилка: запити DELETE та UPDATE без умов заборонені.")
                continue

        try:
            result = session.execute(text(user_query))
            session.commit()

            if user_query.strip().upper().startswith("SELECT"):
                for row in result:
                    print(row)
            else:
                print(f"Запит виконано успішно: {user_query}")

        except Exception as e:
            print(f"Помилка при виконанні запиту: {e}")

    elif command == '2':
        result = session.query(Person).all()
        for person in result:
            print(person.firs_name, person.surrname)

    elif command == "3":
        city = input('Введіть місто: ')
        result = session.query(Person).filter_by(city=city).all()
        for person in result:
            print(person.firs_name, person.surrname, person.city)

    elif command == "4":
        city = input('Введіть місто: ')
        country = input('Введіть країну: ')
        result = session.query(Person).filter(or_(Person.city == city, Person.country == country)).all()
        for person in result:
            print(person.firs_name, person.surrname, person.city, person.country)

    elif command == "5":
        letter = input('Введіть літеру: ')
        result = session.query(Person).filter(Person.firs_name.like(f'{letter}%')).all()
        for person in result:
            print(person.firs_name, person.surrname)

    elif command == "6":
        person = Person(
            firs_name=input("Введіть ім'я: "),
            surrname=input("Введіть прізвище: "),
            city=input("Введіть місто: "),
            country=input("Введіть країну: "),
            birthd_date=input("Введіть дату народження (дд-мм-рррр): ")
        )
        session.add(person)
        session.commit()

    elif command == "7":
        first_name = input("Введіть ім'я: ")
        person = session.query(Person).filter(Person.firs_name == first_name).first()

        if person:
            person.city = input("Введіть місто: ")
            person.country = input("Введіть країну: ")
            session.commit()
        else:
            print("Запис не знайдено")

    elif command == "8":
        first_name = input("Введіть ім'я: ")
        person = session.query(Person).filter(Person.firs_name == first_name).first()

        if person:
            session.delete(person)
            session.commit()
        else:
            print("Запис не знайдено")

session.close()
