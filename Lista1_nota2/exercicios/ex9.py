def filtrar_tuplas_maior_que_5(tuplas):
    # Usando filter para selecionar tuplas com média maior que 5
    resultado = list(filter(lambda t: sum(t) / len(t) > 5, tuplas))
    
    return resultado

# Testando a função com uma lista de exemplo
tuplas = [(2, 8), (4, 5, 6), (1, 2)]
resultado = filtrar_tuplas_maior_que_5(tuplas)

print(resultado)  
