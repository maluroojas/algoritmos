def remover_duplicados(lista_aninhada):
    
    lista_sem_duplicados = []
    
    # Itera sobre cada sublista na lista aninhada
    for sublista in lista_aninhada:
        # Cria uma nova sublista com elementos únicos (usando set) e converte de volta para lista
        sublista_unica = list(set(sublista))
        lista_sem_duplicados.append(sublista_unica)
    
    return lista_sem_duplicados

# Exemplo de uso
lista_aninhada = [
    [1, 2, 3, 3, 4],
    [5, 5, 6, 7, 7],
    [8, 9, 9, 9, 10]
]

# Chama a função para remover os duplicados
resultado = remover_duplicados(lista_aninhada)

# Exibe o resultado
print("Lista sem duplicados:", resultado)
