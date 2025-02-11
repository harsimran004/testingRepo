# Encapsulation
class Car:
    def __init__(self, make, model):
        self.__make = make
        self.__model = model
    
    def set_make(self, make):
        self.__make = make
    
    def get_make(self):
        return self.__make

# Inheritance
class Animal:
    def speak(self):
        print("Animal speaks")

class Dog(Animal):
    def speak(self):
        print("Bark")

# Polymorphism
class Shape:
    def area(self):
        pass

class Circle(Shape):
    def __init__(self, radius):
        self.radius = radius
    
    def area(self):
        return 3.14 * self.radius * self.radius

class Square(Shape):
    def __init__(self, side):
        self.side = side
    
    def area(self):
        return self.side * self.side

# Abstraction
from abc import ABC, abstractmethod

class Vehicle(ABC):
    @abstractmethod
    def start(self):
        pass

class Car(Vehicle):
    def start(self):
        print("Car started")

class Bike(Vehicle):
    def start(self):
        print("Bike started")

# Constructor and Destructor
class Student:
    def __init__(self, name, age):
        self.name = name
        self.age = age
        print(f"Student {self.name} created.")
    
    def __del__(self):
        print(f"Student {self.name} deleted.")

# Demonstrating all concepts together
def demonstrate_oops():
    # Encapsulation
    my_car = Car("Toyota", "Corolla")
    print("Car Make:", my_car.get_make())
    my_car.set_make("Honda")
    print("Updated Car Make:", my_car.get_make())
    
    # Inheritance
    dog = Dog()
    dog.speak()  # Bark
    
    # Polymorphism
    shapes = [Circle(5), Square(4)]
    for shape in shapes:
        print("Area:", shape.area())

    # Abstraction
    vehicle1 = Car()
    vehicle2 = Bike()
    vehicle1.start()  # Car started
    vehicle2.start()  # Bike started
    
    # Constructor and Destructor
    student = Student("John", 21)
    del student

demonstrate_oops()

# Encapsulation
class Car:
    def __init__(self, make, model):
        self.__make = make
        self.__model = model
    
    def set_make(self, make):
        self.__make = make
    
    def get_make(self):
        return self.__make

my_car = Car("Toyota", "Corolla")
my_car.set_make("Honda")
print("Car Make:", my_car.get_make())

# Inheritance
class Animal:
    def speak(self):
        print("Animal speaks")

class Cat(Animal):
    def speak(self):
        print("Meow")

class Dog(Animal):
    def speak(self):
        print("Bark")

cat = Cat()
dog = Dog()
cat.speak()
dog.speak()

# Polymorphism
class Shape:
    def area(self):
        pass

class Circle(Shape):
    def __init__(self, radius):
        self.radius = radius
    
    def area(self):
        return 3.14 * self.radius * self.radius

class Square(Shape):
    def __init__(self, side):
        self.side = side
    
    def area(self):
        return self.side * self.side

shapes = [Circle(5), Square(4)]
for shape in shapes:
    print("Area:", shape.area())

# Abstraction
from abc import ABC, abstractmethod

class Vehicle(ABC):
    @abstractmethod
    def start(self):
        pass

class Car(Vehicle):
    def start(self):
        print("Car started")

class Bike(Vehicle):
    def start(self):
        print("Bike started")

vehicle1 = Car()
vehicle2 = Bike()
vehicle1.start()
vehicle2.start()

# Constructor and Destructor
class Student:
    def __init__(self, name, age):
        self.name = name
        self.age = age
        print(f"Student {self.name} created.")

    def __del__(self):
        print(f"Student {self.name} deleted.")

student = Student("John", 21)
del student
