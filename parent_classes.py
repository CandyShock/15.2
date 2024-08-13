from abc import ABC, abstractmethod

from Mixins import MixinTest


class Category(MixinTest):
    def __init__(self, name, desc, obj):
        self.__list_t = []
        self.name = name
        self.desc = desc
        """количество на складе"""
        self.obj = obj

    @classmethod
    def list_t(cls, emp):
        name, desc, obj = emp.split(' ')
        return cls(name, desc, obj)

    def list_append(self, data):
        self.__list_t.append(data)

    def clsxv(self):
        return self.__list_t

    @property
    def ostatok(self):
        return f"Имя: {self.name} | Остаток: {self.obj}"

    def __str__(self):
        return f"{self.name}"

    def __len__(self):
        return len(self.__list_t)


class Shape(ABC):
    """Абстрактный класс"""

    @abstractmethod
    def print_name(self):
        pass


class Product(Shape, MixinTest):
    def __init__(self, name, desc, price, count):
        self.name = name
        self.desc = desc
        self.price = price
        self.count = count
        self.category_count = 3
        self.product_count = 3

    def print_name(self):
        print(self.name)

    @classmethod
    def create_product(cls, product):
        a, b, c, v = product.split("-")
        return cls(a, b, c, v)

    @property
    def func(self):
        if self.price <= 0:
            return f"Цена не должна быть равна 0"
        return f"Цена: {self.price}"

    @func.setter
    def func(self, data):
        if data <= 0:
            print("не может быть такого значения")
        elif data < self.price:
            user = input("y если хотите поменять значение ")
            if user == "y":
                self.price = data
            else:
                print('значение не изменено')

    def __str__(self):
        return f"{self.name} {self.count}"

    def __add__(self, other):
        return self.price * self.count + other.price * other.count

