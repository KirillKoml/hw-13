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

    def __repr__(self):
        return f'Product {self.name}, {self.description}, {self.__price}, {self.quantity}'

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
