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
        Category.all_quantity_unique_product.add(name)
        
    def __len__(self):
        return self.quantity

    def __str__(self):
        return f'{self.name}, {self.__price}, руб. Остаток: {self.quantity} шт'

    def __add__(self, other):
        if isinstance(other, type(self)):
            total_price_self = self.price * self.quantity
            total_price_other = other.price * other.quantity
            total_price = total_price_self + total_price_other
            return total_price
        else:
            raise TypeError("Нельзя складывать продукты разных типов или объекты других классов.")

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
