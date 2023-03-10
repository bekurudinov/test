# Работа с файлами 



# Каретка - Указатель - Курсор

# open(<путь до файла>)

# file = open('/home/sanzhar/desctop/py.26/files/files.py') #Абсольутный путь


# file = open('files.py')#Относительный путьъ
# ~ working -> Desctop/py.26/files/files.py
# py.26 ->files/files.py

# file = open('files.py')
# print(file.read())
# print(type(data))
# file.close()


 #Режимы работы с файлами
# 1.r/r+(read)
# 2.w/w+ (write)
# 3.a/a+(append)


# file = open('test.txt', 'r')
# print(file.read())
# file.close

# file = open('test.txt', 'r')
# data = file.readlines()
# print(data)
# print(len(data[0]))
# file.close()

# file = open('test.txt', 'r')
# print(file.readline())
# print('!!!!')
# print(file.read())
# file.close()


#контекстный менеджер
# with open('test.txt', 'r') as file:
#     data = file.read()
#     print(data)
#     print(file, 'inside')

# print(file, 'outside')


# with open('test.txt', 'r') as f:
#     data =f.read(5)
#     print(f.tell())
#     print(data)



# file.tell()-> возрашает индекст где находиться указатель(курсор)
# file.seek(index) -> перемешает  курсор на  индекст котроый вы передали



# with open('test.txt', 'r') as file:
    # print(file.readline())
    # file.seek(0)
    # print(file.readline())
    # file.seek(0)
    # a = file.read()
    # print(file.readline())
    # print(file.readlines(15))



# print(a)




# with open('test.txt', 'w') as file:
#     # file.write('Pervaya strochka!')
#     # file.write('\nHe is bastard of Ned Stark!\n')
#     # file.write('This is lession about files!')
#     # file.seek(0)
#     date =['Pervaya strochka!\n', 'He is basrard of Ned Stark!\n', 'This is lesson about files!']
#     file.writelines(date)



# with open ('test.txt', 'a+') as file:
#     file.write('\nJohn Snow is North King!')
#     file.write('\nYou  know  nothing Joohn Snow!')
#     file.seek(0)
#     print(file.read())



#===================================
# try:
#     from PIL import Image
# except ImportError:
#     import Image
# import pytesseract
# import re

# def get_imei_code(image):
#     string = pytesseract.image_to_string(image)
#     # print(string)
#     list_of_imei = re.findall(r'IMEI\d.\s\d+', string)
#     print(list_of_imei)

#     with open('imei_codes.txt', 'w') as file:
#         file.writelines(f'{x}\n' for x in list_of_imei)
#         # for x in list_of_imei:
#         #     file.write(f'{x}\n')
    

# image = 'imei.jpg'
# get_imei_code(image)


# with open("task1.txt", "r+") as file:
#     for line in file.readline(5):
#         print(line)


# with open("task1.txt") as file:
#     for line in file.readlines(9):
#         print(line)


def read_last(lines, file):
    if lines > 0:
        with open(file, encoding='utf-8') as text:
            file_lines = text.readlines()[-lines:]
        for line in file_lines:
            print(line.strip())
        else:
            print('Количество строк может быть только целым положительным')