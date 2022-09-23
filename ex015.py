# - Exercício 015
""""
Escreva um programa que pergunte a quantidade de km percorridos por um carro alugado e a quantidade de dias pelos quais
ele foi alugado. Calcule o preço a pagar, sabendo que o carro custa R$ 60,00 por dia e R$ 0,15 por Km rodado.
"""

dias = float(input('Por quantos dias foi alugado? '))
km = float(input('Quantos km rodados? '))
preco = (dias * 60) + (0.15 * km)
print(f'O total a se pagar pelos dias e a quilometragem do carro é de R$ {preco:.2f}')
