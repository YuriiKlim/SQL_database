from sqlalchemy import create_engine, Column, Integer, String, ForeignKey, Float, Sequence, func
from sqlalchemy.orm import sessionmaker, relationship
from sqlalchemy.orm import declarative_base
import json


with open('config.json', 'r') as f:
    data = json.load(f)
    db_user = data['user']
    db_password = data['password']

db_url = f'postgresql+psycopg2://{db_user}:{db_password}@localhost:5432/Sales'
engine = create_engine(db_url)

Base = declarative_base()


class Salesmen(Base):
    __tablename__ = 'salesmen'
    id = Column(Integer, Sequence('salesmen_id_seq'), primary_key=True)
    name = Column(String(256), nullable=False)
    sales = relationship("Sales", back_populates="salesman")


class Customers(Base):
    __tablename__ = 'customers'
    id = Column(Integer, Sequence('customers_id_seq'), primary_key=True)
    name = Column(String(256), nullable=False)
    sales = relationship("Sales", back_populates="customer")


class Sales(Base):
    __tablename__ = 'sales'
    id = Column(Integer, Sequence('sales_id_seq'), primary_key=True)
    amount = Column(Float, nullable=False)
    salesman_id = Column(Integer, ForeignKey('salesmen.id'), nullable=False)
    customer_id = Column(Integer, ForeignKey('customers.id'), nullable=False)
    salesman = relationship("Salesmen", back_populates="sales")
    customer = relationship("Customers", back_populates="sales")


Base.metadata.create_all(bind=engine)


Session = sessionmaker(bind=engine)
session = Session()


def display_all_sales():
    sales = session.query(Sales).all()
    for sale in sales:
        print(f"Угода ID: {sale.id}, Сума: {sale.amount}, Продавець: {sale.salesman.name}, Покупець: {sale.customer.name}")


def display_sales_by_salesman(salesman_name):
    salesman = session.query(Salesmen).filter_by(name=salesman_name).first()
    if salesman:
        sales = session.query(Sales).filter_by(salesman_id=salesman.id).all()
        for sale in sales:
            print(f"Угода ID: {sale.id}, Сума: {sale.amount}, Покупець: {sale.customer.name}")
    else:
        print("Продавця не знайдено")


def display_max_sale():
    sale = session.query(Sales).order_by(Sales.amount.desc()).first()
    if sale:
        print(f"Максимальна угода: ID {sale.id}, Сума: {sale.amount}, Продавець: {sale.salesman.name}, Покупець: {sale.customer.name}")
    else:
        print("Угод не знайдено")


def display_min_sale():
    sale = session.query(Sales).order_by(Sales.amount).first()
    if sale:
        print(f"Мінімальна угода: ID {sale.id}, Сума: {sale.amount}, Продавець: {sale.salesman.name}, Покупець: {sale.customer.name}")
    else:
        print("Угод не знайдено")


def display_max_sale_by_salesman(salesman_name):
    salesman = session.query(Salesmen).filter_by(name=salesman_name).first()
    if salesman:
        sale = session.query(Sales).filter_by(salesman_id=salesman.id).order_by(Sales.amount.desc()).first()
        if sale:
            print(f"Максимальна угода для продавця {salesman.name}: ID {sale.id}, Сума: {sale.amount}, Покупець: {sale.customer.name}")
        else:
            print("Угод для цього продавця не знайдено")
    else:
        print("Продавця не знайдено")


def display_min_sale_by_salesman(salesman_name):
    salesman = session.query(Salesmen).filter_by(name=salesman_name).first()
    if salesman:
        sale = session.query(Sales).filter_by(salesman_id=salesman.id).order_by(Sales.amount).first()
        if sale:
            print(f"Мінімальна угода для продавця {salesman.name}: ID {sale.id}, Сума: {sale.amount}, Покупець: {sale.customer.name}")
        else:
            print("Угод для цього продавця не знайдено")
    else:
        print("Продавця не знайдено")


def display_max_sale_by_customer(customer_name):
    customer = session.query(Customers).filter_by(name=customer_name).first()
    if customer:
        sale = session.query(Sales).filter_by(customer_id=customer.id).order_by(Sales.amount.desc()).first()
        if sale:
            print(f"Максимальна угода для покупця {customer.name}: ID {sale.id}, Сума: {sale.amount}, Продавець: {sale.salesman.name}")
        else:
            print("Угод для цього покупця не знайдено")
    else:
        print("Покупця не знайдено")


