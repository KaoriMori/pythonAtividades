'''

Larissa Kaori Morinaga 17-12-2018

Faça um Programa que pergunte quanto você ganha por hora e o número de horas trabalhadas no mês.
Calcule e mostre o total do seu salário no referido mês.
'''

salario_hora = float(input("\n\t Digite o salário recebido por hora: "))
mes = input("\n\t Digite o mês de trabalho: ")
horas_trabalhadas = float(input("\n\t Digite a quantidade de horas trabalhadas no mês: "))

salario_mensal = salario_hora * horas_trabalhadas

print("\n\t O salário mensal recebido no mês de", mes, "é de %.2f" % salario_mensal)