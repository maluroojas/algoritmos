def palavras_mais_frequentes(texto, top_n=5):
    # Transformar o texto em minúsculas e dividir em palavras
    palavras = texto.lower().split()
    # Lista para armazenar pares (palavra, frequência)
    frequencias = []
    
    # Iterar pelas palavras únicas
    palavras_unicas = set(palavras)  # Conjunto para evitar repetição
    for palavra in palavras_unicas:
        frequencias.append((palavra, palavras.count(palavra)))  # Adicionar contagem
    
    # Ordenar as palavras por frequência, em ordem decrescente
    palavras_ordenadas = sorted(frequencias, key=lambda x: x[1], reverse=True)
    
    # Retornar as `top_n` palavras mais frequentes
    return palavras_ordenadas[:top_n]

# Solicitar o texto do usuário
texto = input("Digite um texto longo: ")

# Obter as 5 palavras mais frequentes
resultado = palavras_mais_frequentes(texto)

# Exibir o resultado
print("\nAs 5 palavras mais frequentes são:")
for palavra, frequencia in resultado:
    print(f"'{palavra}': {frequencia} vezes")
