from datetime import datetime, date
from decimal import Decimal
from fractions import Fraction

def task1():
    """1. List comprehension (простое преобразование)"""
    squares = [x**2 for x in range(1, 11)]
    print("Квадраты чисел от 1 до 10:", squares)

def task2():
    """2. List comprehension (фильтрация)"""
    evens = [x for x in range(1, 20) if x % 2 == 0]
    print("Четные числа от 1 до 20:", evens)

def task3():
    """3. List comprehension (работа со строками)"""
    words = ["python", "Java", "c++", "Rust", "go"]
    result = [word.upper() for word in words if len(word) > 3]
    print("Слова в верхнем регистре (длина > 3):", result)
    
class Countdown:
    def __init__(self, n):
        self.n = n
    
    def __iter__(self):
        return iter(range(self.n, 0, -1))

def task4():
    """4. Демонстрация итератора"""
    print("Countdown(5):", end=" ")
    for x in Countdown(5):
        print(x, end=" ")
    print()

def fibonacci(n):
    """5. Собственный генератор"""
    x1 = 0
    x2 = 1
    for _ in range(n):
        yield x1
        x1, x2 = x2, x1 + x2

def task5():
    """5. Демонстрация генератора"""
    print("Первые 5 чисел Фибоначчи:", end=" ")
    for num in fibonacci(5):
        print(num, end=" ")
    print()

def task6():
    """6. Финансовый калькулятор"""
    try:
        P = Decimal(input("Начальная сумма (руб): "))
        r = Decimal(input("Процентная ставка (%): "))
        t = Decimal(input("Срок (лет): "))
        
        S = P * (1 + r / (12 * 100)) ** (12 * t)
        profit = S - P
        
        print(f"Итоговая сумма: {S:.2f} руб")
        print(f"Прибыль: {profit:.2f} руб")
    except:
        print("Ошибка ввода!")

def task7():
    """7. Работа с дробями"""
    a = Fraction(3, 4)
    b = Fraction(5, 6)
    
    print(f"3/4 + 5/6 = {a + b}")
    print(f"3/4 - 5/6 = {a - b}")
    print(f"3/4 × 5/6 = {a * b}")
    print(f"3/4 ÷ 5/6 = {a / b}")

def task8():
    """8. Текущая дата и время"""
    now = datetime.now()
    print("Текущая дата и время:", now)
    print("Только дата:", now.date())
    print("Только время:", now.time().strftime("%H:%M:%S"))

def task9():
    """9. Разница дат"""
    try:
        print("=" * 50)
        print("           КАЛЬКУЛЯТОР ДНЕЙ РОЖДЕНИЯ")
        print("=" * 50)
        
        birthday_input = input("Введите вашу дату рождения в формате ГГГГ-ММ-ДД: ")
        denrozdenia = datetime.strptime(birthday_input, "%Y-%m-%d").date()
        today = date.today()
        
        # Вычисляем прожитые дни
        days_lived = (today - denrozdenia).days
        years_old = days_lived // 365
        
        # Вычисляем дни до следующего дня рождения
        next_birthday = date(today.year, denrozdenia.month, denrozdenia.day)
        if next_birthday < today: 
            next_birthday = date(today.year + 1, denrozdenia.month, denrozdenia.day)
        
        days_until_next = (next_birthday - today).days

        print("\n" + "─" * 50)
        
        if days_until_next == 0:
            print("ПОЗДРАВЛЯЕМ! СЕГОДНЯ ВАШ ДЕНЬ РОЖДЕНИЯ!")
        else:
            print(f"Вы прожили: {days_lived:,} дней".replace(',', ' '))
            print(f"Ваш возраст: {years_old} лет")
            print(f"До следующего дня рождения: {days_until_next} дней")
        
        print("─" * 50)
        print()
            
    except ValueError:
        print("\nОшибка! Неверный формат даты.")
        print("ℹПожалуйста, используйте формат ГГГГ-ММ-ДД")
        print("Например: 1990-05-15")

def task10():
    """10. Форматирование даты"""
    now = datetime.now()
    months = ["января", "февраля", "марта", "апреля", "мая", "июня",
              "июля", "августа", "сентября", "октября", "ноября", "декабря"]
    
    result = f"Сегодня {now.day} {months[now.month-1]} {now.year} года, время: {now.hour:02d}:{now.minute:02d}" # [now.month-1]} так как в списке счёт начинается с нуля (0), а не с единицы (1)
    print(result)

def main():
    tasks = {
        '1': ("List comprehension (квадраты)", task1),
        '2': ("List comprehension (четные)", task2),
        '3': ("List comprehension (строки)", task3),
        '4': ("Итератор Countdown", task4),
        '5': ("Генератор Фибоначчи", task5),
        '6': ("Финансовый калькулятор", task6),
        '7': ("Операции с дробями", task7),
        '8': ("Текущая дата и время", task8),
        '9': ("Разница дат", task9),
        '10': ("Форматирование даты", task10),
        '0': ("Выход", exit)
    }
    
    while True:
        print("="*50)
        print("Лабораторная работа 3")
        print("="*50)
        
        for key in tasks:
            task_name = tasks[key][0]  # Название задания
            print(f"{key}. {task_name}")
        
        choice = input("\nВыберите задание (0-10): ")
        
        if choice in tasks:
            print(f"\n--- {tasks[choice][0]} ---")
            tasks[choice][1]()
            input("\nНажмите Enter для продолжения...")
        else:
            print("Неверный выбор!")

if __name__ == "__main__":
    main()