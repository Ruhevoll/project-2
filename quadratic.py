import numpy as np
import math
import matplotlib.pyplot as plt

def sign(x):
    if x >= 0:
        return '+'
    else:
        return '-'


class quad():
    def __init__(self, a, b, c):
        """
        Function to create a quadratic.
        :param a: Leading coefficient.
        :param b: Coefficient of the middle term.
        :param c: Constant term.
        """
        self.__a = a
        self.__b = b
        self.__c = c

    def equation(self) -> str:
        """
        Display the mathematical expression of the quadratic.
        :return: Returns the quadratic's mathematical expression.
        """
        return f'{self.__a}𝒙\u00b2 {sign(self.__b)} {abs(self.__b)}𝒙 {sign(self.__c)} {abs(self.__c)}'

    def graph(self):
        """
        Graph the quadratic on the plane.
        :return: Saves a picture of the parabola generated by the quadratic equation.
        """
        plt.clf()
        x = np.linspace(-10, 10, 100)
        plt.plot(x, self.__c + self.__b*x + self.__a*x**2)
        plt.savefig("graph.png")

    def roots(self) -> str:
        """
        Compute the roots of the quadratic.
        :return: Returns the expression of the roots of the quadratic.
        """
        if self.__b**2 - 4*self.__a*self.__c > 0:
            x1 = (-self.__b + math.sqrt(self.__b**2 - 4*self.__a*self.__c))/(2*self.__a)
            x2 = (-self.__b - math.sqrt(self.__b**2 - 4*self.__a*self.__c))/(2*self.__a)
            return f'𝒙\u2081 = {round(x1, 4)}, 𝒙\u2082 = {round(x2, 4)}'

        elif self.__b**2 - 4*self.__a*self.__c == 0:
            x1 = (-self.__b + math.sqrt(self.__b ** 2 - 4 * self.__a * self.__c)) / (2 * self.__a)
            return f'𝒙\u2081 = 𝒙\u2082 = {round(x1, 4)}'

        elif self.__b**2 - 4*self.__a*self.__c < 0:
            return f'𝒙\u2081 = {-self.__b} + 𝒊{round(math.sqrt(4*self.__a * self.__c - self.__b**2),4)}, 𝒙\u2082 = {-self.__b} - 𝒊{round(math.sqrt(4*self.__a * self.__c - self.__b**2), 4)}'


    def vertex(self) -> str:
        """
        Compute the vertex of the quadratic.
        :return: Returns the coordinates of the vertex of the quadratic.
        """
        return f'({round((-self.__b)/(2*self.__a),4)}, {round(self.__a*((-self.__b)/(2*self.__a))**2 + self.__b*((-self.__b)/(2*self.__a)) + self.__c, 4)})'

    def factor(self) -> str:
        """
        Factor the quadratic.
        :return: Returns the expression for the factorization of the quadratic.
        """
        if self.__b ** 2 - 4 * self.__a * self.__c > 0:
            x1 = (-self.__b + math.sqrt(self.__b ** 2 - 4 * self.__a * self.__c)) / (2 * self.__a)
            x2 = (-self.__b - math.sqrt(self.__b ** 2 - 4 * self.__a * self.__c)) / (2 * self.__a)
            return f'(𝒙 {sign(-1*x1)} {round(abs(x1), 4)})(𝒙 {sign(-1*x2)} {round(abs(x2), 4)})'

        elif self.__b ** 2 - 4 * self.__a * self.__c == 0:
            x1 = (-self.__b + math.sqrt(self.__b ** 2 - 4 * self.__a * self.__c)) / (2 * self.__a)
            return f'(𝒙 {sign(-1*x1)} {round(abs(x1), 4)})\u00b2'

        elif self.__b ** 2 - 4 * self.__a * self.__c < 0:
            return f'(𝒙 - ({-self.__b} + 𝒊{math.sqrt(4 * self.__a * self.__c - self.__b ** 2)})) (𝒙 - ({-self.__b} - 𝒊{math.sqrt(4 * self.__a * self.__c - self.__b ** 2)}))'





