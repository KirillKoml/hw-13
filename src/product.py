class Product:
    name: str
    description: str
    price: float
    quantity: int

    def __init__(self, name, description, price, quantity):
        self.name = name
        self.description = description
        self.__price = float(price)
        self.quantity = quantity

    def __str__(self):
        return f'Продукт: {self.name}, {self.description}, {self.__price}, руб. Остаток: {self.quantity} шт'

    def __add__(self, other):
        return self.name + other.name * self.quantity

    @classmethod
    def add_new_product(cls, **kwargs):
        return cls(**kwargs)

    @property
    def price(self):
        return self.__price

    @price.setter
    def price(self, new_price):
        if new_price <= 0:
            print('Цена введена некоректно')
        else:
            self.__price = new_price
