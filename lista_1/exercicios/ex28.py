def verificar_sudoku(tabuleiro):
    
    # Verifica cada linha
    for linha in tabuleiro:
        if not verificar_unicidade(linha):
            return False
    
    # Verifica cada coluna
    for col in range(9):
        coluna = [tabuleiro[linha][col] for linha in range(9)]
        if not verificar_unicidade(coluna):
            return False
    
    # Verifica cada subgrade 3x3
    for i in range(0, 9, 3):  # percorre as linhas das subgrades
        for j in range(0, 9, 3):  # percorre as colunas das subgrades
            subgrade = [tabuleiro[x][y] for x in range(i, i + 3) for y in range(j, j + 3)]
            if not verificar_unicidade(subgrade):
                return False

    return True

def verificar_unicidade(lista):
    """
    Verifica se todos os números em uma lista são únicos e estão entre 1 e 9.
    """
    lista_filtrada = [num for num in lista if num != 0]  # Ignora os zeros, que representam espaços vazios
    return len(lista_filtrada) == len(set(lista_filtrada))

# Exemplo de uso com um tabuleiro de Sudoku
tabuleiro_sudoku = [
    [5, 3, 4, 6, 7, 8, 9, 1, 2],
    [6, 7, 2, 1, 9, 5, 3, 4, 8],
    [1, 9, 8, 3, 4, 2, 5, 6, 7],
    [8, 5, 9, 7, 6, 1, 4, 2, 3],
    [4, 2, 6, 8, 5, 3, 7, 9, 1],
    [7, 1, 3, 9, 2, 4, 8, 5, 6],
    [9, 6, 1, 5, 3, 7, 2, 8, 4],
    [2, 8, 7, 4, 1, 9, 6, 3, 5],
    [3, 4, 5, 2, 8, 6, 1, 7, 9]
]

# Verifica se o tabuleiro é válido
if verificar_sudoku(tabuleiro_sudoku):
    print("O tabuleiro de Sudoku é válido!")
else:
    print("O tabuleiro de Sudoku NÃO é válido!")
