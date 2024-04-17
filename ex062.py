#Faça um programa que leia  o primeiro termo e a razão de uma PA,
# mostrando os 10 primeiros termos da progressão usando a estrutura while.


a1 = int(input('Primeiro termo da P.A.: '))
r = int(input('A razão da P.A.: '))
c = 1
p = 10
total = 0
termo= a1
while p != 0:
    total=total+p
    while c <= total:
        print(termo, end=' ➡ ')
        termo = a1 + (c * r)
        c += 1
    print('PAUSA')
    p = int(input('Quantos termos a mais vc gostaria de colocar?'))
print('FIM')
print(f'O Programa foi finalizado com o total de {total} termos')




