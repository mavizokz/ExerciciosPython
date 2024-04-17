#Crie um programa que leia um número inteiro e mostre na tela se ele é PAR ou ÍMPAR.

n=int(input('De um numero: '))
d= n%2

if d == 0:
    print('Ele é \033[34mPAR\033[m!')
else:
    print('Ele é \033[34mIMPAR\033[m!')

