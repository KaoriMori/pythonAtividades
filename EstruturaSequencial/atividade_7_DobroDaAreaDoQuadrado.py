'''

Larissa Kaori Morinaga 17-12-2018

Faça um Programa que calcule a área de um quadrado,
em seguida mostre o dobro desta área para o usuário.
'''

import math

lado = float(input("\n\t Digite o lado de um quadrado: "))

area = math.pow(lado, 2)

dobro_Area = area * 2

print("\n\t A área de um quadrado de lado", lado, "é %.2f" % area, "e o dobro desse valor é %.2f" % dobro_Area)