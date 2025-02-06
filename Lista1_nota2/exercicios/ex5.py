def quadrado_ordenado(numeros):
    # Primeiro, usamos 'map' para elevar cada número ao quadrado.
    # Depois, usamos 'sorted' para ordenar a lista.
    return sorted(map(lambda x: x ** 2, numeros))

# Testando a função com uma lista de exemplo
numeros = [3, 1, 4, 2]
resultado = quadrado_ordenado(numeros)

print(resultado)  
