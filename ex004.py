# Exercício Python #004 - Dissecando uma Varíavel
# Faça um programa que leia algo pelo teclado e mostre na tela o seu tipo primitivo e todas as informações possíveis ele.

d = input('Digite algo: ')
print(f'O tipo primito desse valor é: {type(d)}')
print(f'Só tem espaços? {d.isspace()}')
print(f'É um número? {d.isnumeric()}')
print(f'É alfabético? {d.isalpha()}')
print(f'Está em maiúsculas? {d.isupper()}')
print(f'Está em minúsculas? {d.islower()}')
print(f'Está capitalizada? {d.istitle()}')
