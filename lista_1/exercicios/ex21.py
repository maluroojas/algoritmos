def remover_duplicados(lista):
    
    lista_sem_duplicados = []  # Lista para armazenar os elementos sem duplicados
    
    for item in lista:
        if item not in lista_sem_duplicados:  # Verifica se o item já foi adicionado
            lista_sem_duplicados.append(item)  # Adiciona o item à lista
    
    return lista_sem_duplicados

# Solicita ao usuário para inserir uma lista de inteiros
entrada = input("Digite uma lista de inteiros separados por espaço: ")
lista = [int(x) for x in entrada.split()]  # Converte a entrada para uma lista de inteiros

# Chama a função para remover os duplicados
resultado = remover_duplicados(lista)

# Exibe a lista sem duplicados
print(f"Lista sem duplicados: {resultado}")
