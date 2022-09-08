# - Desafio 011
# Faça um programa que leia a largura e a altura de uma parede em metros.
# Calcule sua área e a quantidade de tinta necessária para pintá-la. Considere: 1 litro de tinta = área de 2m² pintada.

largura = float(input('Qual a largura (em metros) da parede que vai ser pintada? '))
altura = float(input('E qual é a altura (em metros novamente) da parede? '))
area = largura * altura
litros = area / 2
print(f'Sua parede possui uma área de {area}m²')
print(f'Sabendo que cada litro de tinta pinta uma área de 2m², vai ser necessário {litros} litros de tinta para pintar a parede inteira')
