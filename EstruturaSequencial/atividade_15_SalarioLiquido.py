'''

Larissa Kaori Morinaga 17-12-2018

Faça um Programa que pergunte quanto você ganha por hora e o número de
horas trabalhadas no mês. Calcule e mostre o total do seu salário no
referido mês, sabendo-se que são descontados 11% para o Imposto de Renda,
8% para o INSS e 5% para o sindicato, faça um programa que nos dê:

salário bruto.
quanto pagou ao INSS.
quanto pagou ao sindicato.
o salário líquido.

calcule os descontos e o salário líquido, conforme a tabela abaixo:
+ Salário Bruto : R$
- IR (11%) : R$
- INSS (8%) : R$
- Sindicato ( 5%) : R$
= Salário Liquido : R$
Obs.: Salário Bruto - Descontos = Salário Líquido.
'''

salario_hora = float(input("\n\t Digite o salário recebido por hora: "))
horas_trabalhadas = float(input("\n\t Digite a quantidade de horas trabalhadas no mês: "))

salario_mensal = salario_hora * horas_trabalhadas
ir = salario_mensal * 11 / 100
inss = salario_mensal * 8 / 100
sindicato = salario_mensal * 5 / 100
salario_liquido = salario_mensal - ir - inss - sindicato
print("\n\t + Salário Bruto: RS %.2f" % salario_mensal)
print("\n\t - IR: RS %.2f" % ir)
print("\n\t - INSS: RS %.2f" % inss)
print("\n\t - Sindicato: RS %.2f" % sindicato)
print("\n\t - Salário Líquido: RS %.2f" % salario_liquido)


