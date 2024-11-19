def calcular_media(nota1, nota2, nota3):
    media = (nota1 + nota2 + nota3) / 3
    return media

print("🎓 Bem-vindo ao Calculador de Média! 🎓")
print("Informe as três notas para calcular a média.\n")

nota1 = float(input("Digite a primeira nota: "))
nota2 = float(input("Digite a segunda nota: "))
nota3 = float(input("Digite a terceira nota: "))

media = calcular_media(nota1, nota2, nota3)

print(f"\n📊 A média das notas {nota1}, {nota2} e {nota3}3
    é: >>{media:.2f}<<.")
print("\nObrigado por usar o programa! Sucesso nos estudos! 😊")

