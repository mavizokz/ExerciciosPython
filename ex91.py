#Exercício Python 091: Crie um programa onde 4 jogadores joguem um dado e tenham resultados aleatórios.
# Guarde esses resultados em um dicionário em Python.
# No final, coloque esse dicionário em ordem, sabendo que o vencedor tirou o maior número no dado.


import random
import time
game = dict()
final = list()
for c in range(1, 5):
    time.sleep(1)
    game[f'jogador_{c}'] = random.randint(1, 6)
    print(f'O jogador{c} tirou {game["jogador_" + str(c)]} no dado')
print('-='*20)
print(f'== RANKING DOS JOGADORES ==')
final = (sorted(game.items(), key=lambda x: x[1], reverse=True))
for c, j in enumerate(final):
    print(f'{c+1}° lugar: {j[0]} com {j[1]}')







