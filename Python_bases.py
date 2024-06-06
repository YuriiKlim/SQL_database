import random
# 1. Напишіть програму, яка приймає два цілих числа від
# користувача і виводить суму діапазону чисел між ними.

def sum_of_range(start, end):
    if start > end:
        start, end = end, start
    total_sum = sum(range(start, end + 1))
    return total_sum


try:
    num1 = int(input("Введіть перше ціле число: "))
    num2 = int(input("Введіть друге ціле число: "))

    result = sum_of_range(num1, num2)
    print(f"Сума чисел у діапазоні між {num1} і {num2} дорівнює {result}")
except ValueError:
    print("Будь ласка, введіть коректні цілі числа.")


# 2. Напишіть програму, для знаходження суми всіх парних
# чисел від 1 до 100.

def sum_of_even_numbers():
    total_sum = 0
    for number in range(1, 101):
        if number % 2 == 0:
            total_sum += number
    return total_sum


result = sum_of_even_numbers()
print(f"Сума всіх парних чисел від 1 до 100 дорівнює {result}")

# 3. Напишіть програму, яка приймає рядок від користувача і
# виводить кожну літеру рядка на окремому рядку.

def print_characters_individually(input_string):
    for character in input_string:
        print(character)


user_input = input("Введіть рядок: ")
print_characters_individually(user_input)

# 4. Напишіть програму, яка створює список цілих чисел та
# виводить новий список, який містить лише парні числа з
# вихідного списку.

def generate_random_list(size, lower_bound, upper_bound):
    return [random.randint(lower_bound, upper_bound) for _ in range(size)]


def filter_even_numbers(numbers):
    even_numbers = [number for number in numbers if number % 2 == 0]
    return even_numbers


list_size = 20
lower_bound = 1
upper_bound = 100

original_list = generate_random_list(list_size, lower_bound, upper_bound)

even_list = filter_even_numbers(original_list)

print(f"Вхідний список: {original_list}")
print(f"Список парних чисел: {even_list}")

# 5. Напишіть функцію, яка приймає список рядків від
# користувача і повертає новий список, що містить лише
# рядки, що починаються з великої літери.

def filter_capitalized_strings(strings):
    capitalized_strings = [string for string in strings if string and string[0].isupper()]
    return capitalized_strings


user_input = input("Введіть рядки, розділені комами: ")
string_list = [s.strip() for s in user_input.split(",")]

filtered_list = filter_capitalized_strings(string_list)

print(f"Рядки, що починаються з великої літери: {filtered_list}")

# 6. Напишіть функцію, яка приймає список рядків від
# користувача і повертає новий список, що містить лише
# рядки, які містять слово "Python"

def filter_strings_with_python(strings):
    python_strings = [string for string in strings if "python" in string.lower()]
    return python_strings


user_input = input("Введіть рядки, розділені комами: ")
string_list = [s.strip() for s in user_input.split(",")]

filtered_list = filter_strings_with_python(string_list)

print(f"Рядки, що містять слово 'Python': {filtered_list}")

# 7. (додаткове на кристалики)Напишіть програму, яка
# створює словник, де ключами є слова, а значеннями - їхні
# визначення. Дозвольте користувачу додавати, видаляти
# та шукати слова у цьому словнику.


class Dictionary:
    def __init__(self):
        self.dictionary = {
            "test": "testing"
        }

    def add_word(self):
        word = input("Введіть слово: ").strip()
        definition = input("Введіть визначення: ").strip()
        self.dictionary[word] = definition
        print(f"Слово '{word}' додано до словника.")

    def delete_word(self):
        word = input("Введіть слово для видалення: ").strip()
        if word in self.dictionary:
            del self.dictionary[word]
            print(f"Слово '{word}' видалено з словника.")
        else:
            print(f"Слово '{word}' не знайдено у словнику.")

    def search_word(self):
        word = input("Введіть слово для пошуку: ").strip()
        if word in self.dictionary:
            print(f"{word}: {self.dictionary[word]}")
        else:
            print(f"Слово '{word}' не знайдено у словнику.")

    def display_menu(self):
        print("\nМеню:")
        print("1. Додати слово")
        print("2. Видалити слово")
        print("3. Шукати слово")
        print("Enter. Вийти")

    def run(self):
        while True:
            self.display_menu()
            choice = input("Виберіть опцію: ").strip()
            if choice == '1':
                self.add_word()
            elif choice == '2':
                self.delete_word()
            elif choice == '3':
                self.search_word()
            elif choice == '':
                print("Вихід з програми.")
                break
            else:
                print("Невірний вибір. Будь ласка, спробуйте ще раз.")


dictionary_app = Dictionary()
dictionary_app.run()

# 8. (додаткове на кристалики)Використовуючи лямбдафункцію, напишіть вираз, який сортує список кортежів
# за другим елементом кожного кортежу (наприклад, [(1,
# 3), (3, 2), (2, 1)]).

tuples_list = [(1, 3), (3, 2), (2, 1)]

sorted_list = sorted(tuples_list, key=lambda x: x[1])

print(f"Відсортований список: {sorted_list}")
