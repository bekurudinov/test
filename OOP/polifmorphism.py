# функция полиформизма  - len()

# print(len('mekers'))
# print(len([1,2,3,4,5]))
# print(len({1: 2, 3: 4}))




# + (__add__)-  метод полиформизм

# print(5+5)
# print('hello' + 'world')
# print([1,2,3]+ [5,6,8])

# полиформизм -  способность метода обработвыть данные  разных типов(объекитов от класса ), обыччно это реализуется путрем создание базового класса и наличия двух или более подклассов которые все реализют (переоперделяет ) методы с одинаковой сигнатурой(названием)
# Широко распрастраненные определение : 'Один и интерфейс много реализаций'

# class Animal:
#     def  info(self):
#         pass

#     def make_sound(self):
#         pass



# class Dog(Animal):

#     def __init__(self, name, age):
#         self.name = name
#         self.age = age
#     def info(self):
#         print(f'It\'s a dog.Dogs name is {self.name}, age {self.age}')

#     def make_sound(self):
#         print('Bark bark')


# class Cat(Animal):

#     def __init__(self, name, age):
#         self.name = name
#         self.age = age
#     def info(self):
#         print(f'It\'s a cat.Cats name is {self.name}, age {self.age}')

#     def make_sound(self):
#         print('Meaw Meaw')


# cat = Cat('Garfild', 5)
# dog = Dog('Pluto', 9)
# for obj in (cat, dog):
#     obj.info()
#     obj.make_sound()
#     print()


'''=============================='''

# class A:
#     def __len__(self):
#         return 132

# a = A()
# str1 = 'makers'
# print(len(str1))
# print(len(a))
'''==============================='''
'''AБСТРАКЦИЯ (абстрактный класс )  его можно рассматривать как набор методов короые должны быть реализованы во всех дочерней классах котроые будут унаследованы от абстарактного класса'''

# Абстракный иетод это метод которого есть обявленные но нет реализции
# from abc import ABC, abstractmethod
# from math import pi

# class Shape(ABC):
#     def __init__(self, name):
#         self.name = name

#     @abstractmethod
#     def area(self):
#         pass
#     @abstractmethod
#     def info(self):
#         pass

# class Squre(Shape):
#     def  __init__(self, lenght):
#         super().__init__("Квадрат")
#         self.length = lenght


#     def area(self):
#         return self.length ** 2

#     def info(self):
#         print(f'Я {self.name},  у меня все угды 90 градусом!')

# class Circle(Shape):
#     def __init__(self, radius):
#         super().__init__(" Окружность")
#         self.radius = radius


#     def area(self):
#         return pi * self.radius ** 2

#     def info(self):
#         print(f'Я {self.name},и я фигура в двухиерной плоскасти!')


# a = Squre(4)
# b = Circle(5)
# for x in (a, b):
#     x.info()
#     print(x.area())
#     print()



'''==========='''

# from abc import ABC, abstractmethod

# class CheesPiece(ABC):
#     # обший метод который будут использоать все наследники этого класса 

#     def take(self):
#         print('take a chees piece')

#     # абстрактный метод который надо переопределить для каждого наслденика

#     @abstractmethod
#     def move(self):
#         pass

# class Queen(CheesPiece):
#     def move(self):
#         print('Queen moves where she  wants giagonally vertically and horizantallyy')

# class Pawn(CheesPiece):
#     def move(self):
#         print('The pawn can move directly to one cell!')


# q = Queen()
# p = Pawn()
# q.move()
# q.take()
# print()
# p.move()
# p.take()

# Создайте класс мобильного телефона. Определите непубличные атрибуты для imei, уровня заряда батареи, краткой информации об установленной ОС. Изначальный уровень заряда
# батареи – 100%, он не может опуститься ниже 0. Методы доступа к данным расходуют 0,5 % заряда при каждом обращении.
# Определите 2 публичных метода: для прослушивания музыки, и для просмотра видео.
# При каждом прослушивании музыки расходуется 5% заряда, а при просмотре видео – 7%.
# Если заряд достигает уровня ниже 10% - не давайте пользователю просматривать видео. При
# полной разрядке все методы телефона не доступны (выбрасывайте ошибку, что телефон
# разряжен).
# Также предусмотрите возможность заряжания батареи.



# class Phone:
#     def __init__(self, os, imei):
#         self.__os = os
#         self.__imei = imei
#         self.__battery_level = 100


#     @property
#     def battery_level(self):
#         if self.__battery_level < 0.5:
#             self.__battery_level = 0
#             raise Exception('telefon razryzhen')
#         self.__battery_level -= 0.5
#         print(self.__battery_level)

#     @property
#     def get_info(self):
#         if self.__battery_level < 0.5:
#             self.__battery_level = 0
#             raise Exception('telefon razryzhen')
#         self.__battery_level -= 0.5
#         print(f'OS: {self.__os}, IMEI: {self.__imei}')

