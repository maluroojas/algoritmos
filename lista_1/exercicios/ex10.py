def calcular_area_retangulo(base, altura):
    area = base * altura  # Calcula a área do retângulo
    return area

print("📐 Bem-vindo ao Calculador de Área do Retângulo! 📐")
print("Informe a base e a altura para calcular a área.\n")

base = float(input("Digite o valor da base do retângulo: "))
altura = float(input("Digite o valor da altura do retângulo: "))

area = calcular_area_retangulo(base, altura)

print(f"\n✅ A área do retângulo é >>{area}<< unidades quadradas.")
print("\nEspero ter ajudado! Até a próxima! 😊")
