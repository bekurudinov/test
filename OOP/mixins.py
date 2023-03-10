# Mixins


# микисны это классы которые будут использоваться для наследоавние, но от этих мисонов но от этих миксинов не создают объекты 
# Для чего:
# 1 вы хотите предостваить множество доп методов для класса
# 2 вы хотите использовать одну конкретенцию во мноежстве разных классов



# class Marhines:
#     def start_engine(self):
#         print('started engine!')

# class RadioMixin:
#      def play_radio(self):
#         print('music is playing')



# class Auto(RadioMixin, Marhines):
#     pass

# class Plane(Marhines):
#     pass

# class Train(RadioMixin, Marhines):
#     pass

# obj = Auto()
# obj2 = Plane()
# obj3 = Train()

# obj.start_engine()
# obj2.start_engine()
# obj3.start_engine()

# obj.play_radio()
# obj3.play_radio()



# class FlyMixin:
#     def fly(self):
#         print('я могу летать')

# class WalkMixin:
#     def walk(self):
#         print('я могу ходить')

# class SwimMixin:
#     def swim(self):
#         print('я могу плыть')

# class Human(WalkMixin, SwimMixin):
#     name = 'человек'

#     def talk(self):
#         print('я могу говорить')

# class Fish(SwimMixin):
#     name = 'рыба'

# class Exocoetidae(SwimMixin, FlyMixin):
#     name = 'летучая рыба'

# class Duck(SwimMixin, WalkMixin, FlyMixin):
#     name = 'утка'





# class Person:
#     def __init__(self, name, age):
#         self.name = name
#         self.age = age
    
#     def display(self):
#         return f"name:{self.name}, age:{self.age}"
    
# class Student(Person):
#     def __init__(self, name, age, faculty):
#         super().__init__(name, age)
#         self.faculty = faculty
    
#     def display_student(self):
#         get_info = super().display()
#         return get_info + f", faculty:{self.faculty}"
    
# obj_student = Student('Rick', 21, 'science')
# print(obj_student.display())
# print(obj_student.display_student())