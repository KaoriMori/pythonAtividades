'''

Larissa Kaori Morinaga 17-12-2018

Faça um Programa que peça o raio de um círculo, calcule e mostre sua área.
'''
import math

raio = float(input("\n\t Digite o raio de um círculo: "))

area = math.pow(raio, 2) * math.pi

print("\n\t A área do círculo de raio", raio, "é %.2f" % area)