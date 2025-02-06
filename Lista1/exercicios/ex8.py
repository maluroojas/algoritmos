from functools import reduce

from functools import reduce  # Importando o reduce para somar os valores

def contar_total_letras(palavras):
    # Usando map para contar o número de letras em cada palavra
    contagem_letras = list(map(len, palavras))
    
    # Usando reduce para somar o total de letras
    total_letras = reduce(lambda x, y: x + y, contagem_letras)
    
    return total_letras

# Testando a função com uma lista de exemplo
palavras = ["casa", "python", "lambda"]
resultado = contar_total_letras(palavras)

print(resultado)  
