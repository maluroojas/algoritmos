def dobrar_lista(numeros):
    # Usamos 'map' para aplicar a função lambda a cada elemento da lista.
    # A função lambda pega cada número 'x' e retorna 'x * 2'.
    return list(map(lambda x: x * 2, numeros))

# Testando a função com uma lista de exemplo
numeros = [1, 2, 3, 4]
resultado = dobrar_lista(numeros)

print(resultado)  
