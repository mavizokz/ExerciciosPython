# Crie um programa que vai gerar cinco números aleatórios e colocar em uma tupla.
# Depois disso, mostre a listagem de números gerados e também indique o menor e o maior valor que estão na tupla.



from random import randint
nums =  (randint(1, 10), randint(1, 10), randint(1, 10), randint(1, 10), randint(1, 10), )
print('Os valores sorteados foram: ', end='')
for n in nums:
    print(f'{n} ', end ='')
print(f'\nO maior valor sorteado foi {max(nums)}')
print(f'O menos valor sorteado foi  {min(nums)}')
