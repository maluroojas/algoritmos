def separar_pares_impares(numeros):
    # Filtra os números pares
    pares = list(filter(lambda x: x % 2 == 0, numeros))
    
    # Filtra os números ímpares
    impares = list(filter(lambda x: x % 2 != 0, numeros))
    
    # Retorna o dicionário com os resultados
    return {"pares": pares, "ímpares": impares}

# Testando a função com uma lista de exemplo
numeros = [1, 2, 3, 4, 5, 6]
resultado = separar_pares_impares(numeros)

print(resultado)  