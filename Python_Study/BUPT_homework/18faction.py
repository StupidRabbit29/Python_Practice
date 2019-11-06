def gcd(a, b):
    i = 0
    if a < b:
        i = a
    else:
        i = b
    while i > 0:
        if a % i == 0 and b % i == 0:
            return i
        else:
            i = i - 1


class Faction:
    def __init__(self, numerator, denominator):
        self.numerator = numerator
        self.denominator = denominator
        if self.denominator < 0:
            self.denominator = - self.denominator
            self.numerator = - self.numerator
        i = gcd(abs(self.numerator), abs(self.denominator))
        self.numerator = int(self.numerator / i)
        self.denominator = int(self.denominator / i)

    def show(self):
        print(self.numerator, '/', self.denominator, sep='')

    def show_numerator(self):
        return self.numerator

    def show_denominator(self):
        return self.denominator

    def __add__(self, fact):
        return Faction(self.numerator * fact.denominator + self.denominator * fact.numerator, self.denominator * fact.denominator)

    def __sub__(self, fact):
        return Faction(self.numerator * fact.denominator - self.denominator * fact.numerator, self.denominator * fact.denominator)

    def __mul__(self, fact):
        return Faction(self.numerator * fact.numerator, self.denominator * fact.denominator)

    def __truediv__(self, fact):
        return Faction(self.numerator * fact.denominator, self.denominator * fact.numerator)

    def riceprocal(self):
        return Faction(self.denominator, self.numerator)

    def floatnum(self):
        print('%.1f' % (self.numerator / self.denominator))


a, b, c, d = map(int, input().split())
fact1 = Faction(a, b)
fact2 = Faction(c, d)
fact1.show()
fact2.show()
temp = fact1 + fact2
temp.show()
temp = fact1 - fact2
temp.show()
temp = fact1 * fact2
temp.show()
temp = fact1 / fact2
temp.show()
fact1.riceprocal().show()
fact1.floatnum()
