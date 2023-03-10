# Инкапсулицая


# 1 Связь данных с методами которые должны управлять этими аттрибутами
# 2 Механизм языка который позволяет ограничить доступ к оперделенымм компонентам класса

# Инкапсуляция  как связь

# class Phone:
#     number = '+996700700700'

#     def print_number(self):
#         print(f'Мой номер: {self.number}')

# my_phone = Phone()
# my_phone.print_number() #Мой номер: +996700700700

# Инкапсуляция как управление доступом 
# 3 уровня доступа в питон
#             1. Публичный(public)- number, print_number
#             2. Зашишенный(_proctected, parent/child)- _number
#             3. Приватный(__private, только текушим)-__number


# class Car:
#     _country = 'Germany'

#     def __init__(self):
#         self.marka = 'Mersedez- Benz'#публичный
#         self._model = 'w140'#зашишеный
#         self.__motor = 'ABC'#приватный



# obj = Car()
# print(obj.marka)
# print(obj._country)
# print(obj._model)
# print(obj._Car__motor)

'''---------------------------------------------------------------------'''
# class Phone:
#     username = 'John Snow'
#     _caller = 'Jamie Lanister'
#     __count_of_calls = 15


#     def call(self):
#         print(f'{self._caller} звонит!')


#     def __increment_of_calls(self):
#         self.__count_of_calls += 1

#     def turn_on(self):
#         print(f'{self.username} взял  трубку')
#         self.__increment_of_calls()

#     def get_count(self):
#         print(self.__count_of_calls)

    



# obj = Phone()
# obj.get_count()
# obj.call()
# obj.turn_on()
# obj.get_count()

'''--------------------------------------------'''

#getter & setter

# Они используются для получение и установки значений в зашишенные аттрибуты чтобы избежать прямого доступа к зашишенному аттрибутты и еще с помошью сеттеров и геттеров можно добавлять логику проверки при получении данных


# class Person:
#     def __init__(self, name):
#         self.name = name
#         self.age = 0


#     def display_info(self):
#         print(f'My name is {self.name}, I\'m {self.age} years old!')


# john = Person('John')
# john.display_info()


# class Person:
#     def __init__(self, name):
#         self.__name = name
#         self.__age = 0


#     def display_info(self):
#         print(f'My name is {self.__name}, I\'m {self.__age} years old!')


#     #getter - получить
#     def get_name(self): return self.__name

#     #setter
#     def set_name(self, name):
#         if not isinstance(name, str):
#             print('Invalid value!')

#         else:
#             self.__name = name


#     def get_age(self): return self.__age

#     def set_age(self, age):
#         if not isinstance(age, int) or not 0 <= age <150:
#             print('Invalid value for age!')

#         else:
#             self.__age = age

# john = Person('John')
# john.display_info()
# john.set_name(None)
# john.set_age(-18)
# john.display_info()
# john.set_name('Jamie')
# john.set_age(24)
# john.display_info()

# class Russia():
#     __name = 'Russian Federation'
#     __population = 0


#     def get_population(self): return self.__population

#     def set_population(self, num):
#         if not isinstance(num, int) or num < 0:
#             print('Invalid value fo population!')
#         else:
#             self.__population  = num

#     def get_name(self): return self.__name

#     def display_info(self):
#         print(f'Population of {self.get_name()}: {self.get_population()}')


# obj = Russia()
# obj.set_population(143_000_000)
# obj.display_info()



'''TASK1'''
# class A: 
#     def public(self): 
#         return 'Public method' 
#     def _protected(self): 
#         return 'Protected method' 
#     def __private(self): 
#         return 'Private method' 
#     def print_protected(self): 
#         self._protected() 
#     def print_private(self): 
#         self.__private() 
        
# obj1 = A() 
# print(obj1.public()) 
# print(obj1.print_protected()) 
# print(obj1.print_private())
'''TASK2'''
# class A:
#     def method1(self):
#         return f'Hello World'
# class B(A):
#     pass
# b1 = B()
# print(b1.method1())
'''TASK4'''
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


"""task6"""
# class Person: 
#     def __init__(self, name, phone_number, card_number) -> None: 
#         self.name = name 
#         self._phone_number = phone_number 
#         self.__card_number = card_number 
#     @property 
#     def number(self): 
#         return self.__card_number 
# john = Person("John", "+996 557 55 17 57", "9999 9999 9999 9999") 
# print(john.name) 
# print(john._phone_number) 
# print(john.number)



