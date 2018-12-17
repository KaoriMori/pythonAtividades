'''

Larissa Kaori Morinaga 17-12-2018

Faça um Programa que peça a temperatura em graus Celsius,
transforme e mostre em graus Farenheit.
'''

celsius = float(input("\n\t Digite a temperatura em Celsius: "))

farenheit = (celsius * 9/5) + 32

print("\n\t A temperatura %.1f" % celsius, "°C em Farenheit é: %.1f" % farenheit, "°F")