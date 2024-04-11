from abc import abstractmethod, ABC


class Mixin:
    def __init__(self, *args):
        print(repr(self))

    def __repr__(self):
        object_attributes = ''
        for k, v in self.__dict__.items():
            object_attributes += f'{k}: {v},'
        return f"создан объект со свойствами {object_attributes})"

class AbstractProduct(ABC):
    @abstractmethod
    def __repr__(self):
        pass

    @abstractmethod
    def __str__(self):
        pass

    @abstractmethod
    def add_new_product(cls, **kwargs):
        pass


class Product(Mixin, AbstractProduct):
    name: str
    description: str
    price: float
    quantity: int

    def __init__(self, name, description, price, quantity, colour, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.name = name
        self.description = description
        self.__price = float(price)
        self.quantity = quantity
        self.colour = colour

    def __len__(self):
        return self.quantity

    def __repr__(self):
        pass

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


class Smartphone(Product):
    def __init__(self, name, description, price, quantity, ram, model, memory, colour):
        super().__init__(name, description, price, quantity)
        self.ram = ram
        self.model = model
        self.memory = memory
        self.colour = colour


class LawnGrass(Product):
    def __init__(self, name, description, price, quantity, manufacturer, growth_period, colour):
        super().__init__(name, description, price, quantity)
        self.manufacturer = manufacturer
        self.growth_period = growth_period
        self.colour = colour