# class Person: 
#     name = "John" 
#     _phone_number = "+996 557 55 17 57" 
#     __card_number = "9999 9999 9999 9999" 
#     def get_number(self): 
#         return self.__card_number 
#     def set_number(self): 
#         self.__card_number = None
#         return self.__card_number 
# john = Person() 
# john.name = None 
# john._phone_number = None 
# print(john.name) 
# print(john._phone_number) 
# print(john.set_number())


# class Person: 
#     def __init__(self, name, phone_number, card_number) -> None: 
#         self.name = name 
#         self._phone_number = phone_number 
#         self.__card_number = card_number 


#     @property
#     def validate_name(self):
#         if len(name) < 2:
#             retur


# class Person:
#     def __init__(self, name, phone_number, card_number):
#         self.name = self.validate_name(name)
#         self._phone_number = phone_number
#         self.__card_number = card_number

#     def validate_name(self, name):
#         if len(name) < 2:
#             return "John"
#         else:
#             return name.capitalize()

# sam = Person("SAM", "+996 557 55 17 57", "9999 9999 9999 9999")
# print("Name:", sam.name)
# print("Phone Number:", sam._phone_number)
# print("Card Number:", sam.__card_number)





# class Person:
#     def __init__(self, name, phone_number, card_number):
#         self.name = self.__validate_name(name)
#         self._phone_number = phone_number
#         self.__card_number = card_number
        
#     def __validate_name(self, name):
#         if len(name) < 2:
#             return "John"
#         else:
#             return name.title()
        
#     def get_card_number(self):
#         return self.__card_number
    
#     def set_card_number(self, card_number):
#         self.__card_number = card_number
        
# sam = Person("SAM", "+996 557 55 17 57", "9999 9999 9999 9999")
# print(sam.name)
# print(sam._phone_number)
# print(sam.get_card_number())

# class Person:
#     def __init__(self, name, phone_number, card_number) -> None:
#         self.name = self.__validate_name(name)
#         self._phone_number = phone_number
#         self.__card_number = card_number

#     def __validate_name(self, name):
#         if len(name) < 2:
#             return 'John'
#         else:
#             return name.title()
            
#     def get_number(self):
#         return self.__card_number

# sam = Person("SAM", "+996 557 55 17 57", "9999 9999 9999 9999")
# print(f'{sam.name}\n{sam._phone_number}\n{sam.get_number()}')


# from datetime import datetime

# class CreateMixin:
#     def create(self, todo, key):
#         if key in self.todos:
#             return "Задача под таким ключом уже существует"
#         else:
#             self.todos[key] = todo

# class DeleteMixin:
#     def delete(self, key):
#         if key in self.todos:
#             task_name = self.todos.pop(key)
#             return f"удалили {task_name}"
#         else:
#             return "Задачи с таким ключом не существует"

# class UpdateMixin:
#     def update(self, key, new_value):
#         if key in self.todos:
#             self.todos[key] = new_value
#         else:
#             return "Задачи с таким ключом не существует"

# class ReadMixin:
#     def read(self):
#         return sorted(self.todos.items())

# class ToDo(CreateMixin, DeleteMixin, UpdateMixin, ReadMixin):
#     todos = {}

#     def set_deadline(self, deadline):
#         deadline_date = datetime.strptime(deadline, '%d/%m/%Y')
#         today_date = datetime.today()
#         days_left = (deadline_date - today_date).days
#         return days_left
# todo = ToDo()

# # добавление задачи
# todo.create("посмотреть фильм", "1")
# todo.create("почитать книгу", "2")
# print(todo.todos) # {'1': 'посмотреть фильм', '2': 'почитать книгу'}

# # обновление задачи
# todo.update("2", "почитать статью")
# print(todo.todos) # {'1': 'посмотреть фильм', '2': 'почитать статью'}

# # удаление задачи
# print(todo.delete("1")) # удалили посмотреть фильм
# print(todo.todos) # {'2': 'почитать статью'}

# # чтение списка задач
# print(todo.read()) # [('2', 'почитать статью')]

# # расчет оставшегося времени до дедлайна
# print(todo.set_deadline("31/12/2022")) # 322



# class CreateMixin:
#     def create(self, key, todo):
#         if key in self.todos.keys():
#             return 'Задача под таким ключом уже существует'
#         self.todos[key] = todo
#         return self.todos
            
# class DeleteMixin:
#     def delete(self, key):
#         delete_ = self.todos.pop(key, 'нет такого ключа')
#         if 'нет такого ключа' == delete_:
#             return delete_
#         return delete_
            
