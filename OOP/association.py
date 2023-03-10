'''
Ассоцация делится на 2 вида 
Ассоцация озночает что внутри объекта будет сушествовать другой в качестве аттрибута
1) Композиция -сильная свзяь
2) Агрегация - слабая сявзь

'''

''' Композиция - Это когда стена не  сушуствует одтельно от комнаты. Она создается при создании комнаты и полностью урправления классом комнаты'''
# class Wall:

#     def __init__(self, diretion):
#         self.type = diretion

#     def __str__(self):
#         return f'{self.type} wall'
#     def info(self):
#         print('White wall')

# class Room:
#     def __init__(self):
#         self.west_wall = Wall('west')
#         self.east_wall = Wall('east')
#         self.south_wall = Wall('south')
#         self.north_wall = Wall('north')


# room = Room()
# print(room.west_wall)
# print(room.north_wall)
# print(room.north_wall.type)
# room.north_wall.info()


'''Агрегация - Это когда экзмепляр двигателя двигается создается где то в другом вмсете, и передаедтся в кдасс Авто в качестве параметре'''
# class Engine:
#     country = 'Germany'
#     def __init__(self, power):
#         self.power = power

#     def __str__(self):
#         return f'Engine: {self.power}'

# class Car:
#     model = 'Audi'
#     country = 'Germany'

#     def __init__(self, type, engine):
#         self.type = type
#         self.engine = engine

#     def __str__(self):
#         return f'{self.model} {self.type} -> {self.engine} {self.engine.country}'


# engine  = Engine(500)
# car = Car('A8', engine)
# print(car)


'''================='''
# class Battery:
#     _power = 100

#     def power(self):
#         if self._power < 100:
#             self._power = 100

# class Iphone:
#     def __init__(self, color) -> None:
#         self.color = color
#         self.battery = Battery()
#         #когда мы зоздаем объект внутри это -композиция

# class Nokia:
#     def __init__(self, color: str, battery = Battery) -> None:
#         self.color = color
#         self.battery = Battery()
#         #когда принимаем в качестве параметра это - аргегация

# iphone = Iphone('gray')
# del iphone
# # при удалении iphine вместе с ним удаляется и battery

# battery = Battery()
# nokia = Nokia('black', battery)
# del nokia
# # при удалении нокии батерейка остается
# nokia2 = Nokia('white', battery)