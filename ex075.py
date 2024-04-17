# Desenvolva um programa que leia quatro valores pelo teclado e guarde-os em uma tupla. No final, mostre:

#A) Quantas vezes apareceu o valor 9.
#B) Em que posição foi digitado o primeiro valor 3.
#C) Quais foram os números pares.


valores = (int(input('Digite um valor: ')),
          int(input('Digite um valor: ')),
          int(input('Digite um valor: ')),
          int(input('Digite um valor: ')))
print(f'Os  valores digitados foram {valores}')
print(f'O  numero 9 aparaceu  {valores.count(9)} vezes')
try:
    ndx = print(f'O número 3 foi digitado na poisção {valores.index(3)+1}')
except:
    ndx = print(f'Não teve número 3 nessa tupla')
print(f'Os números pares foram:', end=' ')
for n in valores:
    if n % 2 == 0:
        print(f'{n}', end=' ')


