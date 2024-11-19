def tabuada(numero):
    
    for i in range(1, 11):  # Loop de 1 a 10 para mostrar a tabuada
        resultado = numero * i
        print(f"{numero} x {i} = {resultado}")

# Saudação inicial e explicação
print("🎉 Bem-vindo ao Gerador de Tabuada! 🎉")
print("Informe um número e veja a tabuada dele de 1 a 10.\n")

# Solicita o número ao usuário de forma amigável
numero = int(input("Digite um número inteiro para ver a tabuada: "))

# Chama a função para gerar e exibir a tabuada
print("\nAqui está a sua tabuada:")
tabuada(numero)

# Mensagem de despedida
print("\nEspero que tenha sido útil! Até a próxima! 😊")
