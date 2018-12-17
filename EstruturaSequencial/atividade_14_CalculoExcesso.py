'''

Larissa Kaori Morinaga 17-12-2018

João Papo-de-Pescador, homem de bem, comprou um microcomputador
para controlar o rendimento diário de seu trabalho.
Toda vez que ele traz um peso de peixes maior que o estabelecido pelo
regulamento de pesca do estado de São Paulo (50 quilos) deve pagar uma
multa de R$ 4,00 por quilo excedente. João precisa que você faça um
programa que leia a variável peso (peso de peixes) e calcule o excesso.
Gravar na variável excesso a quantidade de quilos além do limite e na
variável multa o valor da multa que João deverá pagar.
Imprima os dados do programa com as mensagens adequadas
'''

print("\n\t Calculo de multa por peso excedente de peixe.")
peso = float(input("\n\t Digite o peso dos peixes (kg): "))

if peso <= 50:
    print("\n\t Não existe excesso")
else:
    excesso = peso - 50

    multa = excesso * 4

    print("\n\t O excesso no peso dos peixes é de %.2f" %excesso, "kg e portanto a multa a ser paga é de R$ %.2f" %multa)