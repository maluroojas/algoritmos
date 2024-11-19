def contar_vogais_e_consoantes(frase):
    
    # Definindo as vogais
    vogais = 'aeiouAEIOU'
    
    # Inicializando as contagens
    contagem_vogais = 0
    contagem_consoantes = 0
    
    # Itera sobre cada caractere da frase
    for char in frase:
        # Ignora espaços e caracteres especiais
        if char.isalpha():
            if char in vogais:
                contagem_vogais += 1  # Incrementa se for uma vogal
            else:
                contagem_consoantes += 1  # Incrementa se for uma consoante
    
    return contagem_vogais, contagem_consoantes

# Solicita a frase ao usuário
frase = input("Digite uma frase: ")

# Chama a função para contar as vogais e consoantes
vogais, consoantes = contar_vogais_e_consoantes(frase)

# Exibe os resultados
print(f"Vogais: {vogais}")
print(f"Consoantes: {consoantes}")
