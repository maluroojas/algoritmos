import random

def jogar_adivinhacao():

    # Gera um número secreto aleatório entre 1 e 100
    numero_secreto = random.randint(1, 100)
    tentativas = 0  # Contador de tentativas
    acertou = False  # Estado do jogo: True se o jogador acertar

    print("=== Bem-vindo ao Jogo de Adivinhação! ===")
    print("O objetivo é adivinhar o número secreto entre 1 e 100.")
    print("Boa sorte!\n")

    # Loop principal do jogo
    while not acertou:
        try:
            # Solicita o palpite do jogador
            palpite = int(input("Digite seu palpite: "))
            tentativas += 1  # Incrementa o número de tentativas

            # Verifica a relação do palpite com o número secreto
            if palpite < numero_secreto:
                print("Dica: O número secreto é >>maior<<. Tente novamente!\n")
            elif palpite > numero_secreto:
                print("Dica: O número secreto é >>menor<<. Tente novamente!\n")
            else:
                acertou = True
                print(f"\n🎉 Parabéns! Você acertou o número secreto: {numero_secreto}!")
                print(f"Você conseguiu em {tentativas} tentativas.")
        except ValueError:
            print("Entrada inválida! Por favor, insira um número inteiro.\n")

# Inicia o jogo
jogar_adivinhacao()

