# Множественные наследование - это когда класс наследование от двух или более классов




# class Auto:
#     def play_music_at_station(self):
#         print('Music ids playing!')


#     def ride(self):
#         print('We\'re riding on the ground!')


# class Plane:
#     def play_music_at_station(self):
#         print('Listining Ed Sheren!')


#     def fly(self):
#             print('We\'re flaying')



# class FutureAuto(Auto, Plane):
#     pass



# obj = FutureAuto()
# obj.ride()
# obj.fly()
# obj.play_music_at_station()



# class A:
#     def print_A(self):
#         print('A')


# class B:
#     def print_B(self):
#         print('B')


# class C:
#     def print_C(self):
#         print('C')

# class MyClass(A,B,C):
#     pass


# obj = MyClass()
# obj.print_A()
# obj.print_B()
# obj.print_C()
# print(MyClass.mro())



# class Test:
#     pass

# a = Test()
# print(dir(a))
# print(dir(a))

# Проблема ромба(решена с помошью mro)
'''Mro (Method Resoltution Order) - механизм для коректного поиска родительских методов. Был создан для решение проблемы робма, котороя  появилось после введение класса  object  в пайтон. Поиск идет таким образом что если у родитнельских классов один общий предок , то идет поиск в ширину.'''

# class Zero:
#     def say(self):
#         print('class Zero!')


# class First(Zero):
#     # def say(self):
#     #     print('class First')
#     ...

# class Second(Zero):
#     ...
#     # def say(self):
#     #     print('class Second')


# class MyClass(First, Second):
#     def say(self):
#         super().say()
#         print('My CLass')


# obj = MyClass()
# obj.say()
# print(MyClass.mro())


# проблема перекрестного наследование 

# class Y:
#     pass

# class X:
#     pass
# class A(X,Y):
#     pass
# class B(X, Y):
#     pass
# class MyMro(type):
#     def mro(cls) -> list[type]:
#         return [cls, A, B, X, Y, object]

# class MyClass(A,B, metalass=MyMro):
#     pass

# obj = MyClass()
# print(MyClass.mro())



# class  RadioMixin:
#     def play_music(self):
#         title_py = 'title'
#         print( "Песня называется {title_py}")

# class Auto(RadioMixin):
#     pass

# class Boat(RadioMixin):
#     pass

# class  Amphibian(Auto,Boat):
#     pass

# auto = Auto()
# boat = Boat()
# obj = Amphibian()
# obj.play_music()

# import datetime
# class Clock:
#     def current_time(self):
#         print('14:10:41')

# class Alarm:
#     def on(self):
#         print('')

#     def off(self):
#         print('09:00:00')

# class AlarmClock(Clock, Alarm):
#     def alarm_on(self):
#         print('Будильник включён')

# clock = AlarmClock()
# clock.current_time()
# clock.alarm_on()

# import datetime
# class Clock:
#     def current_time(self):
#         dt_now = datetime.datetime.today().strftime("%H:%M:%S")
#         print(dt_now)

# class Alarm:

#     @staticmethod
#     def on():
#         print('Будильник включен')

#     @staticmethod
#     def off():
#         print('Будильник выключен')

# class AlarmClock(Clock, Alarm):
#     @staticmethod
#     def alarm_on():
#         Alarm.on()

# clock = AlarmClock()
# clock.current_time()
# clock.alarm_on()


# from abc import ABC, abstractmethod

# class Coder():
#     count_code_time = 0
#     @abstractmethod
#     def get_info(self):
#         pass
#     @abstractmethod
#     def coding(self):
#         pass

# class Backend(Coder):
#     def __init__(self, experience, languages_backend):
#         self.experience = 'experince'
#         self.languages_backend = 'languages_backend'
#     def get_info(self, experience, languages_backend):
#         self.coding = self.count_code_time 
#         print(f'Python разработчик, уровень:Junior, потрачено {self.coding} часов на программирование')

# class Frontend(Coder):
#     def __init__(self,experience, languages_frontend):
#         self.experience = experience
#         self.languages_frontend = languages_frontend
#     def get_info(self, experience , languages_frontend):
#         self.coding = self.count_code_time
#         print(f'Javascript разработчик, уровень: Middle, потрачено {self.coding} часов на программирование')
#         print(f'Python and JS разработчик, уровень: Senior, потрачено {self.coding} часов на программирование')

# class Fullstack(Backend, Frontend):
#     pass

# a = Backend()
# b = Frontend()
# c = Fullstack()
# a.coding(12) 
# b.coding(45) 
# c.coding(17) 
# print(a.get_info()) 
# print(b.get_info()) 
# print(c.get_info()) 



# Переопределите в обоих классах методы get_info и coding так, чтобы он принимал количество часов кодинга и при каждом вызове этого метода добавлял это значение к count_code_time.
# Напишите абстрактный класс Coder с атрибутом класса count_code_time = 0 и абстрактными методами get_info и coding.

# Создайте классы Backend и Frontend, которые наследуют все атрибуты и методы от класса Coder.

# Класс Backend должен принимать дополнительно параметры experience и languages_backend, а Frontend такие параметры как — experience и languages_frontend соответственно.



# Также бывают Fullstack разработчики, поэтому создайте данный класс так чтобы у него были атрибуты и методы предыдущих классов. При этом нее определяйте никаких методов и атрибутов в данном классе он должен наследовать их от родительских классов.

