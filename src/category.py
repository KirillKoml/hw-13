class Category:
    all_quantity_category = 0
    all_quantity_unique_product = set()
    name: str
    description: str
    product: list

    def __init__(self, name, description, product):
        self.name = name
        self.description = description
        self.__product = product
        self.all_quantity_category = 1
        Category.all_quantity_category += 1

    def __str__(self):
        return f'{self.name}, количество продуктов:{len(self)} шт'
        
    def product(self,products):
        self.__product.append(products)

    def __len__(self):
        return len(self.__product)



    @property
    def updated_product(self):
        updated_product = []
        for product in self.__product:
            updated_product.append(f'{product.name},{product.price} руб. Остаток: {product.quantity} шт.')
        return updated_product

    @updated_product.setter
    def updated_product(self, item):
        self.__product.append(item)