# class UpdateMixin:
#     def update(self, key, new_value):
#         self.todos[key] = new_value
#         return self.todos
        
# class ReadMixin:
#     def read(self):
#         res = [x for x in self.todos.items()]
#         return sorted(res)
    
# class ToDo(CreateMixin, DeleteMixin, UpdateMixin, ReadMixin):
#     todos = {}
#     def set_deadline(self, deadline):
#         import datetime
#         time_ = datetime.datetime.now().strftime('%d/%m/%Y')
#         deadline = deadline.split('/')
#         time_ = time_.split('/')
#         deadline = list(map(int, deadline))
#         time_ = list(map(int, time_))
#         time_ = sum((time_[0], time_[1]*30, time_[2]*365))
#         deadline = datetime.date(deadline[2], deadline[1], deadline[0])
#         time_ = datetime.date.today()
#         return (deadline - time_).days
    
# task = ToDo() 
# print(task.set_deadline('31/12/2022'))
# print(task.create(1, 'todo'))
# print(task.delete(3))
# print(task.update(1, 'todo'))
# print(task.read())
# print(task.create(1, 'Do housework'))
# print(task.create(1, 'Do housework'))
# print(task.create(2, 'Go for a walk'))
# print(task.update(1, 'Do homework'))
# print(task.delete(2))
# print(task.read())
# print(task.set_deadline('31/12/2021'))



# class ExtensionMixin:
#     def add_extension(self, extension_name):
#         self.extensions.append(extension_name)
#         return f'Добавлено новое расширение {extension_name} для игры {self.name}.' 

#     def remove_extension(self, extension_name):
#         if extension_name in self.extensions:
#             self.extensions.remove(extension_name)
#             return f'{extension_name} был отключен от {self.name}'
        
#         else:
#             return 'Такого расширения нет в списке.'

# class Game(ExtensionMixin):
#     def __init__(self, game_type, name):
#         self.type = game_type
#         self.name = name
#         self.extensions = []
    
#     def get_description(self, description):
#         return f"{self.name} это {description}"
    
#     def get_extensions(self):
#         if len(self.extensions) == 0:
#             return "Нет подключенных расширений"
#         else:
#             return self.extensions





# game = Game('CS_GO', 'Minencraft')

# print(game.get_description('инди-игра в жанре песочницы с элементами выживания и открытым миром'))
# print(game.add_extension('Multiverse-Core'))
# print(game.add_extension('Multiverse-Core1'))
# game.extensions
# print(game.get_extensions())
# print(game.remove_extension('Multiverse-Core'))
# print(game.get_extensions())

# class Person:
#     def __init__(self, name, phone_number, card_number) -> None:
#         self.name = self.__validate_name(name)
#         self._phone_number = phone_number
#         self.__card_number = card_number

#     def __validate_name(self, name):
#         if len(name) < 2:
#             return 'John'
#         else:
#             return name.title()
            
#     def get_number(self):
#         return self.__card_number

# sam = Person("SAM", "+996 557 55 17 57", "9999 9999 9999 9999")
# print(f'{sam.name}\n{sam._phone_number}\n{sam.get_number()}')

# class Person:
#     def __init__(self, name, phone_number, card_number):
#         self.name = name
#         self._validate_phone_number = phone_number
#         self.__validate_phone_number = card_number
#     def __validate_phone_number(self):
#         if 

# class Person: 
#     def __init__(self, name, phone_number, card_number): 
#         self.name = name 
#         self._phone_number = self._validate_phone_number(phone_number) 
#         self.__card_number = self.__validate_card_number(card_number) 
        
#     def _validate_phone_number(self, phone_number): 
#         if isinstance(phone_number, int) and str(phone_number).startswith('996'): 
#             return phone_number 
#             return None 
#     def __validate_card_number(self, card_number): 
#         if isinstance(card_number, int) and len(str(card_number)) == 16: 
#             return card_number 
#             return None 
# tolik = Person('Sam', 996557551757, 9999999999999999) 
# print(tolik.name) 
# print(tolik._phone_number) 
# print(tolik._Person__card_number)


# class Game:
#     __level = 0

#     def __init__(self, name):
#         self.name = self.__validate_name(name)

#     def set_level(self, level):
#         if self.name == 'Tolik':
#             self.__level = level
#         else: print(f"{self.name} ты не Tolik!")
    
#     def __validate_name(self, name):
#         return name.title()

# game = Game('Raychel')
# game.set_level(5)
# print(game._Game__level)
# game2 = Game('TOLIK')
# game2.set_level(5)
# print(game2._Game__level)


