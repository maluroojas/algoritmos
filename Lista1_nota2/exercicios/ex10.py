from functools import reduce 

def calcular_media_ponderada(alunos):
    resultado = {} 
    
    for aluno, notas in alunos.items():
        peso = notas[-1]  # O último valor da lista é o peso
        notas_sem_peso = notas[:-1]  # Pegamos todas as notas, exceto o peso
        
        # Multiplicamos cada nota pelo peso
        soma_ponderada = reduce(lambda acc, nota: acc + (nota * peso), notas_sem_peso, 0)
        
        # Calculamos a média ponderada dividindo pela soma dos pesos
        media = soma_ponderada / (len(notas_sem_peso) * peso)
        
        # Adicionamos ao dicionário de resultados
        resultado[aluno] = media
    
    return resultado

# Testando a função
alunos = {
    "João": [8, 7, 9, 2],  # Notas: 8, 7, 9; Peso: 2
    "Ana": [5, 6, 7, 3]  # Notas: 5, 6, 7; Peso: 3
}

resultado = calcular_media_ponderada(alunos)
print(resultado)  

