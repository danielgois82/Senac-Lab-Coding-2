print('Canção: Cinco patinhos.\n')

patinhos = {
    5: 'Cinco patinhos',
    4: 'Quatro patinhos',
    3: 'Três patinhos',
    2: 'Dois patinhos',
    1: 'Um patinho'
}

trecho = 'foram passear\nAlém das montanhas para brincar\nA mamãe gritou: Quá, quá, quá, quá\nMas só'
trecho2 = 'foi passear\nAlém das montanhas para brincar\nA mamãe gritou: Quá, quá, quá, quá\nMas'
trecho3 = 'Poxa a mamãe patinha ficou tão triste naquele dia\nAonde será que estavam os seus filhotinhos?\nMas essa história vai ter um final feliz\nSabe porque?\n\n'
trecho4 = 'A mamãe patinha foi procurar\nAlém das montanhas, na beira do mar\nA mamãe gritou: Quá, quá, quá, quá!\nE os cinco patinhos voltaram de lá\n'

musica = ''

for i in range(5, 0, -1):
    if i > 2:
        musica += f'{patinhos[i]} {trecho} {patinhos[i -1].lower()} voltaram de lá\n\n'
    elif i > 1:
        musica += f'{patinhos[i]} {trecho} {patinhos[i -1].lower()} voltou de lá\n\n'
    else:
        musica += f'{patinhos[i]} {trecho2} nenhum patinho voltou de lá\n\n{trecho3}{trecho4}'

print(musica)