def display_min_sale_by_customer(customer_name):
    customer = session.query(Customers).filter_by(name=customer_name).first()
    if customer:
        sale = session.query(Sales).filter_by(customer_id=customer.id).order_by(Sales.amount).first()
        if sale:
            print(f"Мінімальна угода для покупця {customer.name}: ID {sale.id}, Сума: {sale.amount}, Продавець: {sale.salesman.name}")
        else:
            print("Угод для цього покупця не знайдено")
    else:
        print("Покупця не знайдено")


def display_top_salesman():
    result = session.query(Sales.salesman_id, func.sum(Sales.amount).label('total')).group_by(Sales.salesman_id).order_by(func.sum(Sales.amount).desc()).first()
    if result:
        salesman = session.query(Salesmen).get(result.salesman_id)
        print(f"Продавець з максимальною сумою продажів: {salesman.name}, Сума: {result.total}")
    else:
        print("Угод не знайдено")


def display_bottom_salesman():
    result = session.query(Sales.salesman_id, func.sum(Sales.amount).label('total')).group_by(Sales.salesman_id).order_by(func.sum(Sales.amount)).first()
    if result:
        salesman = session.query(Salesmen).get(result.salesman_id)
        print(f"Продавець з мінімальною сумою продажів: {salesman.name}, Сума: {result.total}")
    else:
        print("Угод не знайдено")


def display_top_customer():
    result = session.query(Sales.customer_id, func.sum(Sales.amount).label('total')).group_by(Sales.customer_id).order_by(func.sum(Sales.amount).desc()).first()
    if result:
        customer = session.query(Customers).get(result.customer_id)
        print(f"Покупець з максимальною сумою покупок: {customer.name}, Сума: {result.total}")
    else:
        print("Угод не знайдено")


def display_avg_sale_by_customer(customer_name):
    customer = session.query(Customers).filter_by(name=customer_name).first()
    if customer:
        result = session.query(func.avg(Sales.amount)).filter(Sales.customer_id == customer.id).scalar()
        print(f"Середня сума покупки для покупця {customer.name}: {result}")
    else:
        print("Покупця не знайдено")


def display_avg_sale_by_salesman(salesman_name):
    salesman = session.query(Salesmen).filter_by(name=salesman_name).first()
    if salesman:
        result = session.query(func.avg(Sales.amount)).filter(Sales.salesman_id == salesman.id).scalar()
        print(f"Середня сума продажу для продавця {salesman.name}: {result}")
    else:
        print("Продавця не знайдено")


def insert_salesman():
    name = input("Введіть ім'я продавця: ")
    salesman = Salesmen(name=name)
    session.add(salesman)
    session.commit()
    print(f"Продавець {name} доданий успішно")


def insert_customer():
    name = input("Введіть ім'я покупця: ")
    customer = Customers(name=name)
    session.add(customer)
    session.commit()
    print(f"Покупець {name} доданий успішно")


def insert_sale():
    amount = float(input("Введіть суму угоди: "))
    salesman_id = int(input("Введіть ID продавця: "))
    customer_id = int(input("Введіть ID покупця: "))
    sale = Sales(amount=amount, salesman_id=salesman_id, customer_id=customer_id)
    session.add(sale)
    session.commit()
    print("Угода додана успішно")


def update_salesman():
    salesman_id = int(input("Введіть ID продавця для оновлення: "))
    name = input("Введіть нове ім'я продавця: ")
    salesman = session.query(Salesmen).get(salesman_id)
    if salesman:
        salesman.name = name
        session.commit()
        print(f"Продавець з ID {salesman_id} оновлений успішно")
    else:
        print("Продавця не знайдено")


def update_customer():
    customer_id = int(input("Введіть ID покупця для оновлення: "))
    name = input("Введіть нове ім'я покупця: ")
    customer = session.query(Customers).get(customer_id)
    if customer:
        customer.name = name
        session.commit()
        print(f"Покупець з ID {customer_id} оновлений успішно")
    else:
        print("Покупця не знайдено")


