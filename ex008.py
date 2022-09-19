# - Exercício 008
# Escreva um programa que leia um valor em metros e exiba convertido em centímetros e milímetros.

distancia = float(input('Digite uma distância em metros: '))
km = distancia / 1000
hm = distancia / 100
dam = distancia / 10
cm = distancia * 100
mm = distancia * 1000
print(f'A medida de {distancia} metros corresponde a:')
print(f'{km} quilômetros (km)')
print(f'{hm} hectômetros (hm)')
print(f'{dam} decâmetros (dam)')
print(f'{cm} centrímetos (cm)')
print(f'{mm} milímetros (mm)')
