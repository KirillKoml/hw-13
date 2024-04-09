from abc import abstractmethod, ABC


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

    def __init__(self, name, description, product):
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

    @property
    def updated_product(self):
        updated_product = []
        for product in self.__product:
            updated_product.append(f'{product.name},{product.price} руб. Остаток: {product.quantity} шт.')
        return updated_product

    @updated_product.setter
    def updated_product(self, item):
        self.__product.append(item)
