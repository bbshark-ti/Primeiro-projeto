import random

def aposta(): #def funcao bem util
    saldo = 100  # Saldo inicial
    while True: #apostar baseado em saldo
        print(f"Seu saldo atual é: R${saldo}")
        aposta = int(input("Digite o valor da sua aposta: "))
        if aposta > saldo:
            print("Saldo insuficiente!")
            continue #usando para continua loop
                #escolher numero para apostar
        numero_apostado = int(input("Escolha um número entre 1 e 10: "))
        numero_sorteado = random.randint(1, 10)

        if numero_apostado == numero_sorteado:
            ganho = aposta * 10
            saldo += ganho
            print(f"Parabéns! Você ganhou R${ganho}.")
        else:
            saldo -= aposta
            print(f"Você perdeu! O número sorteado foi {numero_sorteado}.")

        if saldo <= 0:
            print("Você ficou sem saldo! Fim de jogo.")
            break
#break oferece a possibilidade de sair de um loop quando uma condição externa é acionada. prefencia usar apos if
        continuar = input("Deseja continuar apostando? (s/n): ")
        if continuar.lower() != 's':
            break

    print(f"Seu saldo final é: R${saldo}")

aposta()
      #jogo baseado em aposta com valor fixo,perde caso acabe seu saldo,ficou mais facil utilizar IA pra ajuda escreve muito mais facil utilizar ganho e saldo para digita cod