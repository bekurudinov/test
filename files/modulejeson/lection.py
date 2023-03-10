#Json -- javaScript Object noеion
#Единый формат хранаение и передачи  данных между приложениями сайтами сервисами и языками програмирование через сеть интернет 
#<failname>.json #файл в  формате JSON


# {
#     "id": 1,
#     "author": "Ed Sheeran"
#     "title": "Perfect"
#     "year": 2015
#     "hit": true,
#     "feat": null
# }#---- JSON
# #наша задача научиться переволить данные JSON v Python
# dictionary


# !!!
# JS object == {key: value}
# PY dict == {key:value}
# JSON == {key: value}


# Процессы Серифлизации и ДЕсериализации данных

# Серифлизация (Запсиь данных в JSON)- Это перевод из Python обьектов в JSON формат   


# Json.dump -> метод записывет патйтон данные в файл  в формате JSON паралеьные сделав серализации

# Json.dumps-> метод записывет патйтон данные в строку  в формате JSON 

# Десериализация (Чтение даных из JSON)- это процесс перевода из Jsona v PY dict



# json.load-> метод котрый счистывает файл в формате Json и переводит его в PY object


# json.loads-> метод котрый счистывает текст формате Json и переводит его в PY object


#===============================================


#Процесс сериализации

# import json


# dict_ ={
#     'name': 'JOhn',
#     'last_name': 'Smow',
#     'status': True,
#     'age': 24,
#     'wife': False,
#     'children': None
# }

# print(dict_)
# print(type(dict_))

# json_text = json.dumps(dict_)
# print('------------------')
# print(json_text)
# print(type(json_text))



# import json


# dict_ ={
#     'name': 'JOhn',
#     'last_name': 'Smow',
#     'status': True,
#     'age': 24,
#     'wife': False,
#     'children': None
# }

# print(dict_)
# with open('new.json', 'w') as file:
#     json.dump(dict_, file)

# with open('new.json', 'r') as file:
#     data = file.read()
#     print(data)



#======================================


# процесс десериализации 

# import json

# with open('new.json', 'r') as file:
#     json_data = file.read()


# print(json_data)
# print(type(json_data))

# dict_ = json.loads(json_data)
# print(dict_, type(dict_))



# import json

# with open('new.json') as file:
#     dict_ = json.load(file)
#     print(dict_)
#     print(type(dict_))



# #------------------------------------
# https://34.12.121.10/users/ - запрос на получение всех юзеров

# from urllib.request import urlopen
# import json

# url = 'https://randomuser.me/api/'
# json_data = urlopen(url)


# print(json_data)
# # print(dir(json_data))
# # print(json_data.read())


# dict_ = json.load(json_data)#.loads(json_data.read())
# print(dict_)
# print(type(dict_))