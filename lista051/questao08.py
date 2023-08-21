"""
Desenvolver um programa que apresente todos os valores numéricos inteiros ímpares situados
na faixa de 0 até 500.Utilize um laço que efetue a variação de 2 em 2.
"""

cont = 2

while (cont < 500):
    if(cont % 2 > 0):
        print(f"{cont} é ímpar")
    cont = cont + 1