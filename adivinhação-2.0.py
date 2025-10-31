from random import randint
computador = randint(0, 10)
print("o computador vai escolher entre 0 a 10, acerte o numero escolhido")
print("sera que voce vai conseguir acertar?")
acertou = False
palpites = 0 
while not acertou:
    jogador = int(input("O numero escolhido foi: "))
    palpites += 1
    if jogador == computador:
        acertou = True
    else:
        if jogador < computador:
            print("Mais...")
        elif jogador > computador:
            print("Menos...")

print("Parabéns! Você acertou com {} palpites".format(palpites))
