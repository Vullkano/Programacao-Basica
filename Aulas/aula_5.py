class Calculator:

    def __init__(self):
        self.__value = 0

    @property
    def value(self):
        return self.__value

    def add(self, n):
        self.__value += n

    def reset(self):
        self.__value = 0

    def subtracao(self, n):
        self.__value -= n

    def multiplicacao(self, n):
        i = n
        a = self.__value
        while i > 1:
            self.__value += a
            i -= 1
        if i == 0:
            self.__value = 0

    def tencia(self, n):
        i = 1
        while i < n:
            self.multiplicacao(c.value)
            i += 1

    def divide(self, n):
        self.__value = int(self.__value / n)

    def resto(self, n):
        i = self.__value
        while i >= n:
            self.__value -= n
            i = self.__value


c = Calculator()
c.add(5)


class Rectangle:

    def __init__(self, width, height):
        self.__width = width
        self.__height = height
        self.__perimetro = 2 * self.__height + 2 * self.__width
        self.__area = self.__height * self.__width

    @property
    def width(self):
        return self.__width

    @property
    def height(self):
        return self.__height

    @property
    def perimetro(self):
        return self.__perimetro

    @property
    def area(self):
        return self.__area

    def is_square(self):
        return self.__width == self.__height

    def diagonal(self):
        return (self.__height ** 2 + self.__width ** 2) ** 0.5

    def scale(self, factor):
        self.__width *= factor
        self.__height += factor

    def sum(self, width, height):
        self.__width += width
        self.__height += height

    def is_smaller(self, width, height):
        a = width * height
        if a > self.__area:
            return True
        else:
            return False

    def __str__(self):
        return "width: " + str(self.__width) + "; " + "height: " + str(self.__height) + "; " + "Área: " + str(
            self.__area) + "; " + "Perímetro: " + str(self.__perimetro) + "; " + "Diagonal: " + str(self.diagonal())


def max_rectangle(a, b):
    x = a.area
    y = b.area
    if y > x:
        print(b)
    else:
        print(a)


r1 = Rectangle(2, 3)
r2 = Rectangle(2, 2)


class Contacto:

    def __init__(self, name, phone):
        self.__name = name
        self.phone = phone

    @property
    def name(self):
        return self.__name

    def __str__(self):
        return 'Nome: ' + str(self.__name) + ' --> ' + 'Contacto: ' + str(self.phone)


c1 = Contacto('Jony', 937541632)
c2 = Contacto('Karen', 987654321)
c3 = Contacto('David', 974926351)


class Rational:

    def __init__(self, numerador, denominador):
        self.__denominador = denominador
        self.__numerador = numerador

    @property
    def denominador(self):
        return self.__denominador

    @property
    def numerador(self):
        return self.__numerador

    def __float__(self):
        return float(self.__numerador / self.__denominador)

    def sum(self, numerador, denominador):
        if self.__denominador != denominador:
            numerador = numerador * self.__denominador
            self.__numerador = self.__numerador * denominador
            self.__denominador = self.__denominador * denominador
            self.__numerador = self.__numerador + numerador
        else:
            self.__numerador = self.__numerador + numerador

    def mult(self, numerador, denominador):
        self.__numerador = self.__numerador * numerador
        self.__denominador = self.__denominador * denominador

    def is_equal(self, numerador, denominador):
        if float(self.__numerador / self.__denominador) == float(numerador / denominador):
            return True
        else:
            return False

    def is_greater_than(self, numerador, denominador):
        if float(self.__numerador / self.__denominador) > float(numerador / denominador):
            return True
        else:
            return False


a1 = Rational
