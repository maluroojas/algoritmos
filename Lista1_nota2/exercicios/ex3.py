from functools import reduce

from functools import reduce

def somar_lista(numeros):
    # 'reduce' aplica a função lambda acumulando a soma de todos os números.
    # A função lambda recebe dois números e retorna a soma deles.
    return reduce(lambda x, y: x + y, numeros)

# Testando a função com uma lista de exemplo
numeros = [1, 2, 3, 4]
resultado = somar_lista(numeros)

print(resultado) 

