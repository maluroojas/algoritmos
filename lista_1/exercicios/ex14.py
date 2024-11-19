def verificar_palindromo(palavra):
    palavra = palavra.replace(" ", "").lower()  # Remove espaços e coloca tudo em minúsculas

    tamanho = len(palavra)
    for i in range(tamanho // 2):
        if palavra[i] != palavra[tamanho - 1 - i]:  # Compara os caracteres nas posições opostas
            return False
    return True

print("🔄 Bem-vindo ao Verificador de Palíndromos! 🔄")
print("Digite uma palavra para saber se ela é um palíndromo.\n")

palavra_usuario = input("Digite a palavra: ")

if verificar_palindromo(palavra_usuario):
    print(f"\n🎉 A palavra '{palavra_usuario}' é um palíndromo!")
else:
    print(f"\n❌ A palavra '{palavra_usuario}' não é um palíndromo.")

print("\nEspero ter ajudado! Até logo! 😊")
