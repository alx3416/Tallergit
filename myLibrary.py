import math


def getAreaRectangle(sideB, sideA):
    return sideA * sideB


def getPerimeterRectangle(sideA, sideB):
    return (sideA + sideB) * 2


def gerAreaCircle(radius):
    return math.pi * (radius ** 2)


def gerPerimeterCircle(radius):
    return math.pi * (radius * 2)
