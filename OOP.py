import datetime


class WebPage:
    def __init__(self, title, content):
        self.title = title
        self.content = content
        self.publish_date = datetime.datetime.now()

    def display_details(self):
        print(f"Заголовок: {self.title}")
        print(f"Вміст: {self.content}")
        print(f"Дата публікації: {self.publish_date}")


class WebSite:
    def __init__(self, name, url):
        self.name = name
        self.url = url
        self.pages = []

    def add_page(self, title, content):
        for page in self.pages:
            if page.title == title:
                print("Сторінка з такою назвою вже існує.")
                return
        new_page = WebPage(title, content)
        self.pages.append(new_page)
        print(f"Сторінка '{title}' додана.")

    def delete_page(self, title):
        for page in self.pages:
            if page.title == title:
                self.pages.remove(page)
                print(f"Сторінка '{title}' видалена.")
                return
        print(f"Сторінка '{title}' не знайдена.")

    def edit_page(self, title, new_title, new_content):
        for page in self.pages:
            if page.title == title:
                if new_title == '':
                    page.title = page.title
                else:
                    page.title = new_title
                if new_content == '':
                    page.content = page.content
                else:
                    page.content = new_content
                print(f"Сторінка '{title}' відредагована.")
                return
        print(f"Сторінка '{title}' не знайдена.")

    def search_pages(self, keyword):
        found_pages = [page for page in self.pages if keyword in page.title or keyword in page.content]
        if found_pages:
            print("Знайдені сторінки:")
            for page in found_pages:
                page.display_details()
        else:
            print("Жодної сторінки не знайдено.")

    def display_info(self):
        print(f"Назва сайту: {self.name}")
        print(f"URL: {self.url}")
        print("Сторінки:")
        for page in self.pages:
            page.display_details()


class User:
    def __init__(self, username, password):
        self.username = username
        self.password = password


class WebSimulator:
    def __init__(self):
        self.users = []
        self.sites = []
        self.current_user = None
        self.current_site = None

    def register_user(self, username, password):
        for user in self.users:
            if user.username == username:
                print("Користувач з таким ім'ям вже існує.")
                return
        new_user = User(username, password)
        self.users.append(new_user)
        print(f"Користувач '{username}' зареєстрований.")

    def login(self, username, password):
        for user in self.users:
            if user.username == username and user.password == password:
                self.current_user = user
                print(f"Ви увійшли як '{username}'.")
                return
        print("Невірне ім'я користувача або пароль.")

    def logout(self):
        if self.current_user:
            print(f"Користувач '{self.current_user.username}' вийшов.")
            self.current_user = None
        else:
            print("Ніхто не увійшов в систему.")

    def create_site(self, name, url):
        if not (url.startswith("www.") and "." in url[url.index("www.") + 4:]):
            print("Невірний URL. URL повинен починатися з 'www.' і закінчуватися доменом.")
            return
        if self.current_user:
            new_site = WebSite(name, url)
            self.sites.append(new_site)
            self.current_site = new_site
            print(f"Сайт '{name}' створено.")
        else:
            print("Увійдіть, щоб створити сайт.")

    def select_site(self, name):
        for site in self.sites:
            if site.name == name:
                self.current_site = site
                print(f"Сайт '{name}' обраний.")
                return
        print(f"Сайт '{name}' не знайдений.")

    def run(self):
        while True:
            if self.current_user:
                if self.current_site:
                    print("\n1. Додати сторінку")
                    print("2. Видалити сторінку")
                    print("3. Редагувати сторінку")
                    print("4. Шукати сторінки")
                    print("5. Переглянути інформацію про сайт")
                    print("6. Вийти з сайту")
                    print("7. Вийти з програми")
                    choice = input("Виберіть опцію: ")

                    if choice == '1':
                        title = input("Введіть заголовок сторінки: ")
                        content = input("Введіть вміст сторінки: ")
                        self.current_site.add_page(title, content)
                    elif choice == '2':
                        title = input("Введіть заголовок сторінки для видалення: ")
                        self.current_site.delete_page(title)
                    elif choice == '3':
                        title = input("Введіть заголовок сторінки для редагування: ")
                        new_title = input("Введіть новий заголовок (Enter - залишити без змін): \n")
                        new_content = input("Введіть новий вміст (Enter - залишити без змін): \n")
                        self.current_site.edit_page(title, new_title, new_content)
                    elif choice == '4':
                        keyword = input("Введіть ключове слово для пошуку: ")
                        self.current_site.search_pages(keyword)
                    elif choice == '5':
                        self.current_site.display_info()
                    elif choice == '6':
                        self.current_site = None
                    elif choice == '7':
                        break
                    else:
                        print("Невірний вибір. Будь ласка, спробуйте ще раз.")
                else:
                    print("\n1. Створити сайт")
                    print("2. Вибрати сайт")
                    print("3. Вийти з системи")
                    print("4. Вийти з програми")
                    choice = input("Виберіть опцію: ")

                    if choice == '1':
                        name = input("Введіть назву сайту: ")
                        url = input("Введіть URL сайту: ")
                        self.create_site(name, url)
                    elif choice == '2':
                        name = input("Введіть назву сайту: ")
                        self.select_site(name)
                    elif choice == '3':
                        self.logout()
                    elif choice == '4':
                        break
                    else:
                        print("Невірний вибір. Будь ласка, спробуйте ще раз.")
            else:
                print("\n1. Зареєструватися")
                print("2. Увійти")
                print("3. Вийти з програми")
                choice = input("Виберіть опцію: ")

                if choice == '1':
                    username = input("Введіть ім'я користувача: ")
                    password = input("Введіть пароль: ")
                    self.register_user(username, password)
                elif choice == '2':
                    username = input("Введіть ім'я користувача: ")
                    password = input("Введіть пароль: ")
                    self.login(username, password)
                elif choice == '3':
                    break
                else:
                    print("Невірний вибір. Будь ласка, спробуйте ще раз.")


simulator = WebSimulator()
simulator.run()
