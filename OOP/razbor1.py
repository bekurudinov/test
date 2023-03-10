# class Salary:
#     proc_nalog = 0.15

#     def __init__(self,sallary, stagh) -> None:
#         self.sallary = sallary
#         self.stagh = stagh

#     def get_sum(self):
#         res = (self.sallary*self.stagh)*(self.stagh * 12)
#         print(f'Сумма налогов составила {res} сомов за {self.stagh}лет')
        
# bek = Salary(177_000, 11)
# bek.get_sum()



# class Calc:
#     def add(self, a, b):
#         '''Function of sum'''
#         return a + b

#     def sqrt(self, num):
#         '''функция нахаждение корня'''
#         import math
#         res = math.sqrt(num)
#         return round(res, 2)

#     def percent(self, num, percent):
#         '''Функция нахождение процента от числа'''
#         return(num * percent)/100


#     def super_func(self, string):
#         '''Функиция выполняет вычисление в строке'''
#         '''1+1+2+3'''
#         try:
#             return eval(string)
#         except:
#             return 'Invalid Operation'


# calc = Calc()
# print(calc.add(4, 5))#9
# print(calc.sqrt(9))# 3
# print(calc.sqrt(2))#1.41
# print(calc.percent(255, 55))#140.25
# print(calc.super_func('(5-7)**2 - 10'))# -16
# print(calc.super_func(input('Vvedite operasiy: ')))

class CRUD:
    __products = []
    __id = 0

    def _get_id(self):
        self.__id += 1
        return self.__id

    def _get_product(self, id):
        for x in self.__products:
            if x ['id']==id: return x
        return False

    def create(self):
        print('CREATE of prodect!')
        title = input('Enter name of product: ')
        price = input('Enter price: ')
        self.__products.append({
            'id': self._get_id(),
            'title': title,
            'price': price
        })

    
    def list_of_products(self):
        print('All products: ')
        for x in self.__products:
            print(x['title'])

    def detail_product(self):
        print('Detail:')
        id = int(input('Введите ID  продукта: '))
        product = self._get_product(id)
        print(product if product else 'Нет такого продукта')
        # for x in self.__products:
        #     if x ['id']==id:
        #         product = x
        # return product if product else 'нет такого продукта'


    def update_product(self):
        print('Update:')
        id = int(input('Введите ID  продукта:'))
        product = self._get_product(id)
        if not product:
            print('Нет такого продукта')
            return None
        choice = input('Что изменить(title/price):')
        index = self.__products.index(product)
        self.__products[index][choice] = input('Введите новое знвачение: ')



    def delete_product(self):
        print('DELETE')
        id = int(input('Введите ID продукта :'))
        product = self._get_product(id)
        if not product:
            print('Нет такого продукта')
            return
        self.__products.remove(product)
        print('Удалено')


product = CRUD()
product.create()
product.create()
product.list_of_products()
# product.detail_product()
# product.detail_product()
# product.update_product()
# product.update_product()
# product.detail_product()
# print('===================\n')
# print(product._CRUD__product)
product.delete_product()
product.list_of_products()
