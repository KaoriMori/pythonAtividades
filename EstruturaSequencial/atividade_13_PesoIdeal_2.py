'''

Larissa Kaori Morinaga 17-12-2018

Tendo como dado de entrada a altura (h) de uma pessoa, construa um algoritmo que calcule seu peso ideal, utilizando as seguintes fórmulas:
Para homens: (72.7*h) - 58
Para mulheres: (62.1*h) - 44.7
'''

altura= float(input(" \n\t Digite sua altura: "))
genero= input("\n\t Digite seu gênero: ")

if genero == "mulher":
    peso_ideal = (62.1 * altura) - 44.7
else:
    peso_ideal = (72.7 * altura) - 58

print(" \n\t Seu peso ideal é: %.2f" % peso_ideal)