'''

Larissa Kaori Morinaga 17-12-2018

Faça um Programa para uma loja de tintas. O programa deverá pedir o tamanho em metros quadrados
da área a ser pintada. Considere que a cobertura da tinta é de 1 litro para cada 6 metros
quadrados e que a tinta é vendida em latas de 18 litros, que custam R$ 80,00 ou em galões de
3,6 litros, que custam R$ 25,00.
Informe ao usuário as quantidades de tinta a serem compradas e os respectivos preços em
3 situações:

1. comprar apenas latas de 18 litros;
2. comprar apenas galões de 3,6 litros;
3. misturar latas e galões, de forma que o preço seja o menor. Acrescente 10% de folga e
sempre arredonde os valores para cima, isto é, considere latas cheias.
'''

import math

metros = float(input("\n\t Digite a quantidade em metros quadrados da área a ser pintada: "))

tinta = metros / 6

latasGrandes = int(math.ceil(tinta/18))
opcao1 = latasGrandes * 80

latasPequenas = int(math.ceil(tinta/3.6))
opcao2 = latasPequenas * 25

tinta_folga = tinta * 1.1
excesso = tinta % 18
print( excesso )
latasMistasGrandes = int(math.ceil(tinta_folga/18))
latasMistasPequenas = int(math.ceil(excesso/3.6))
print(excesso/3.6)
print(latasMistasPequenas)
opcao3 = latasMistasGrandes * 80 + latasMistasPequenas * 25

print("\n\t A quantidade de latas de 18 litros necessárias para pintar", metros, "da parede é(são):", latasGrandes, "e o preço é: R$ %.2f" % opcao1)
print("\n\t A quantidade de latas de 3,6 litros necessárias para pintar", metros, "da parede é(são):", latasPequenas, "e o preço é: R$ %.2f" % opcao2)
print("\n\t A quantidade de latas de 18 litros e de 3,6 necessárias para pintar", metros, "da parede são, respectivamente :", latasMistasGrandes, "e", latasMistasPequenas, " e o preço é: R$ %.2f" % opcao3)