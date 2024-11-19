def calcular_media(notas):
    return sum(notas) / len(notas)

def notas_maiores_que_media(notas):
    media = calcular_media(notas)
    maiores_que_media = [nota for nota in notas if nota > media]
    return maiores_que_media

print("📊 Bem-vindo ao Verificador de Notas! 📊")
print("Digite as notas dos alunos para calcular a média e as notas acima dela.\n")

notas_usuario = input("Digite as notas dos alunos separadas por espaço: ").split()
notas_usuario = [float(nota) for nota in notas_usuario]

media = calcular_media(notas_usuario)
notas_acima_da_media = notas_maiores_que_media(notas_usuario)

print(f"\n📈 A média das notas é: >>{media:.2f}<<")
print(f"🔝 As notas acima da média são: {notas_acima_da_media}.")

print("\nEspero ter ajudado! Até logo! 😊")