#     def play_music(self):
#         if self.__battery_level < 0.5:
#             self.__battery_level = 0
#             raise Exception('telefon razryzhen')
#         self.__battery_level -= 0.5
#         print('Slushaem bek Borbieva')

#     def play_video(self):
#         if self.__battery_level <= 10:
#             raise Exception('Nedopustimyi uroven zaryada')
#         self.__battery_level -= 7
#         print('Smotrim Toples')

#     def charge_battery(self, sec):
#         from time import sleep
#         i = 1
#         while i<=sec:
#             sleep(1)
#             if self.__battery_level < 100:
#                 self.__battery_level +=1
#                 break
#                 print(f'Idet zaryadka battereyi! vash uroven zaryada: {self.__battery_level}')
#                 i += 1


# phone  = Phone(os='IOS', imei='12343565656')
# phone.battery_level
# phone.get_info
# phone.play_music()
# phone.play_music()
# phone.play_music()
# phone.play_music()
# phone.play_music()
# phone.play_music()
# phone.play_video()
# phone.play_video()
# phone.play_video()
# phone.play_video()
# phone.play_video()
# phone.play_video()
# phone.battery_level

# phone.charge_battery(50)
# phone.battery_level


    

    
#1 a = '12342342345' 
# b = [1,['a',5,6],2,3,4,5] 
# c = {1:'a', 2: {'a': 1, 'b': 2}, 3:'c'} 
# lst = [a, b, c]
# for item in lst:
#     print(len(item))

#2 class Dog:
#     def voice(self):
#         print("Гав")
    
# class Cat:
#     def voice(self):
#         print("Мяу")

# barsik = Cat()
# rex = Dog()

# def to_pet(pet):
#     pet.voice()

# to_pet(barsik)
# to_pet(rex)


# class Person:
#     def __init__(self, name, last_name):
#         self.name = name
#         self.last_name = last_name

#     def get_info(self):
#         print(f'Привет, меня зовут {self.name} {self.last_name}')
    
# class Employee(Person):
#     def __init__(self, name, last_name,work,status):
#         super().__init__(name, last_name)
#         self.work = work
#         self.status = status


#     def get_info(self):
#         print(f'Привет, меня зовут {self.name} {self.last_name}, я работаю в компании {self.work} на должности {self.status}')

# class Student(Person):
#     def __init__(self, name, last_name, university, course):
#         super().__init__(name, last_name)
#         self.university = university
#         self.course = course
#     def get_info(self):
#         print(f'Привет, меня зовут {self.name} {self.last_name}, я учусь в {self.university} на {self.course} курсе')

# def get_human_info(bek):
#         return bek.get_info()


# person = Person('Азамат', 'Айталиев')
# employee = Employee('Азамат', 'Айталиев', 'BEK', 'программист')
# student = Student('Азамат', 'Айталиев', 'Makers', 1)


# get_human_info(employee) 
# get_human_info(student) 
# get_human_info(person) 

'''
Expected:
Привет, меня зовут Азамат Айталиев
Привет, меня зовут Азамат Айталиев, я работаю в компании The Most на должности официант
Привет, меня зовут Азамат Айталиев, я учусь в КГЮА на 1 курсе

Recieved:
Привет, меня зовут Азамат Айталиев, я работаю в компании The Most на должности официант.
Привет, меня зовут Азамат Айталиев, я учусь в КГЮА на 1 курсе.
Привет, меня зовут Азамат Айталиев
'''


'''from abc import ABC, abstractmethod
from math import pi

class Shape(ABC):

    @abstractmethod
    def get_area(self):
        pass

class Triangle(Shape):
    def init(self, base, height):
        self.base = base
        self.height = height
    
    def get_area(self):
        return self.base * self.height * 0.5

class Square(Shape):
    def init(self, length):
        self.length = length

    def get_area(self):
        return self.length  2


class Circle(Shape):
    def __init__(self, radius):
        self.radius = radius

    def get_area(self):
        return pi * self.radius  2

triangle = Triangle(12, 6)
square = Square(5)
circle = Circle(5)

print(triangle.get_area())
print(square.get_area())
print(circle.get_area())'''

# from abc import ABC, abstractmethod
# from math import pi

# class Shape(ABC):

#     @abstractmethod
#     def get_area(self):
#         pass

# class Triangle(Shape):
#     def __init__(self, base, height):
#         self.base = base
#         self.height = height
    
#     def get_area(self):
#         return self.base * self.height * 0.5

# class Square(Shape):
#     def __init__(self, length):
#         self.length = length

#     def get_area(self):
#         return self.length ** 2


# class Circle(Shape):
#     def __init__(self, radius):
#         self.radius = radius

#     def get_area(self):
#         return pi * self.radius ** 2

