"""ООП-ОБЪЕКТНО-ОРЕНТИРОВАНИЕ ПРОГРАМИРОВАНИЕ"""

# Класс -> Это описание того, как должен выгллядить обхъект, то есть в классе мы описываем какими свойствами (даныыми) и поведением(функциями)должен обладеть объект



# Объект -> это сушность которую мы создаем от класса , у объекта есть состояние свойства(данных)

# Целью создание былло связать данные(атрибуты) с функцими(методы)котроые использовали их


# Свойствами (аттрибуты) называют обычные переменные внутри класса, в которых хрянятся данные оперделенного объекта


# Методы - это обычные функции которые описывают поеведение объекта функции внутрии класса назвыают методами


#----------------------------------------------------

# '''
# john = ['John', 'snow', 'King of North', 30]

# def show_info(human):
#     print(f'Name: {human[0]} {human [1]} , Age: {human [-1]}, job:{human[2]} , Salary:{human[3]}')

# show_info(john)
# '''

# class Human:
#     def __init__(self, name, last_name, age, job, salary):
#         self.name = name
#         self.last = last_name
#         self.age = age
#         self.job = job
#         self.salary = salary

#     def show_info(self):
#         return f'Name: {self.name}, Age: {self.age}, job:{self.job} , Salary:{self.salary}'

# john = Human('John', 'Snow', 30, 'King of North', 500)

# sultan = Human('Sultan', 'Katana', 19, 'Mentor', 100)

# print(dir(john))
# print(john.show_info())
# print(john.name)
# print(john.age)
# print('------------------------------')
# print(sultan.show_info())
# print(sultan.name)



#=============================================

# class Dog:
#     #аттрибуты класса
#     age = 0
#     ushi = True


#     def __init__(self, name, color):
#         """Инициализатор именно здесь создаются аттрибуты объекта"""
#         # в self прилетает ссылка на объект от класса
#         self.name = name # атрибуты объекта
#         self.color= color


#     def bark(self):
#         print(f'{self.name} лает!')



# bobik = Dog('Bobik', 'Brown')
# yumi = Dog(name ='Yumi', color='white')
# aktosh = Dog('Aktosh', 'gray')

# print(f'name: {bobik.name}, age: {bobik.age}, color: {bobik.color}, ushi: {bobik.ushi}')
# print(f'name: {yumi.name}, age: {yumi.age}, color: {yumi.color}, ushi: {yumi.ushi}')
# print(f'name: {aktosh.name}, age: {aktosh.age}, color: {aktosh.color}, ushi: {aktosh.ushi}')

# bobik.age = 2
# yumi.age = 1
# aktosh.age= 3
# aktosh.ushi = False

# print('After')
# print(f'name: {bobik.name}, age: {bobik.age}, color: {bobik.color}, ushi: {bobik.ushi}')
# print(f'name: {yumi.name}, age: {yumi.age}, color: {yumi.color}, ushi: {yumi.ushi}')
# print(f'name: {aktosh.name}, age: {aktosh.age}, color: {aktosh.color}, ushi: {aktosh.ushi}')

# yumi.bark()


#=====================Task1=============================
# class Song:
#     def __init__(self,title,author,year):
#         self.title = title
#         self.author = author
#         self.year = year

#     def show_title(self):
#         return f'Название этой песни {self.title}'

#     def show_author(self):
#         return f'Автор этой песни {self.author}'

#     def show_year(self):
#         return f'Эта песня вышла в {self.year} году'



# song = Song(title = 'Happy', author = 'Pharrell Williams', year = 2013)
# print(song.show_title())
# print(song.show_author())
# print(song.show_year())



# class Circle:
#     color = 'Синий'
#     pi = 3.14
#     def init(self, radius):
#         self.radius = radius
        
#     def get_area(self):
#         return self.pi*(self.radius**2)
        

# circle = Circle(radius=13)
# circle.color = 'желтый'
# print(circle.color)

# print(circle.get_area())

# class Taxi: 
#     def __init__(self, name, cost, cost_km): 
#         self.name = name 
#         self.cost = cost 
#         self.cost_km = cost_km 
#     def get_total_cost(self, km): 
#         self.cost = self.cost_km * km + self.cost 
#         return f'Такси {self.name}, стоимость поездки: {self.cost} сом' 
        
        
# taxi1 = Taxi(name='Namba',cost=29, cost_km=15) 
# taxi2 = Taxi(name='Yandex',cost=25, cost_km=17) 
# taxi3 = Taxi(name='Jorgo',cost=28, cost_km=15) 
# print(taxi1.get_total_cost(10)) 
# print(taxi2.get_total_cost(6)) 
# print(taxi3.get_total_cost(14))



# class Phone:
#     def __init__(self, name, last_name, phone):
#         self.name = name
#         self.last_name = last_name
#         self.phone=phone

#     def get_info(self):
#         print(f'Контакт: {self.name} {self.last_name}, телефон: {self.phone}')

# contact = Phone('John','Snow',+996707707707)
# contact.get_info()

# class Salary:
#     percent = 8
#     def __init__(self, salary, experience):
#         self.salary = salary
#         self.experience = experience

#     def count_percent(self):
#         return self.salary*self.percent/100*self.experience

# obj = Salary(10000, 10)     
# print(obj.count_percent()) 




# # task1
# class Class1:
#     def first(self):
#         pass

#     def second(self):
#         pass


# class Class2(Class1):
#     def third(self):
#         pass

#     def fourth(self):
#         pass



# obj = Class2()
# obj.first()
# obj.second()
# obj.third()
# obj.fourth()


# class A:
#     def method1(self):
#         print('Основной функционал')

# class B(A):
#     def method1(self):
#         super().method1()
#         print('Дополнительный функционал')

# obj = B()
# obj.method1()

# class MyString(str): 
#     def __init__(self, stroka1): 
#         self.stroka1 = stroka1 
#     def append(self, stroka2): 
#         self.stroka2 = stroka2 
#         self.stroka1 = self.stroka1 + self.stroka2 
#         return self.stroka1 
#     def pop(self): 
#         last_w = self.stroka1[-1] 
#         self.stroka1 = self.stroka1[:-1] 
#         return last_w 
#     def __str__(self) -> str: 
#         return self.stroka1 

# example = MyString('String') 
# example.append('hello')
# print(example.pop()) 
# print(example) 



# class Car: 
#     __speed=0
#     @property
#     def speed(self): 
#         return self.__speed
#     @speed.setter
#     def speed(self, new):
#         self.__speed = new
#         return self.__speed
# car1=Car() 
# print(car1.speed)
# car1.speed = 20
# print(car1.speed)







