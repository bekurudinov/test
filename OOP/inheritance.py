# #Приниципы ООП:
# 1 Наследование
# 2 Инкапуляция
# 3 Полифармизм
# 4 Абстракция 
# 5 Композиция
# 6 Агреция 

'''==========================================='''

# Наслелование принимать методы и атрибуты для дочернего класса


# Родительский класс
# Дочерний класс
'''============================================='''

# class Animal:
#     def print_info(self):
#         print('I\'m an animal!')


# class Croco(Animal):
#     pass
#     # def print_info(self):
#     #     print('I\'m an animal!')

# class Croco(Animal):
#     pass

# class Lion(Animal):
#     pass

# class Dog(Animal):
#     pass


# croco = Croco()
# croco.print_info()


# class Animal:
#     name = None
#     golos = None
#     meal = None

#     def say(self):
#         print(f'this animal is {self.name}: {self.golos}')


#     def eat(self):
#         print(f'This animal is {self.name}: {self.meal}')
    

# class Lion(Animal):
#     name = 'lion'
#     golos = 'roar'
#     meal = 'meat'
#     griva = True


#     def say(self):
#         print(f'king of  Animal The {self.name}')

#     def info(self):
#         print(f'{self.name} griva: {self.griva}')



# class Dog(Animal):
#     name = 'dog'
#     golos = 'roar'
#     meal = 'meat'

# class Koala(Animal):
#     name = 'koala'
#     golos = 'roar'
#     meal = 'efkalit'



# rex = Dog()
# simba = Lion()
# julin = Koala()
# rex.say()
# rex.eat()


# simba.say()
# simba.eat()
# simba.info()

# julin.say()
# julin.eat()

'''================================================================'''


# class Person:
#     def info(self):
#         print('I\'m person from Bishkek')

# class Student(Person):
#     def info(self):
#         super().info()
#         print('Im study at Manas University!')


# obj = Student() #I'm person from Bishkek Im study at Manas University!
# obj.info()

# obj2 = Person()  #I'm person from Bishkek
# obj2.info()


# class Laptop:
#     def __init__(self, brand, model, price):
#         self.brand = brand
#         self.model = model
#         self.price = price

#     def get_info(self):
#         return {'brand':self.brand, 'model':self.model, 'price':self.price}
    
# class Macbook(Laptop):
#     def __init__(self, brand, model, price, year, display):
#         super().__init__(brand, model, price)
#         self.year = year
#         self.display = display

#     def get_info(self):
#         repr = super().get_info
#         repr['year'] = self.year
#         repr['display']= self.display
#         return repr


# class Acer(Laptop):
#     def __init__(self, brand, model, price,videocard, display):
#         super().__init__(brand, model, price)
#         self.videocard = videocard
#         self.display = display


#     def get_info(self):
#         repr = super().get_info()
#         repr['videocard'] = self.videocard
#         repr['dispaly'] = self.display


# mac = Macbook('Apple', 'air', 1000, 2022, 13)
# print(mac.get_info())
# acer = Acer('Acer', 'Swift', 600, ' ge force 3040', 'xRGB 14')
# print(acer.get_info())



# class Employee:
#     bonus = 1.5

#     def __init__(self, first_name, last_name, salary):
#         self.name = f'{first_name} {last_name}'
#         self.salary = salary


#     def get_info(self):
#         return f'FIO: {self.name}, Salary: {self.salary}'

#     def give_increase(self):
#         self.salary = self.salary * self.bonus

#     def __str__(self) -> str:
#         return self.get_info()


# class Developer(Employee):
#     def __init__(self, first_name, last_name, salary, language):
#         super().__init__(first_name, last_name, salary)
#         self.prog_lang = language

#     def get_info(self):
#         info = super().get_info()
#         info += f', Prog language: {self.prog_lang}'
#         return info

#     def __str__(self) -> str:
#         return self.get_info()


# class Manager(Employee):
#     def __init__(self, first_name, last_name, salary, devs=[]):
#         super().__init__(first_name, last_name, salary)
#         self.devs = devs

#     def add_devs(self, developer):
#         self.devs.append(developer)

#     def show_devs(self):
#         return [x.get_info() for x in self.devs]
    
#     def __str__(self) -> str:
#         return self.get_info()



# dev1 = Developer('John', 'snow', 1500, 'Python')
# dev2 = Developer('Steve', 'Jobs', 3000, 'C++')
# dev3 = Developer('Larry', 'Page', 1500, 'JS')
# dev4 = Developer('Tirion', 'lanister', 1000, 'Python')

# man1= Manager('jamie', 'lanister', 2000)
# man2= Manager('dastan', 'Katana', 4000, [dev3,dev2])


# print(f'Manger {man1.get_info()}, has {man1.show_devs()}developers')
# print(f'Manger {man2.get_info()}, has {man2.show_devs()}developers')


# man1.add_devs(dev1)
# man1.add_devs(dev4)
# man2.add_devs(dev1)
# print('\nafter:')
# print(f'Manger {man1.get_info()}, has {man1.show_devs()}developers')
# print(f'Manger {man2.get_info()}, has {man2.show_devs()}developers')


# dev1.give_increase()
# man2.give_increase()

# print(dev1)
# print(man2)








    