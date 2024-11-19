def contar_caracteres(frase):
    
    contador = {}  # Dicionário para armazenar os contadores dos caracteres
    
    # Itera sobre cada caractere da frase
    for char in frase:
        if char in contador:
            contador[char] += 1  # Add o contador se o caractere já existe no dicionário
        else:
            contador[char] = 1  # Add o caractere ao dicionário com o contador inicializado em 1
    
    return contador

frase = input("Digite uma frase: ")
resultado = contar_caracteres(frase)

# Exibe o dicionário com a contagem de cada caractere
print("Contagem de caracteres:", resultado)
