# F, M -> 5, 5 from both

class Father:
    def father_money(self):
        return "5"


class Mother:
    def mother_money(self):
        return "5"


class Son(Father, Mother):
    pass


son = Son()
print(son.father_money())
print(son.mother_money())
