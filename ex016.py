# - Exercício 016
# Crie um programa que leia um número real qualquer pelo teclado e mostre na tela sua porção inteira.

import math
valor = float(input('Digite um valor: '))
porcaointeira = math.trunc(valor)
print(f'O valor digitado foi {valor} e sua porção inteira é de {porcaointeira}.')
