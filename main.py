print('Hello, GitHub!')

# ===== ЦИКЛЫ =====

# Задание 1.1: Вывести на экран таблицу умножения от 1 до 9 с помощью вложенных циклов. Приветствуется красивый вывод с использованием табуляции.
print("1. Таблица умножения:")
for i in range(1, 10):
    for j in range(1, 10):
        print(f"{i * j:2}", end="\t")
    print()

# Задание 1.2: Посчитать сумму всех нечётных чисел от 1 до 100.
print("\n2. Сумма нечётных чисел от 1 до 100:")
sum_odd = sum(num for num in range(1, 101) if num % 2 != 0)
print(f"Сумма: {sum_odd}")

# Задание 1.3: Запросить у пользователя число и вывести все его делители.
print("\n3. Делители числа:")
number = int(input("Введите число: "))
deliteli = [str(i) for i in range(1, number + 1) if number % i == 0]
print(f"Делители: {' '.join(deliteli)}")

# Задание 1.4: Найти факториал числа, введённого пользователем, с помощью цикла.
print("\n4. Факториал числа:")
n = int(input("Введите число: "))
factorial = 1
for i in range(1, n + 1):
    factorial *= i
print(f"{n}! = {factorial}")

# Задание 1.5: Сгенерировать последовательность Фибоначчи длиной n и вывести её.
print("\n5. Последовательность Фибоначчи:")
n = int(input("Введите длину последовательности: "))
fibonacci = [0, 1][:n]
for i in range(2, n):
    fibonacci.append(fibonacci[i-1] + fibonacci[i-2])
print(f"Первые {n} чисел: {fibonacci}")

# ===== СПИСКИ =====

# Задание 2.0:
import random
numbers = [random.randint(-59, 50) for _ in range(10)]
print(f"\nСгенерированный список: {numbers}")

# Задание 2.1: Создать список из 10 чисел и вывести только чётные элементы.
print("\n1. Чётные элементы:")
even_numbers = [num for num in numbers if num % 2 == 0]
print(f"Чётные: {even_numbers}")

# Задание 2.2: Найти максимальное и минимальное число в списке.
print("\n2. Максимальное и минимальное:")
print(f"Max: {max(numbers)}, Min: {min(numbers)}")

# Задание 2.3: Запросить у пользователя 5 чисел, сохранить в списке, отсортировать и вывести.
print("\n3. Сортировка 5 чисел:")
user_numbers = []
for i in range(5):
    user_numbers.append(int(input(f"Число {i+1}: ")))
user_numbers.sort()
print(f"Отсортировано: {user_numbers}")

# Задание 2.4: Удалить из списка все дубликаты (без использования множеств).
print("\n4. Удаление дубликатов:")
unique_list = []
for num in numbers:
    if num not in unique_list:
        unique_list.append(num)
print(f"Без дубликатов: {unique_list}")

# Задание 2.5: Поменять местами первый и последний элемент списка.
print("\n5. Замена первого и последнего:")
if len(numbers) > 1:
    numbers[0], numbers[-1] = numbers[-1], numbers[0]
print(f"После замены: {numbers}")

# ===== СЛОВАРИ =====

# Задание 3.1: Создать словарь студентов и их оценками, вывести средний балл.
print("\n1. Средний балл студентов:")
students = {"Иван": 3.4, "Мария": 4.8, "Дмитрий": 5.0, "Ксения": 4.3}
average = sum(students.values()) / len(students)
print(f"Средний балл: {average:.2f}")

# Задание 3.2: Посчитать количество каждой буквы в строке.
print("\n2. Количество букв в строке:")
text = input("Введите строку: ").lower()
letter_count = {}
for char in text:
    if char.isalpha():
        letter_count[char] = letter_count.get(char, 0) + 1
print(f"Результат: {letter_count}")

# Задание 3.3: Создать словарь, где ключи – числа от 1 до 10, а значения – их квадраты.
print("\n3. Словарь квадратов:")
squares = {i: i**2 for i in range(1, 11)}
print(squares)

# Задание 3.4: Составить словарь из двух списков: ключи и значения.
print("\n4. Объединение списков в словарь:")
keys = ['a', 'b', 'c', 'd']
values = [1, 2, 3, 4]
result_dict = dict(zip(keys, values))
print(result_dict)

