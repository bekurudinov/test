# Анатация свойств(@property(getter setter))


# class Person:
#     __name = "John"
#     __age = 22
#     __code = '+996'
#     __number = '770066776'
#     __full_number = __code + __number


#     @property
#     def name(self):
#         '''The name property(getter)'''
#         # print('geter!')
#         print(self.__name)

#     @name.setter
#     def name(self, value):
#         print('Setter')
#         if not isinstance(value, str):
#             print('Не валидные данные')
#             return
#         self.__name = value


#     @property
#     def age(self):
#         print(self.__age)

#     @age.setter
#     def age(self, value):
#         if not isinstance(value, int) or not 0<value<170:
#             print('Не валдидные данные')
#             return
#         self.__age = value


#     @property
#     def number(self):
#         name = input('Введите свое имя : ')
#         if self.__name != name:
#             print('Invalid name!!')
#             return
#         print(self.__full_number)
# obj = Person()
# obj.name
# obj.name = 'Bayel'
# obj.name
# obj.age
# obj.number


# class Circle:
#     def __init__(self, radius):
#         self.__radius = radius


#     @property
#     def radius(self):
#         return self.__radius


#     @radius.setter
#     def radius(self, value):
#         if not isinstance(value, (int, float)):
#             raise Exception('Invalid value, must be an int ot float object')
#         self.__radius = value

# circle = Circle(42)
# print(circle.radius)
# circle.radius = 15
# print(circle.radius)



class Game:
    __level = 0
    def __init__(self, name):
        self.name = name
    def play(self, hours):
        if hours > 2:
            self.__class__.__level += 1
      
    def get_level(self):
        return self.__class__.__level
game = Game('bek') 
print(game.get_level()) 
game.play(2)
print(game.get_level())
game.play(3)
print(game.get_level())
