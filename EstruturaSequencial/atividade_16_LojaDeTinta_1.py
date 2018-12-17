'''

Larissa Kaori Morinaga 17-12-2018

Faça um programa para uma loja de tintas. O programa deverá pedir o tamanho em metros
quadrados da área a ser pintada. Considere que a cobertura da tinta é de 1 litro para cada
3 metros quadrados e que a tinta é vendida em latas de 18 litros, que custam R$ 80,00.
Informe ao usuário a quantidades de latas de tinta a serem compradas e o preço total.
'''

import math

metros = float(input("\n\t Digite a quantidade em metros quadrados da área a ser pintada: "))

tinta = metros / 3

latas = int(math.ceil(tinta/18))

print("\n\t A quantidade de latas necessárias para pintar", metros, "da parede é(são): ", latas)

