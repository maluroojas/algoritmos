def nomes_maiores_que_cinco(nomes):
    # Usamos 'filter' com lambda para pegar nomes com mais de 5 letras.
    return list(filter(lambda nome: len(nome) > 5, nomes))

# Testando a função com uma lista de exemplo
nomes = ["Ana", "Lucas", "Fernanda", "João"]
resultado = nomes_maiores_que_cinco(nomes)

print(resultado)  
