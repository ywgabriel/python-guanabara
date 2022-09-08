# - Desafio 013
# Faça um algoritmo que leia o salário de um funcionário e mostre seu novo salário, com 15% de aumento.

salario1 = float(input('De quanto foi seu salário do mês passado, antes do aumento de 15% desse mês? '))
salario2 = salario1 * 1.15
print(f'Então seu salário desse mês vai ser de: R$ {salario2:.2f}.')
