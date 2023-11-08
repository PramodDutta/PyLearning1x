class GF:
    def car(self):
        return "Old car"


class F(GF):
    pass
    # def car(self):
    #     return "honda civic"


class S(F):
    # def car(self):
    #     return "Lambo"
    pass


son = S()
print(son.car())