class MixinTest:
    """репр для вывода информации о всех объектах класса вызывается repr()"""
    def __init__(self):
        super().__init__()

    def unpuck(self):
        a = []
        for k, v in self.__dict__.items():
            """product и category в любом случае попадают в миксин, не знаю как настроить так что бы попадали
            только нужные переменные"""
            if k == "product_count":
                pass
            elif k == "category_count":
                pass
            else:
                s = f"{k}:{v}"
                a.append(s)
        return " ".join(a)

    def __repr__(self):
        return f"создан объект класса {self.__class__.__name__}({self.unpuck()})"
