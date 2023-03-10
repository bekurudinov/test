# Магические методы (dunder - duble umderscore)- методы у которых два нихжних подчеркиваниях в начале ив конце . Магия в том что мы иих не вызываем напрямую, а они вызываются в опердеенной момент либо они вызывается оперделенными оператоми или функициями


# res = 5 + 5 #__add__
# print(res)

# class A(int):
#     pass

# obj = A()
# print(dir(obj))


# магические методы котрые срабатывают при помоши оператора :

# __eq__(self, other)-> ==  : 5 == 7 seelf: 5 other: 7
# __ne__(self, other)-> !=
# __lt__(self, other)->  < ;  __le__ -> <=
#__gt__(self, other) ->  > ;  __ge__ ->  >=


# __sub__ ->(self, other)  __div__ -> /
# __mul__ -> *  __mod__ ->  %
# __floordiv__ -> // __add__ -> +
#__pow__ -> **


# class MyClass:
#     def __init__(self, string):
#         self.string = string


#     def __add__(self, other):
#         print('add сработал')
#         print(self, '!!!')
#         print(other, '****')
#         res = self.string + other.string
#         return MyClass(res)
     
#     def __str__(self) -> str:
#         return self.string

# obj1 = MyClass('John')
# obj2 = MyClass('Bek')
# obj3 = MyClass('Baiel') 
# # print(obj1 + obj2 + obj3)
# res = (obj1 + obj2 + obj3)
# print(res)
# print(res.string)


# class Word(str):
#     def __init__(self, word):
#         self.word =word

#     def __gt__(self, other: str) -> bool:
#         print(' gt  сработал')
#         print(self, '!!!')
#         print(other, '****')
#         return len(self) > len(other)


# obj1 = Word('Johnb   ')
# obj2 = Word('Hello world')
# print(obj1 > obj2)

'''========================'''
# конструктор -> __new__(cls)
# инициализатор -> __init__(self)
# вызывается когда создаем объект


# class Conventer(float):
#     def __new__(cls, __x):
#         print(' new сработал')
#         print(cls, '!!!')
#         print(__x, 'xxx')
#         if __x < 50:
#             raise ValueError('x  меньше 50!')
#         return super().__new__(cls, __x)

#     def __init__(self, x):
#         print('init сработал')
#         print(self, '!!!')
#         self.number = x

# obj = Conventer(51)
# print(obj)

    


# class Word(str):

#     def __new__(cls, word):
#         word = word.replace(' ', '')
#         return super().__new__(cls, word)

#     def __init__(self, word):
#         self.word =word

#     def __gt__(self, other: str) -> bool:
#         print(' gt  сработал')
#         print(self, '!!!')
#         print(other, '****')
#         return len(self) > len(other)


# obj1 = Word('John   ')
# obj2 = Word('Hello world')
# print(obj1 > obj2)


'''===================='''
# дандер метод стокового отоброжение объектов

# __str__ -> для отоброжение строки которую будет видеть пользователи

# __repr__ -> строковую информацию о тттом как создать объект


# __len__ -> len(obj)
# __repr__ ->repr(obj)

# evel('6 + 6') -> 6 + 6


# class Base:
#     def __init__(self, string):
#         self.string = string

#     def __str__(self):
#         return f'объект: {self.string}'

#     def __repr__(self):
#         return f'Base("string")'

#     def __len__(self):
#         return 5

# user = Base('Hello John')
# print(user)
# print(repr(user))
# obj1 = eval(repr(user)) #Base("string")
# print(obj1)




# class Person:
#     def __init__(self, attrs: dict):
#         # self.name = attrs['name']
#         #self.a = 5 == settatr(self, 'a' 5)
#         for key, value in attrs.items():
#             setattr(self, key, value)



# alice = Person({'name': 'alice Rose', 'income':180000, 'eyes': 'btown'})
# john = Person({'email': 'johnsnow@gmail.com', 'last_name': 'snow'})
# print(f'{alice.name} --{alice.income}-- {alice.eyes}')
# print(f'{john.email} -- {john.last_name}')

# class MyList(list):
#     def __init__(self, ls):
#         self.ls = ls
#     def __getitem__(self, index):
#         print(self.ls[index - 1])

# x = MyList([1,2,4,5])
# x[1]
# # x[3]
# # x[2]


# __iter__ - вызывается когда мы итерируем объект


# class A:
#     def __init__(self, word):
#         self.word = word
#     def __iter__(self):
#         for i in self.word:
#             # print('iter method')
#             yield i

# x = A('Humnan')
# for i in x:
#     print(i)

# a = range(1, 10)
# print(a)
# for x in a:
#     print(x)

# def generator(num):
#     for i in range(num):
#         yield i

# a =  generator(5)
# for x in a:
#     print(x)

'''-----'''
# class User:
#     def __init__(self, name):
#         self.name = name

#     def __call__(self):
#         print(f' user objerct: {self.name}')
# user1 = User('john Snow')
# user1()


'''Task 1'''
# class Account:
#     def __init__(self, name, balance, city):
#         self.name = name
#         self.balance = balance
#         self.city = city
#         print(f'Счет создан')
#     def __str__(self):
#         return f'Hello {self.name} {self.balance} {self.city}'
#     def __repr__(self):
#         return f'{self.name} {self.balance}'
#     def __del__(self):
#         print(f'Пока')

