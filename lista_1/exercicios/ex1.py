def soma_simples(num1, num2):
    
    return num1 + num2

# Mensagem inicial para o usuário
print("=== Bem-vindo à Calculadora de Somas! ===")
print("Digite dois números, e eu calcularei a soma para você.\n")

# Solicitar os números do usuário com mensagens claras
numero1 = float(input("Por favor, insira o primeiro número: "))
numero2 = float(input("Agora, insira o segundo número: "))

# Calcular a soma usando a função `soma_simples`
resultado = soma_simples(numero1, numero2)

# Exibir o resultado formatado de forma amigável
print("\n🎉 Aqui está o resultado!")
print(f"A soma de {numero1} e {numero2} é: {resultado}.")
