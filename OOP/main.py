# import json
# class MyBook:

#     id = 0
#     country = 'Kyrgyzstan'

#     def __init__(self, title, author, price):
#         self.title = title
#         self.author = author
#         self.price = price

#     def create(self):

#         MyBook.id += 1

#         with open('db.json') as file:
#             list_ = json.load(file)

#         with open ('db.json', 'w') as file:
#             dict_ = {'id':self.id, 'title': self.title, 'author': self.author, 'price': self.price}
#             list_.append(dict_)
#             list_json = json.dumps(list_)
#             file.write(list_json)
    
#     @staticmethod
#     def read():
#         with open('db.json') as file:
#             list_json = file.read()
#             list_ = json.loads(list_json)
#             print(list_)

#     @staticmethod
#     def delete(id):
#         with open('db.json') as file:
#             list_ = json.load(file)
#         with open('db.json', 'w') as file:
#             list_2 = list_.copy()
#             for obj in list_2:
#                 if id == obj['id']:
#                     list_.remove(obj)
#                     list_json = json.dumps(list_)
#                     file.write(list_json)

#     @staticmethod
#     def update(id, pole, a):
#         with open('db.json') as file:
#             list_ = json.load(file)
#         with open('db.json', 'w') as file:
#             list_2 = list_.copy()
#             for obj in list_2:
#                 if id == obj['id']:
#                     obj[pole] = a
#                     res = json.dumps(list_2)
#                     file.write(res)


# book_1 = MyBook('Katana', 'Sultan', '100$')
# book_1.create()

# book_2 = MyBook('MyLife', 'Aigerim', '200$')
# book_2.create()

# MyBook.delete(1)
# MyBook.update(2, 'title', 'Anton')
# MyBook.read()




