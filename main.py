from string import ascii_letters
class Verify:
    letters_rus = 'абвгдеёжзийклмнопрстуфхцчшщъыьэюя .'
    letters_rus_upper = letters_rus.upper()
    letters = letters_rus + letters_rus_upper + ascii_letters
    code1 = 0

    def verify1(self, value):
        if type(value) != str:
            raise TypeError('Тип и продавец должны быть строками')
        elif len(value.strip(self.letters)) != 0:
            raise TypeError('Принямаются только буквы')
    def verify2(self, value):
        if type(value) != int and type(value) != float:
            raise TypeError('Вес, размер и цена должны быть числами')

class Descript(Verify):

    def __set_name__(self, owner, name):
        self.name = "__" + name

    def __get__(self, instance, owner):
        print(f'Возвращаю {self.name}')
        return instance.__dict__[self.name]

    def __set__(self, instance, value):
        self.verify1(value)
        print(f'Меняю значение {self.name} на {value}')
        instance.__dict__[self.name] = value

class Product(Verify):
    seller = Descript()
    n = 1

    def create_code(self):
        self.__code = Product.n
        Product.n += 1

    def __init__(self, weight, size, tip, seller, price):
        self.verify1(tip)
        self.verify2(weight)
        self.verify2(size)
        self.verify2(price)
        self.weight = weight
        self.size = size
        self.tip = tip
        self.seller = seller
        self.price = price
        self.create_code()

    def __str__(self):
        return f'Цена - {self.price} руб, тип - {self.tip}, вес - {self.weight} кг, размер - {self.size} см, продавец - {self.seller}'

    # __code доступен только для чтения, обращаться через code

    def get_code(self):
        return self.__code

    def set_code(self, value):
        self.__code = value

    code = property(get_code, set_code)
