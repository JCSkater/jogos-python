from random import randint
from time import sleep
computador = randint(1, 3)

if computador == 1:
    computador = 'pedra'
elif computador == 2:
    computador = 'papel'
elif computador == 3:
    computador = 'tesoura'

print('=' * 10)
print('JO-KEN-PÔ!!')
print('=' * 10)

jogador = str(input('Escolha uma das três opções: Pedra, Papel, Tesoura: ').lower().strip())
print('Jo...')
sleep(1)
print('ken...')
sleep(1)
print('PÔ!')

print('-=-' * 15)
if computador == jogador:
    print(f'Você escolheu {jogador} e eu escolhi {computador} \nempate.')
elif computador == 'pedra': 
    if jogador == 'papel':
        print(f'Você escolheu {jogador} e eu escolhi {computador} \npapel embrulha pedra. Você ganhou')
    elif jogador == 'tesoura':
        print(f'Você escolheu {jogador} e eu escolhi {computador} \npedra quebra tesoura. Você perdeu')
elif computador == 'papel': 
    if jogador == 'pedra':
        print(f'Você escolheu {jogador} e eu escolhi {computador} \npapel embrulha pedra. Você perdeu')
    elif jogador == 'tesoura':
        print(f'Você escolheu {jogador} e eu escolhi {computador} \ntesoura corta papel. Você ganhou')
elif computador == 'tesoura': 
    if jogador == 'pedra':
        print(f'Você escolheu {jogador} e eu escolhi {computador} \npedra quebra tesoura. Você ganhou')
    elif jogador == 'papel':
        print(f'Você escolheu {jogador} e eu escolhi {computador} \ntesoura corta papel. Você perdeu')
else:
    print('Opção inválida')
print('-=-' * 15)
sleep(10)