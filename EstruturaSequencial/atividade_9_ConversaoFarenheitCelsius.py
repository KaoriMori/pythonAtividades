'''

Larissa Kaori Morinaga 17-12-2018

Faça um Programa que peça a temperatura em graus Farenheit,
transforme e mostre a temperatura em graus Celsius.
C = (5 * (F-32) / 9).
'''

farenheit = float(input("\n\t Digite a temperatura em Farenheit: "))

celsius = (5 * (farenheit - 32)/9)

print("\n\t A temperatura %.1f" % farenheit, "°F em Celsius é: %.1f" % celsius, "°C")