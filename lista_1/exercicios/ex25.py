def filtrar_pares(numeros):
    pares = []  # Lista para armazenar os números pares
    for num in numeros:
        if num % 2 == 0:  # Verifica se o número é par
            pares.append(num)  # Adiciona o número par à lista
    return pares

# Solicitando a entrada do usuário
print("Digite os números inteiros um por um. Digite 'fim' para terminar:")
numeros = []  # Lista para armazenar os números

while True:
    entrada = input("Número: ")
    if entrada.lower() == 'fim':  # Condição de parada?
        break
    try:
        numeros.append(int(entrada))  # Converte em inteiro e adiciona à lista
    except ValueError:
        print("Por favor, digite um número inteiro válido ou 'fim' para encerrar.")

# Chamando a função para filtrar os pares
pares = filtrar_pares(numeros)

# Exibindo o resultado
print("Números pares:", pares)
