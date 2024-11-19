def ordenar(numeros):
    # Inicializar duas listas para negativos e positivos
    ordenados = []
    # Adicionar os números negativos primeiro
    for num in numeros:
        if num < 0:
            ordenados.append(num)
    # Adicionar os números positivos em seguida
    for num in numeros:
        if num >= 0:
            ordenados.append(num)
    return ordenados

# Solicitando entrada do usuário
entrada = input("Digite uma lista de números inteiros separados por espaço: ")
# Convertendo a entrada para uma lista de inteiros
numeros = list(map(int, entrada.split()))

# Chamando a função e exibindo o resultado
resultado = ordenar(numeros)
print("Lista ordenada:", resultado)


