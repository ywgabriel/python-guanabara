# - Exercício 011
"""
Faça um programa que leia a largura e a altura de uma parede em metros, calcule a sua área e a quantidade de tinta
necessária para pintá-la, sabendo que cada litro de tinta, pinta uma área de 2m².
"""

largura = float(input('Largura da sua parede (m): '))
altura = float(input('Altura da sua parede (m): '))
area = largura * altura
litros = area / 2
print(f'Sua parede tem a dimensão de {largura}x{altura} e sua área é de {area} m²')
print(f'Sabendo que um litro de tinta pinta 2 m² de uma parede, você precisará de {litros} litros de tinta para pintá-la.')
