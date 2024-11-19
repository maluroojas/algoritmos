def contar_caracteres(palavra):
    # Retorna o número total de caracteres na palavra
    return len(palavra)

# Mensagem de boas-vindas e instrução clara
print("👋 Bem-vindo ao contador de caracteres! 🧑‍💻")
print("Digite uma palavra, e eu direi quantos caracteres ela tem.\n")

# Solicita ao usuário que insira uma palavra
palavra = input("Por favor, digite uma palavra: ")

# Conta os caracteres e exibe o resultado de forma amigável
quantidade = contar_caracteres(palavra)
print(f"\n✨ A palavra '{palavra}' tem >>{quantidade}<< caracteres.\n")

# Despedida com uma mensagem leve e acolhedora
print("Obrigado por usar o contador! Volte sempre que precisar. Até logo! 👋")