# Создайте экземпляры a, b, c от классов Backend, Frontend, Fullstack соответственно и вызовите их методы.

# Ввод должен быть:

# a.coding(12) 
# b.coding(45) 
# c.coding(17) 
# print(a.get_info()) 
# print(b.get_info()) 
# print(c.get_info()) 
# Вывод:

# Python разработчик, уровень: Junior, потрачено 12 часов на программирование

# Javascript разработчик, уровень: Middle, потрачено 45 часов на программирование

# Python and JS разработчик, уровень: Senior, потрачено 17 часов на программирование 

# class SmartPhones:
#     def __init__(self, name, color, memory):
#         self.name = name
#         self.color = color
#         self.memory = memory
#         self.battery = 0

#     def __str__(self):
#         return f"{self.name} {self.memory}"

#     def charge(self, number):
#         self.battery += number
    
# class Iphone(SmartPhones):
#     def __init__(self, name, color, memory, ios):
#         super().__init__(name, color, memory)
#         self.ios = ios

#     def send_imessage(self, string):
#         return f"sending {string} from {self.name} {self.memory}"


# class Samsung(SmartPhones):
#     def __init__(self, name, color, memory, android):
#         super().__init__(name, color, memory)
#         self.android = android

#     def show_time(self):
#         import datetime
#         return datetime.datetime.now().time()


# phone = SmartPhones('generic', 'blue', '128GB') 
# print(phone) 

# print(phone.battery) 
# phone.charge(20) 
# print(phone.battery) 

# iphone7 = Iphone('Iphone 7', 'gold', '128gb', '12.1.3') 
# print(iphone7)
# print(iphone7.send_imessage('hello'))

# samsung21 = Samsung('Samsung A21', 'black', '256gb', 'Oreo') 
# print(samsung21.show_time())


# class CustomError(Exception):
#     def __init__(self, message):
#         self.message = message
    

# capitals_error = CustomError('ТОЛЬКО БОЛЬШИЕ БУКВЫ РАЗРЕШЕНЫ В ЭТОМ КОДЕ')

# def check_letters(str_):
#     if str_.islower():
#         raise CustomError('ТОЛЬКО БОЛЬШИЕ БУКВЫ РАЗРЕШЕНЫ В ЭТОМ КОДЕ')
#     else: return f'ВСЕ ОТЛИЧНО! {str_}'

# print(check_letters("HELLO"))

# class Square: 
#     def __init__(self, side) -> None: 
#         self.side = side 
#     def get_area(self): 
#         return self.side * self.side 
# class Triangle: 
#     def __init__(self, height, base) -> None: 
#         self.height = height 
#         self.base = base 
#     def get_area(self): 
#         return int(0.5*self.base*self.height) 
# class Pyramid(Triangle, Square): 
#     def __init__(self, height, base) -> None: 
#         super().__init__(height, base) 
#     def get_volume(self): 
#         return int(1/3*self.base**2*self.height) 

# obj = Square(3) 
    
# print(obj.get_area()) 
# obj2 = Triangle(3,5) 
# print(obj2.get_area()) 
# obj3 = Pyramid(10,10) 
# print(obj3.get_volume())


# class Game:
#     __level = 0
#     def __init__(self, name):
#         self.name = name
#     def get_level(self):
#         return self.__level
#     def set_level(self, level):
#         self.__level = level
# game = Game('name')
# print(game.get_level())
# game.set_level(10)
# print(game.get_level())



# class Game:
#     __level = 0
#     @property
#     def level(self):
#         return self.__level
# game = Game()
# print(game.level)

# class Game:
#     __level = 0
#     @property
#     def get_level(self):
#         return self.__level
#     @get_level.setter
#     def level(self, value):
#         self.__level = value
# game = Game()
# print(game.get_level)
# game.level = 10
# print(game.get_level)


# class Person:
#     def __init__(self):
#         self.__name = None
#         self.__last_name = None
#         self.__age = None
#         self.__email = None
#     def get_name(self):
#         return self.__name
#     def set_name(self,name):
#         self.__name = name
#     def get_last_name(self):
#         return self.__last_name
#     def set_last_name(self, last_name):
#         self.__last_name = last_name
#     def get_age(self):
#         return self.__age
#     def set_age(self, age):
#         self.__age = age
#     def get_email(self):
#         return self.__email
#     def set_email(self, email):
#         self.__email = email


# john = Person()
# print(john.get_name()) # None
# print(john.get_last_name()) # None
# print(john.get_age()) # None
# print(john.get_email()) # None
# john.set_name('John')
# john.set_last_name('Snow')
# john.set_age(30)
# john.set_email('johnsnow@gmail.com')
# print(john.get_name()) # John
# print(john.get_last_name()) # Snow
# print(john.get_age()) # 30
# print(john.get_email()) # johnsnow@gmail.com


class Dad: 
    name = 'John' 
    _last_name = 'Snow' 
    __age = 40 
class Me(Dad): 
    name = 'Sam' 
    def about_me(self): 
        print(f"My name is {self.name} {self._last_name} and I am {self.__age} years old") 
        __age = 10 
    def about_my_father(self): 
        print(f"My father is {Dad.name} {Dad._last_name}") 
me = Me() 
me.about_me() 
me.about_my_father()


