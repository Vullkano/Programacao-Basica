class Rectangle:

    def __init__(self, w, h):
        self.__w = w
        self.__h = h

    def area(self):
        return self.__w * self.__h

    def perimetro(self):
        return 2 * self.__w + 2 * self.__h

    def diag(self):
        return (self.__w ** 2 + self.__h ** 2) ** (1 / 2)

    def is_square(self):
        return self.__w == self.__h

    def scale(self, f):
        return Rectangle(self.__w * f, self.__h * f)

    def sum(self, w, h):
        return Rectangle(self.__w + w, self.__h + h)

    def is_area_greater_than(self, r):
        return self.area() > r.area()

    def __eq__(self, other):
        if not isinstance(other, self.__class__):
            return False
        return self.__w == other.__w and self.__h == other.__h

    def __str__(self):
        return "width: " + str(self.__w) + "; " + "height: " + str(self.__h) + "; " + "Área: " + str(
            self.area()) + "; " + "Perímetro: " + str(self.perimetro()) + "; " + "Diagonal: " + str(self.diag())


r1 = Rectangle(3, 5)
r2 = Rectangle(3, 5)
r3 = Rectangle(4, 3)

same_object = r1 is r2
equal = r1 == r2


class Contact:

    def __init__(self, name, phone):
        self.__name = name
        self.phone = phone

    @property
    def name(self):
        return self.__name

    def show(self):
        print("Name: ", self.name, " Phone:", self.phone)

    def __eq__(self, other):
        if not isinstance(other, self.__class__):
            return False
        return self.__name == other.__name and self.phone == other.phone

    def __str__(self):
        return "Name: " + str(self.__name) + "; " + "Phone: " + str(self.phone)


c1 = Contact('Jony', '987654321')
c2 = Contact('Jony', '987654321')
c3 = Contact('Memory error', '404404404')

print(c1 is c2)
print(c1 == c2)
