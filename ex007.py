# - Exercício 007
# Desenvolva um programa que leia as duas notas de um aluno, calcule e mostre sua média.

primeiranota = float(input('Primeira nota do aluno: '))
segundanota = float(input('Segunda nota do aluno: '))
media = (primeiranota + segundanota) / 2
print(f'A média entre {primeiranota} e {segundanota} é igual a {media}')
