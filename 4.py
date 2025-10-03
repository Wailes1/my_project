class Transport:
    def __init__(self, brand, speed):
        self.brand = brand
        self.speed = speed
    
    def move(self):
        print(f"Transport is moving at {self.speed} km/h")
    
    def __str__(self):
        return f"Transport: {self.brand}, Speed: {self.speed}"


class Car(Transport):
    def __init__(self, brand, speed, seats):
        super().__init__(brand, speed)
        self.seats = seats
    
    def honk(self):
        print("Beep beep!")
    
    def move(self):
        print(f"Car {self.brand} is driving at {self.speed} km/h")
    
    def __str__(self):
        return f"Transport: {self.brand}, Speed: {self.speed}, Seats: {self.seats}"
    
    def __len__(self):
        return self.seats
    
    def __eq__(self, other):
        if isinstance(other, Car):
            return self.speed == other.speed
        return False
    
    def __add__(self, other):
        if isinstance(other, Car):
            return self.speed + other.speed
        return NotImplemented


class Bike(Transport):
    def __init__(self, brand, speed, bike_type):
        super().__init__(brand, speed)
        self.type = bike_type
    
    def move(self):
        print(f"Bike {self.brand} is cycling at {self.speed} km/h")
    
    def __str__(self):
        return f"Transport: {self.brand}, Speed: {self.speed}, Type: {self.type}"


# Тестирование
if __name__ == "__main__":
    # Создание объектов
    transport = Transport("Avtobus", 60)
    car1 = Car("BMW", 220, 5)
    car2 = Car("Mercedes", 250, 4)
    car3 = Car("Kia", 180, 5)
    car4 = Car("Bugatti", 420, 2)
    bike = Bike("Honda", 35, "sport")
    
    # Вывод их на экран (чтобы сработал __str__)
    print("Вывод объектов через __str__")
    print(transport)
    print(car1)
    print(car2)
    print(car3)
    print(car4)
    print(bike)
    print()
    
    # Проверка методов move() и honk()
    print("Проверка методов move() и honk()")
    transport.move()
    car1.move()
    car2.move()
    car3.move()
    car4.move()
    bike.move()
    car1.honk()
    print()
    
    # Использование магических методов
    print("Использование магических методов")
    print(f"Seats in BMW: {len(car1)}")
    print(f"Seats in Bugatti: {len(car4)}")
    print(f"BMW == Mercedes: {car1 == car2}")
    print(f"Kia == Kia: {car3 == car3}")
    print(f"BMW + Bugatti: {car1 + car4} km/h")
    
    # Сложение машины и велосипеда
    print("Сложение машины и велосипеда")
    try:
        result = car1 + bike
        print(f"BMW + Honda bike: {result}")
    except TypeError as e:
        print(f"BMW + Honda bike: Error - {e}")
    print()
    
    # Дополнительное задание
    print("Дополнительное задание")
    vehicles = [transport, car1, car2, car3, car4, bike]
    for vehicle in vehicles:
        vehicle.move()
