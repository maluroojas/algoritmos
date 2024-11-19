def contar_palavras_unicas(frase):
    palavras = frase.lower().split()  # Converte a frase para minúsculas e separa as palavras
    palavras_unicas = set(palavras)  # Elimina duplicatas ao criar um conjunto
    return len(palavras_unicas)  # Retorna a quantidade de palavras únicas

print("📝 Bem-vindo ao Contador de Palavras Únicas! 📝")
print("Digite uma frase para descobrir quantas palavras únicas ela possui.\n")

frase_usuario = input("Digite sua frase: ")

quantidade_unicas = contar_palavras_unicas(frase_usuario)

print(f"\n🔍 Sua frase contém >>{quantidade_unicas}<< palavras únicas.")
print("\nEspero que tenha ajudado! Até logo! 😊")

