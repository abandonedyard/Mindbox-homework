import math
from abc import ABC, abstractmethod


class Shape(ABC):
    """Базовый класс всех фигур."""
    @abstractmethod
    def area(self) -> float:
        """Площадь фигуры."""
        pass


class Circle(Shape):
    """Круг по радиусу."""
    def __init__(self, radius: float):
        if radius <= 0:
            raise ValueError("Радиус должен быть положительным")
        self.radius = radius

    def area(self) -> float:
        return math.pi * self.radius ** 2


class Triangle(Shape):
    """Треугольник по трём сторонам."""
    def __init__(self, a: float, b: float, c: float):
        # проверяем положительность сторон
        if a <= 0 or b <= 0 or c <= 0:
            raise ValueError("Стороны должны быть положительными")
        # проверяем существование треугольника
        if a + b <= c or a + c <= b or b + c <= a:
            raise ValueError("Сумма двух сторон должна быть больше третьей")
        self.a, self.b, self.c = a, b, c

    def area(self) -> float:
        s = (self.a + self.b + self.c) / 2
        return math.sqrt(s * (s - self.a) * (s - self.b) * (s - self.c))

    def is_right(self) -> bool:
        """Проверка, является ли треугольник прямоугольным."""
        x, y, z = sorted((self.a, self.b, self.c))
        return abs(x*x + y*y - z*z) < 1e-9


def compute_area(shape: Shape) -> float:
    """Вычисление площади без знания типа фигуры в compile-time."""
    return shape.area()
