#Faça um programa que leia 5 valores numéricos e guarde-os em uma lista.
#No final, mostre qual foi o maior e o menor valor digitado e as suas respectivas posições na lista.


valores = list()
for cont in range(0,5):
    valores.append(int(input(f'Digite um valor na posiçao {cont}: ')))
print('=-'*20)
print(f'Voce digitou os valores {valores}')

maior = max(valores)
menor = min(valores)

print(f'O maior valor foi {max(valores)} que esta na posição', end='')
for c in range(0, 5):
    if valores[c] == maior:
        print(f' {c}', end='...')


print(f'\nO menor valor foi {min(valores)} que esta na posiçao', end='')
for c in range(0, 5):
    if valores[c] == menor:
        print(f' {c}', end='...')

