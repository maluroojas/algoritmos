def mesclar_dicionarios(dicionario1, dicionario2):
    # Cria um novo dicionário que será a mesclagem dos dois
    dicionario_mesclado = dicionario1.copy()  # Cria uma cópia do primeiro dicionário
    
    # Percorre o segundo dicionário
    for chave, valor in dicionario2.items():
        if chave in dicionario_mesclado:
            # Se a chave já existe, soma os valores
            dicionario_mesclado[chave] += valor
        else:
            # Se a chave não existe, adiciona ela ao dicionário mesclado
            dicionario_mesclado[chave] = valor
            
    return dicionario_mesclado

# Exemplo de dicionários
dicionario1 = {'a': 5, 'b': 3, 'c': 8}
dicionario2 = {'b': 2, 'c': 7, 'd': 4}

# Chama a função para mesclar os dicionários
resultado = mesclar_dicionarios(dicionario1, dicionario2)

# Exibe o dicionário mesclado
print("Dicionário mesclado:", resultado)
