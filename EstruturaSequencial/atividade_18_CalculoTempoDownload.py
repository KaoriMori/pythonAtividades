'''

Larissa Kaori Morinaga 17-12-2018

Faça um programa que peça o tamanho de um arquivo para download (em MB) e a velocidade de um
link de Internet (em Mbps), calcule e informe o tempo aproximado de download do arquivo usando
este link (em minutos).
'''
import math

megaBytes = float(input("\n\t Digite o tamanho do arquivo (MB): "))
link = float(input("\n\t Digite a velocidade da internet (Mbps): "))

tempo = math.ceil((megaBytes * link)/ 60)

print("\n\t O tempo de download do arquivo é de:", tempo,"minutos")