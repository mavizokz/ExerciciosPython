#Exercício Python 084: Faça um programa que leia nome e peso de várias pessoas,
# guardando tudo em uma lista. No final, mostre:
# A) Quantas pessoas foram cadastradas.
# B) Uma listagem com as pessoas mais pesadas.
# C) Uma listagem com as pessoas mais leves.

temporario = []
pessoas = []
maior = menor = 0

while True:
    temporario.append(str(input('Nome: ')))
    temporario.append(int(input('Peso: ')))
    if len(pessoas)==0:
        maior = temporario[1] #temporario[1] pq o peso esta guardado no indici 1;
        menor = temporario[1]
    else:
        if temporario[1] > maior:
            maior = temporario[1]
        if temporario[1] < menor:
            menor = temporario[1]
    pessoas.append(temporario[:])
    temporario.clear()
    resp = str(input('Quer continnuar?[S/N] '))
    if resp in 'Nn':
        break

print(f'Ao todo, você cadastrou {len(pessoas)} pessoas')
print(f'O maior peso foi {maior}Kg. nomes ', end=' ')
for p in pessoas:
    if p[1] == maior:
        print(f'{p[0]}', end=' ')
print(f'\nO menor peso foi {menor}Kg. nomes ', end=' ')
for p in pessoas:
    if p[1] == menor:
        print(f'{p[0]}', end=' ')