# Crie um programa que faça o computador jogar Jokenpô com você


import random

op = ['pedra', 'papel', 'tesoura']
comp = random.choice(op)
jogador = str(input('''Escolha oq vc vai jogar (pedra, papel ou tesoura): ''')).strip().lower()

print(f'\nO computador escolheu {comp} e você escolheu {jogador}!')

if comp == jogador:
    print('\033[33mEmpate!\033[m')

elif comp == 'tesoura':
    if jogador == 'pedra':
        print('VC ganhou')
    else:
        print('VC perdeu')

elif comp == 'pedra':
    if jogador == 'papel':
        print('VC ganhou')
    else:
        print('VC perdeu')

elif comp == 'papel':
    if jogador == 'tesoura':
        print('VC ganhou')
    else:
        print('VC perdeu')
