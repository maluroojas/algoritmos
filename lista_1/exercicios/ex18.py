def soma_diagonais(matriz):
    soma_principal = 0
    soma_secundaria = 0
    n = len(matriz)

    for i in range(n):
        soma_principal += matriz[i][i]  # Soma da diagonal principal
        soma_secundaria += matriz[i][n - 1 - i]  # Soma da diagonal secundária

    return soma_principal, soma_secundaria

# Entrada direta do usuário
n = int(input("Digite a ordem da matriz quadrada: "))
matriz = []

print("Digite os elementos da matriz, linha por linha:")
for _ in range(n):
    linha = list(map(int, input().split()))
    matriz.append(linha)

# Calcular as somas das diagonais
soma_principal, soma_secundaria = soma_diagonais(matriz)

# Exibir os resultados
print(f"Soma da diagonal principal: {soma_principal}")
print(f"Soma da diagonal secundária: {soma_secundaria}")
