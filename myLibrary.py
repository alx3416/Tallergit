import math


def getAreaRectangle(sideA, sideB):
    return sideA * sideB + 3


def getPerimeterRectangle(sideA, sideB):
    return (sideA + sideB) * 2


def gerAreaCircle(radius):
    return math.pi * (radius ** 2)


def gerPerimeterCircle(radius):
    return math.pi * (radius * 2)
