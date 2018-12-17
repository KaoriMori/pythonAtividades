'''

Larissa Kaori Morinaga 17-12-2018

Faça um Programa que peça 2 números inteiros e um número real.
Calcule e mostre:

a. o produto do dobro do primeiro com metade do segundo .
b. a soma do triplo do primeiro com o terceiro.
c. o terceiro elevado ao cubo.
'''

import math

int1 = int(input("\n\t Digite o primeiro valor inteiro: "))
int2 = int(input("\n\t Digite o segundo valor inteiro: "))
real = float(input("\n\t Digite o numero real: "))

opcaoA = (2 * int1) * (int2 / 2)
opcaoB = (3 * int1) + real
opcaoC = math.pow(real, 3)

print(" \n\t O produto do dobro de", int1, "e a metade de", int2, "é: ", opcaoA)
print(" \n\t A soma do tripo de", int1, "e", real, "é: ", opcaoB)
print(" \n\t O cubo de", real, "é: ", opcaoC)