# ===== МНОЖЕСТВА =====

# Задание 4.1: Создать два множества и вывести их пересечение и объединение.
print("\n1. Операции с множествами:")
set1 = {1, 2, 3, 4, 5}
set2 = {4, 5, 6, 7, 8}
print(f"Пересечение: {set1 & set2}")
print(f"Объединение: {set1 | set2}")

# Задание 4.2: Найти все уникальные слова в тексте.
print("\n2. Уникальные слова:")
text = input("Введите текст: ").lower()
words = set(text.split())
print(f"Уникальные слова: {words}")

# Задание 4.3: Найти общие элементы двух списков с помощью множеств.
print("\n3. Общие элементы:")
list1 = [1, 2, 3, 4, 5]
list2 = [4, 5, 6, 7, 8]
common = set(list1) & set(list2)
print(f"Общие элементы: {common}")

# Задание 4.4: Проверить, является ли одно множество подмножеством другого.
print("\n4. Проверка подмножества:")
set_a = {1, 2, 3}
set_b = {1, 2, 3, 4, 5}
print(f"Является подмножеством: {set_a.issubset(set_b)}")

# Задание 4.5: Удалить из множества все элементы, которые меньше заданного числа.
print("\n5. Фильтрация множества:")
num_set = {1, 5, 10, 15, 20}
porog = int(input("Введите порог: "))
filtered_set = {x for x in num_set if x >= porog}
print(f"Результат: {filtered_set}")

# ===== КОМБИНИРОВАННЫЕ ЗАДАНИЯ =====

# Задание 5.1: Сгенерировать список из 20 случайных чисел и вывести только уникальные значения.
print("\n1. Уникальные значения из 20 случайных чисел:")
random_list = [random.randint(1, 10) for _ in range(20)]
unique_values = list(set(random_list))
print(f"Исходный: {random_list}")
print(f"Уникальные: {unique_values}")

# Задание 5.2: Создать словарь: элемент списка → количество его повторений.
print("\n2. Частота элементов:")
from collections import Counter
freq_dict = dict(Counter(random_list))
print(f"Частоты: {freq_dict}")

# Задание 5.3: Создать множество из слов длиной больше 5 символов.
print("\n3. Длинные слова:")
words = ["apple", "banana", "cat", "dog", "elephant"]
long_words = {word for word in words if len(word) > 5}
print(f"Слова >5 символов: {long_words}")

# Задание 5.4: Сохранить в словарь количество вхождений каждого слова в предложении.
print("\n4. Частота слов в предложении:")
sentence = input("Введите предложение: ").lower()
word_count = {}
for word in sentence.split():
    word = word.strip('.,!?')
    word_count[word] = word_count.get(word, 0) + 1
print(f"Частота слов: {word_count}")

# Задание 5.5: Преобразовать список в множество и обратно (убрать дубликаты).
print("\n5. Удаление дубликатов через множество:")
numbers = [1, 2, 2, 3, 4, 4, 5]
unique_list = list(set(numbers))
print(f"Без дубликатов: {unique_list}")

# Задание 5.6: Найти самый дорогой товар в словаре.
print("\n6. Самый дорогой товар:")
products = {"apple": 50, "banana": 30, "orange": 70, "milk": 100}
most_expensive = max(products, key=products.get)
print(f"Самый дорогой: {most_expensive} ({products[most_expensive]} руб.)")

# Задание 5.7: Определить, какие имена встречаются более одного раза и какое чаще всего.
print("\n7. Анализ имён:")
names = ["Иван", "Мария", "Петр", "Анна", "Иван", "Мария", "Иван"]
name_count = {}
for name in names:
    name_count[name] = name_count.get(name, 0) + 1

duplicates = [name for name, count in name_count.items() if count > 1]
popular = max(name_count, key=name_count.get)

print(f"Повторяющиеся: {duplicates}")
print(f"Самое частое: {popular} ({name_count[popular]} раз)")

# Задание 5.8: Составить словарь: символ → индекс его первого вхождения.
print("\n8. Первые вхождения символов:")
text = input("Введите строку: ")
first = {}
for i, char in enumerate(text):
    if char not in first:
        first[char] = i
print(f"Первые вхождения: {first}")