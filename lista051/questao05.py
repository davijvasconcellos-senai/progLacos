"""
Desenvolver um programa que apresente os resultados de uma tabela de um número qualquer.
Ela dever ser impressa no seguinte formato:

Considerando como exemplo o fornecimento de número 2

2.1 = 2
2.2 = 4
2.3 = 6
2.4 = 8
2.5 = 10
(..)
2.10 = 20
"""

cont = 0
num = int(input("Informe um número inteiro: "))

while (cont <= 10):
    print(f"{num} . {cont} = {num * cont}")
    cont = cont + 1