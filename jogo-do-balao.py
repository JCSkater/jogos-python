from random import randint
from time import sleep
computador = randint(0, 1000) # Faz o computador "pensar", ou seja, sorteia um número entre 0 e 1000.
tentativas = 10
print('-=-' * 32)
print('JOGO DO BALÃO \nVou pensar em um número entre 0 e 1000 e você tem 10 tentativas para acertar... Tente adivinhar.')
print('-=-' * 32)

while tentativas != 0:
    jogador = int(input('Em qual número eu pensei?: ')) # Jogador tenta adivinhar
    if jogador == computador:
        print(f'Certa a resposta! eu pensei no {computador} mesmo.')
        sleep(10)
        break
    elif jogador < computador: 
        print('hum...')
        sleep(1)
        print(f'Mais!!')
    elif jogador > computador: 
        print('hum...')
        sleep(1)
        print(f'Menos!!')
    tentativas -=1
if tentativas == 0:
    print(f'Você perdeu! a resposta certa era: {computador}')
    sleep(10)