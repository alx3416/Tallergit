import math

def volumen_cilindro(radio, altura):
    # Calcular el volumen del cilindro utilizando la fórmula V = pi * r^2 * h
    volumen = math.pi * radio**2 * altura
    return volumen

# Ejemplo de uso
radio_cilindro = 3.0
altura_cilindro = 5.0

resultado = volumen_cilindro(radio_cilindro, altura_cilindro)
print(f'El volumen del cilindro es: {resultado:.2f}')