# obj_account = Account("Rick", 2013, 'Bishkek')  
# print(obj_account)  
# print(repr(obj_account))
'''task 2'''
# class MyNumber(int):
#     def __init__(self, value):
#         self.value = value
#     def __add__(self, other):
#         return f'Это сложение и результат равен: {self.value + other}'
#     def __sub__(self, other):
#         return f'Это вычитание и результат равен: {self.value - other}'
#     def __mul__(self, other):
#         return f'Это умножение и результат равен: {self.value * other}'
#     def __truediv__(self, other):
#         return f'Это деление и результат равен: {self.value / other}'
# obj_int = MyNumber(5)  
# print(obj_int + 5)  
# print(obj_int - 5)  
# print(obj_int * 5)  
# print(obj_int / 5)  

'''task3'''
# class MyList(list):
#     def __init__(self , list_):
#         self.list_ = list_
#     def __getitem__(self, index):
#         return(self.list_[index -1])
# obj_list = MyList([1,2,3,4,5])  
# print(obj_list[1]) 


'''task 4j'''
# class Student:
#     def __init__(self, name, class_name, ball) -> None:
#         self.name = name
#         self.class_name = class_name
#         self.ball = ball
#     def srednee_znach(self):
#         srednee = sum(self.ball.values())/len(self.ball)
#         return srednee

#     def __gt__(self, other):
#         return f'> {self.srednee_znach() > other.srednee_znach()}'
#     def __lt__(self, other):
#         return f'< {self.srednee_znach() < other.srednee_znach()}'
#     def __ge__(self,other):
#         return f'>= {self.srednee_znach() >= other.srednee_znach()}'
#     def __le__(self, other):
#         return f'<= {self.srednee_znach() <= other.srednee_znach()}'

# obj_student1 = Student('a', 'A', {'math': 100, 'history': 50, 'literature': 88})  
# obj_student2 = Student('b', 'Aa', {'math': 100, 'history': 50, 'literature': 88})  
# print(obj_student1 > obj_student2)  
# print(obj_student1 < obj_student2)  
# print(obj_student1 >= obj_student2)  
# print(obj_student1 <= obj_student2)



# class Word(str):
#     def __init__(self, word):
#         self.word = word
#     def __gt__(self, other: str) -> bool:
#         return len(self) > len(other)
#     def __lt__(self, other):
#         return len(self) < len(other)
#     def __ge__(self, other):
#         return len(self) >= len(other)
#     def __le__(self, other):
#         return len(self) <= len(other)

#     def __new__(cls, word):
#         word = word.replace(' ', '')
#         return super().__new__(cls, word)



# word1 = Word('H  e  l  l  o')  
# word2 = Word('world!')  
# print(word1 > word2)  
# print(word1 < word2)  
# print(word1 >= word2)  
# print(word1 <= word2)


# class Word:
#     def __init__(self, word_text):
#         self.word_text = word_text


#     def __new__(cls, word_text):
#         # Удаляем пробелы и пустые строки
#         word_text = ' '.join(word_text.split())
#         if not word_text:
#             return None
#         return super(Word, cls).__new__(cls)

#     def __lt__(self, other):
#         return len(self.word_text) > len(other.word_text)

#     def __gt__(self, other):
#         return len(self.word_text) < len(other.word_text)

#     def __le__(self, other):
#         return len(self.word_text) >= len(other.word_text)

#     def __ge__(self, other):
#         return len(self.word_text) <= len(other.word_text)

# word1 = Word('H  e  l  l  o')
# word2 = Word('world!')
# print(word1 > word2)
# print(word1 < word2)
# print(word1 >= word2)
# print(word1 <= word2)
'''Task 6'''
# class Kopilka:
#     __total = 0
#     __coins = []
#     def add_moneta(self, moneta):
#         self.__total += moneta
#         self.__coins.append (moneta)

#     def __len__(self):
#         return len(self.__coins)
#     def __getitem__(self, index):
#         return self.__coins[index]
# obj = Kopilka() 
# obj.add_moneta(25) 
# obj.add_moneta(30)

# print(len(obj))
# for i in obj: 
#     print(i) 
        
# class Kopilka: 
#     def __init__(self): 
#         self.__total = 0 
#         self.__coins = [] 
#     def add_moneta(self,moneta): 
#         self.__total += moneta 
#         self.__coins.append(moneta) 
#     def __len__(self): 
#         return len(self.__coins) 
#     def __getitem__(self,index): 
#         return self.__coins[index] 
# obj = Kopilka() 
# obj.add_moneta(25) 
# obj.add_moneta(30) 
# print(len(obj)) 
# for i in obj: 
#     print(i)

'''task 7'''

# class Anagram(str):
#     def __init__(self, value):
#         self.value = value

#     def eq(self, other):
#         list1 = list(map(lambda x: x, self.value))
#         list1.sort()
#         list2 = list(map(lambda x: x, other.value))
#         list2.sort()
#         return list1 == list2

#     def __mul__(self, other):
#         return self.value[::-1] * other
    

    
# word1 = Anagram('hello') 
# word2 = Anagram('olleh') 
# print(word1 == word2)
# print(word1 * 3)

    