jokenpô = ['pedra', 'papel', 'tesoura']
from random import choice
from time import sleep
print("Vamos jogar JOKENPÔ")
computador = choice(jokenpô)
jogador = str(input("Escolha entre pedra, papel ou tesoura: ").lower())
print("JO")
sleep(1)
print("KEN")
sleep(1)
print("PÔ")
sleep(1)
if jogador == computador:
    print("Empate!! Os dois escolheram {}".format(jogador))
elif jogador == 'pedra' and computador == 'tesoura':
    print("Voce VENCEU!! Voce escolheu {} e o computador escolheu {}".format(jogador, computador))
elif jogador == 'papel' and computador == 'pedra':
    print("Voce VENCEU!! Voce escolheu {} e o computador escolheu {}".format(jogador, computador))
elif jogador == 'tesoura' and computador == 'papel':
    print("Voce VENCEU!! Voce escolheu {} e o computador escolheu {}".format(jogador, computador))
else:
     print("Voce PERDEU!! Voce escolheu {} e o computador escolheu {}".format(jogador, computador))