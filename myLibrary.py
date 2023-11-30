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
    area = (side * height) / 2
    return area

def calcular_area_cilindro(radio, altura):
    area_base = 2 * math.pi * (radio ** 2)
    area_lateral = 2 * math.pi * radio * altura
    area_total = area_base + area_lateral
    return area_total