def update_sale():
    sale_id = int(input("Введіть ID угоди для оновлення: "))
    amount = float(input("Введіть нову суму угоди: "))
    sale = session.query(Sales).get(sale_id)
    if sale:
        sale.amount = amount
        session.commit()
        print(f"Угода з ID {sale_id} оновлена успішно")
    else:
        print("Угоду не знайдено")


def delete_salesman():
    salesman_id = int(input("Введіть ID продавця для видалення: "))
    salesman = session.get(Salesmen, salesman_id)
    if salesman:
        session.query(Sales).filter(Sales.salesman_id == salesman_id).delete()
        session.delete(salesman)
        session.commit()
        print(f"Продавець з ID {salesman_id} видалений успішно")
    else:
        print("Продавця не знайдено")

def delete_customer():
    customer_id = int(input("Введіть ID покупця для видалення: "))
    customer = session.get(Customers, customer_id)
    if customer:
        session.query(Sales).filter(Sales.customer_id == customer_id).delete()
        session.delete(customer)
        session.commit()
        print(f"Покупець з ID {customer_id} видалений успішно")
    else:
        print("Покупця не знайдено")


def delete_sale():
    sale_id = int(input("Введіть ID угоди для видалення: "))
    sale = session.query(Sales).get(sale_id)
    if sale:
        session.delete(sale)
        session.commit()
        print(f"Угода з ID {sale_id} видалена успішно")
    else:
        print("Угоду не знайдено")


while True:
    print("Введіть команду")
    print("1. Відображення усіх угод")
    print("2. Відображення угод конкретного продавця")
    print("3. Відображення максимальної за сумою угоди")
    print("4. Відображення мінімальної за сумою угоди")
    print("5. Відображення максимальної суми угоди для конкретного продавця")
    print("6. Відображення мінімальної за сумою угоди для конкретного продавця")
    print("7. Відображення максимальної за сумою угоди для конкретного покупця")
    print("8. Відображення мінімальної за сумою угоди для конкретного покупця")
    print("9. Відображення продавця з максимальною сумою продажів за всіма угодами")
    print("10. Відображення продавця з мінімальною сумою продажів за всіма угодами")
    print("11. Відображення покупця з максимальною сумою покупок за всіма угодами")
    print("12. Відображення середньої суми покупки для конкретного покупця")
    print("13. Відображення середньої суми покупки для конкретного продавця")
    print("14. Додавання нового продавця")
    print("15. Додавання нового покупця")
    print("16. Додавання нової угоди")
    print("17. Оновлення даних продавця")
    print("18. Оновлення даних покупця")
    print("19. Оновлення даних угоди")
    print("20. Видалення продавця")
    print("21. Видалення покупця")
    print("22. Видалення угоди")
    print("23. Вихід")

    command = input()

    if command == "23":
        break
    elif command == "1":
        display_all_sales()
    elif command == "2":
        salesman_name = input("Введіть ім'я продавця: ")
        display_sales_by_salesman(salesman_name)
    elif command == "3":
        display_max_sale()
    elif command == "4":
        display_min_sale()
    elif command == "5":
        salesman_name = input("Введіть ім'я продавця: ")
        display_max_sale_by_salesman(salesman_name)
    elif command == "6":
        salesman_name = input("Введіть ім'я продавця: ")
        display_min_sale_by_salesman(salesman_name)
    elif command == "7":
        customer_name = input("Введіть ім'я покупця: ")
        display_max_sale_by_customer(customer_name)
    elif command == "8":
        customer_name = input("Введіть ім'я покупця: ")
        display_min_sale_by_customer(customer_name)
    elif command == "9":
        display_top_salesman()
    elif command == "10":
        display_bottom_salesman()
    elif command == "11":
        display_top_customer()
    elif command == "12":
        customer_name = input("Введіть ім'я покупця: ")
        display_avg_sale_by_customer(customer_name)
    elif command == "13":
        salesman_name = input("Введіть ім'я продавця: ")
        display_avg_sale_by_salesman(salesman_name)
    elif command == "14":
        insert_salesman()
    elif command == "15":
        insert_customer()
    elif command == "16":
        insert_sale()
    elif command == "17":
        update_salesman()
    elif command == "18":
        update_customer()
    elif command == "19":
        update_sale()
    elif command == "20":
        delete_salesman()
    elif command == "21":
        delete_customer()
    elif command == "22":
        delete_sale()


session.close()