# triangle = Triangle(5, 5)
# square = Square(5)
# circle = Circle(4)

# print(triangle.get_area())
# print(square.get_area())
# print(circle.get_area())



# class OS:
#     def __init__(self, version):
#         self.version = version

#     def copy(self, text):
#         pass


# class Windows(OS):
#     def copy(self, text):
#         return f'скопирован текст "{text}" горячими клавишами CTRL + C'


# class MacOS(OS):
#     def copy(self, text):
#         return f'скопирован текст "{text}" горячими клавишами COMMAND + C'


# class Linux(OS):
#     def copy(self, text):
#         return f'скопирован текст "{text}" горячими клавишами CTRL + SHIFT + C'


# win = Windows('Windows 10')
# mac = MacOS('MacOS Big Sur')
# lin = Linux('Ubuntu 20.04')

# print(win.copy('Полиморфизм — одна из основных парадигм ООП'))
# print(mac.copy('Полиморфизм - разное поведение одного и того же метода в разных классах'))
# print(lin.copy('На самом деле одинаковым является только имя метода, его исходный код зависит от класса'))

# class Language:
#     def __init__(self, level, type) -> None:
#         self.level = level
#         self.type = type
# class Python(Language):
#     def write_function(self, func_name, arg):
#         return f'def {func_name}({arg}):'
#     def create_variable(self, var_name, value):
#         if isinstance(value, str):
#             return f"{var_name} = '{value}'"
#         else:
#             return f"{var_name} = {value}"
# class JavaScript(Language):
#     def write_function(self, func_name, arg):
#         return f'function {func_name}({arg}) {{    }};'
#     def create_variable(self, var_name, value):
#         if isinstance(value, str):
#             return f"let {var_name} = '{value}';"
#         else:
#             return f"let {var_name} = {value};"

# py = Python('high-level', 'interpreted')
# js = JavaScript('high-level', 'interpreted')
# print(py.write_function('get_code', 'a')) 
# print(py.create_variable('name', 'John'))
# print(js.write_function('validate', 'form'))
# print(js.create_variable('password', 'hchjh'))
# # '''
# class Money:
#     def __init__(self, country, symbol):
#         self.country = country
#         self.symbol = symbol


# class Dollar(Money):
#     rate = 84.80


#     def exchange(self, amount):
#         return f"$ {amount} равен {Dollar.rate * amount} сомам"


# class Euro(Money):
#     rate = 98.40

    
#     def exchange(self, amount):
#         return f"€ {amount} равен {Euro.rate * amount} сомам"


# dol = Dollar('Alaska', '$')
# eu = Euro('France', '€')
# print(dol.exchange (100))
# print(eu.exchange (80))

# class Money:
#     def __init__(self, country, symbol) -> None:
#         self.counry = country
#         self.symbol = symbol

# class Dollar(Money):
#     rate = 84.80
#     def exchange(self, amount):
#         return f'$ {amount} равен {Dollar.rate*amount} сомам'

# class Euro(Money):
#     rate = 98.40
#     def exchange(self, amount):
#         return f'€ {amount} равен {Euro.rate*amount} сомам'
    
# dol = Dollar('Alaska', '$')
# eu = Euro('France', '€')
# print(dol.exchange(100))
# print(eu.exchange(80))





# class Planet:
#     def __init__(self, orbit):
#         self.orbit = orbit

# class Mercury(Planet):

#     def get_age(self, earth_age):
#         return f'на Меркурии ваш возраст составляет {int(earth_age * 365 /self.orbit)} лет'

# class Venus(Planet):
    

#     def get_age(self, earth_age):
#         return f'на Венере ваш возраст составляет {round(earth_age * 365 / self.orbit * 365)} дней'
# class Jupiter(Planet):
  
#     def get_age(self, earth_age):
#         return f'на Юпитере ваш возраст составляет {round(earth_age * 365 // self.orbit * 365 * 24)} часов'

# mercury = Mercury(88)
# venus = Venus(225)
# jupiter = Jupiter(12)


# print(venus.get_age(20))
# print(jupiter.get_age(20))
# print(mercury.get_age(20))

        
# Создайте классы Mercury, Venus, Jupiter, которые наследуют метод __init__ от родительского класса Planet. У объектов данного класса должен быть аттрибут orbit, орбита в классе Venus состовляет 225 земных дней, Mercury 88 земных дней, а на Jupiter 12 дней. У всех этих классов должен быть метод get_age, принимающий возраст в переменную earth_age и расчитывающий ваш возраст на данной планете.

# Метод должен возвращать возраст на Mercury в годах, на Venus в днях и на Jupiter в часах. Например, если возраст earth_age равен 20:

# на Венере ваш возраст составляет 11842 дней
# на Юпитере ваш возраст составляет 5326080 часов
# на Меркурии ваш возраст составляет 82 лет
