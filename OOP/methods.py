# Сушествует 3  вида методов
# class methods, instance methods, static methods


# instance methods - обычные методы котроые принимают первым аргументы self(ссылка  на обеъект )Нужны для того чтобы внутри мметода мы могли работать с атрибутами объекта

# class A:
#     def instance_method(self):
#         print('метод обеъкта')
#         print('первый аргумент:', self)

# obj_a = A()
# obj_a.instance_method(5)# если вызывем у объекта то self передается автоматический
# A.instance_method(obj_a, 5)# если вызываем у класса  то self , нужно передать обьект вручную

'''================='''

# class methods -  методы котроые принимают первым аргументом cls(ссылка на класс).Нужны они для создания объектов или изменения аттрибутов класса. Для того чтобы создыать класс меттод нужно восрользоваться декаратором  @classmethod



# class B:
#     @classmethod
#     def class_method(cls, a):
#         print('Класс метод')
#         print('первый аргумент:', cls)


# obj_b = B()
# obj_b.class_method(5)
# B.class_method(5)



# class C:
#     counter = 0
#     def __init__(self) -> None:
#         self._inc_counter()

#     @classmethod
#     def _inc_counter(cls):
#         cls.counter += 1


# obj1 = C() #1
# obj2 = C()#2
# obj3 = C()#3
# print(C.counter)

# class Pizza:
#     def __init__(self, radius, *ingredients) -> None:
#         self.r = radius
#         self.ingredients = ingredients

#     def cook(self):
#         print('готовится пицаа размером  {self.r * 2} cm')

#     @classmethod
#     def four_chees(cls, r):
#         pizza = cls(r, 'моцерело' 'чедер', 'голандский', 'брынза' )
#         return pizza


# pizza1 = Pizza(17, 'пеперони', 'моцерело', 'грибы')
# # pizza2 = Pizza(15, 'моцерело' 'чедер', 'голандский', 'брынза')
# # pizza2 = Pizza(20, 'моцерело' 'чедер', 'голандский', 'брынза')
# pizza2 = Pizza.four_chees(15)
# pizza3 = Pizza.four_chees(20)




# class Person:
#     surname = 'Stark'

#     def __init__(self, name, age) -> None:
#         self.name = name
#         self.age = age

#     @classmethod
#     def from_birth_date(cls, name, date_birth):
#         from datetime import date
#         age = date.today().year - date_birth
#         return cls(name, age)

# obj = Person('John', 24)
# print(obj.name, obj.surname, obj.age)
# obj2 = Person.from_birth_date('Sansa', 1961)
# print(obj2.name, obj2.surname, obj2.age)


'''
STATIC methods - это функции внутри класса, которые не взаимодействуют ни с классом, ни с объектом. Находятся они внутри класса, потому что их используют только внутри класса, так как вне они бесполезны. 
'''

# class C:
#     @staticmethod
#     def static_method():
#         print('статический метод!!!')


# obj = C()
# obj.static_method()
# C.static_method()



class Cylinder:
    def __init__(self, diameter, height)-> None:
        self.di = diameter
        self.h = height
        self.area = self.get_area(self.di, self.h)

    @staticmethod
    def get_area(diameter, h):
        from math import pi
        circle = pi * (diameter / 2) ** 2
        side = pi *h *diameter
        area = circle * 2 + side
        return round(area, 2)
obj = Cylinder(10, 7)
print(f'Area: {obj.area}')

obj1 = Cylinder(4, 10)
print(f'Area {obj1.area}')





