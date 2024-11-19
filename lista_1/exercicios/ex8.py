def contar_numeros(lista):
    contador = 0
    for _ in lista:
        contador += 1
    return contador

print("📋 Bem-vindo ao Contador de Números! 📋")
print("Informe os números de uma lista, separados por espaço.\n")

entrada = input("Digite os números: ")
numeros = entrada.split()  
numeros = [int(num) for num in numeros]

quantidade = contar_numeros(numeros)

print(f"\n🔢 A lista contém >>{quantidade}<< números.")
print("\nEspero que tenha sido útil! Até logo! 😊")
