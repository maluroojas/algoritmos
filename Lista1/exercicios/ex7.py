def agrupar_numeros(numeros):
    # Filtrando os números positivos
    positivos = list(filter(lambda x: x > 0, numeros))
    
    # Filtrando os números negativos
    negativos = list(filter(lambda x: x < 0, numeros))
    
    # Filtrando os zeros
    zeros = list(filter(lambda x: x == 0, numeros))
    
    # Retornando o dicionário com as categorias
    return {
        "positivos": positivos,
        "negativos": negativos,
        "zeros": zeros
    }

# Testando a função com uma lista de exemplo
numeros = [1, -2, 0, 3, -5, 0]
resultado = agrupar_numeros(numeros)

print(resultado)  
