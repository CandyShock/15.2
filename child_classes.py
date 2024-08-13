from Mixins import MixinTest
from parent_classes import Product, Category


class Smartfone(Product, MixinTest):
    product_list = []
    """атрибут на уровне класса для хранине всех продуктов"""

    def __init__(self, name, desc, price, count, gpu, model, ram, color):
        super().__init__(name, desc, price, count)
        self.gpu = gpu
        self.model = model
        self.ram = ram
        self.color = color

    @classmethod
    def create_product(cls, product):
        "создает экземпляр класса"
        name, desc, price, count, gpu, model, ram, color = product.split("-")
        new_product = cls(name, desc, price, count, gpu, model, ram, color)
        return new_product

    def print_name(self):
        """метод абстрактного класса"""
        print(self.name)

    def __len__(self):
        return len(self.product_list)

    def __add__(self, other):
        """складываются только объекты одного и того же класса"""
        if type(self) == type(other):
            return super().__add__(other)
        raise TypeError

    def ad_prod(self, other):
        """если добавляемый экземпляр не является наследником или родителем TypeError"""
        if isinstance(other, Product):
            self.product_list.append(other)
            return f'Добавлено'
        raise TypeError


class Gras(Product, MixinTest):
    product_list = []
    """атрибут на уровне класса для хранине всех продуктов"""

    def __init__(self, name, desc, price, count, Country, deadline, color):
        super().__init__(name, desc, price, count)
        self.Country = Country
        self.deadline = deadline
        self.color = color

    @classmethod
    def create_product(cls, product):
        "создает экземпляр класса и выводит часть его атрибутов"
        name, desc, price, count, Country, deadline, color = product.split("-")
        new_product = cls(name, desc, price, count, Country, deadline, color)
        return new_product

    def print_name(self):
        """метод абстрактного класса"""
        print(self.name)

    def __len__(self):
        return len(self.product_list)

    def __add__(self, other):
        """складываются только объекты одного и того же класса"""
        if type(self) == type(other):
            return super().__add__(other)
        raise TypeError

    def ad_prod(self, other):
        """если добавляемый экземпляр не является наследником или родителем TypeError"""
        if isinstance(other, Product):
            self.product_list.append(other)
            return f'Добавлено'
        raise TypeError



