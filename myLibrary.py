import math


def getAreaRectangle(side1, side2):
    return side1 * side2


def getPerimeterRectangle(sideA, sideB):
    return (sideA + sideB) * 2


def gerAreaCircle(radius):
    return math.pi * (radius ** 2)


def gerPerimeterCircle(radius):
    return math.pi * (radius * 2)


def gerPerimeterTriangle(side1, side2, side3):
    return side1 + side2 + side3


def getAreaTriangle(side, height):
    return (side * height) / 2