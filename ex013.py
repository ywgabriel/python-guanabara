# - Exercício 013
# Faça um algoritmo que leia o salário de um funcionário e mostre seu novo salário, com 15% de aumento.

salario = float(input('Qual é o salário do funcionário? R$ '))
novosalario = salario * (115 / 100)
print(f'Um funcionário que ganhava R${salario:.2f}, com 15% de aumento irá ganhar R${novosalario:.2f}')
