def inverter_palavra(palavra):
    palavra_invertida = ""
    for letra in palavra:
        palavra_invertida = letra + palavra_invertida
    return palavra_invertida

print("🔄 Bem-vindo ao Inversor de Palavras! 🔄")
print("Digite uma palavra e veja como ela fica ao contrário.\n")

entrada = input("Digite uma palavra: ")

palavra_invertida = inverter_palavra(entrada)

print(f"\n✨ A palavra invertida é: >>{palavra_invertida}<<.")
print("\nEspero que tenha gostado! Até a próxima! 😊")

