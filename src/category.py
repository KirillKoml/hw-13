from abc import abstractmethod, ABC

from src.product import Product


class AbstractCategory(ABC):
    @abstractmethod
    def product(self):
        pass

    @abstractmethod
    def __len__(self):
        pass

    @abstractmethod
    def __str__(self):
        pass


class Category(AbstractCategory):
    all_quantity_category = 0
    all_quantity_unique_product = set()
    count_category = 0
    name: str
    description: str
    product: list

    def __init__(self, name, description, product, allowed_types):
        super().__init__()
        self.allowed_types = allowed_types
        self.name = name
        self.description = description
        self.__product = product
        Category.count_category += 1
        Category.all_quantity_unique_product.update(set(self.product))
        Category.all_quantity_category = len(Category.all_quantity_category)

    def product(self, products):
        self.__product.append(products)
        self.all_quantity_unique_product += 1

    def __len__(self):
        count_products = 0
        for product in self.__product:
            count_products += product.quantity
        return count_products

    def __str__(self):
        return f'{self.name}, количество продуктов:{len(self)} шт'

    def add_product(self, product: Product):
        try:
            if product.quantity == 0:
                raise ZeroError("Товар с нулевым количеством не может быть добавлен.")
            if not isinstance(product, self.allowed_types):
                raise TypeError(f"Можно добавлять только продукты следующих типов: {self.allowed_types}")
        except (ZeroError, TypeError) as e:
            print(f"Ошибка при добавлении товара: {e}")
        else:
            self.__product.append(product)
            self.all_quantity_unique_product += 1
            print("Товар успешно добавлен.")
        finally:
            print("Обработка добавления товара завершена.")

    @property
    def updated_product(self):
        updated_product = []
        for product in self.__product:
            updated_product.append(f'{product.name},{product.price} руб. Остаток: {product.quantity} шт.')
        return updated_product

    def average_price(self):
        try:
            total_price = sum(product.price for product in self.__product)
            average_price = total_price / len(self.__product)
            return average_price
        except ZeroDivisionError:
            print("В категории нет товаров.")
            return 0

    @updated_product.setter
    def updated_product(self, item):
        self.__product.append(item)


class ZeroError(Exception):

    def __init__(self, message="Товар с нулевым количеством не может быть добавлен."):
        self.message = message
        super().__init__(self.message)
