def filtrar_pares(numeros):
    # Usamos 'filter' para aplicar a função lambda e filtrar apenas os números pares.
    # A função lambda verifica se o número é par: (x % 2 == 0).
    return list(filter(lambda x: x % 2 == 0, numeros))

# Testando a função com uma lista de exemplo
numeros = [1, 2, 3, 4, 5]
resultado = filtrar_pares(numeros)

print(resultado) 
