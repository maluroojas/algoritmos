def calculadora_basica():
    # Solicita os números e a operação ao usuário
    num1 = float(input("Digite o primeiro número: "))
    num2 = float(input("Digite o segundo número: "))
    
    # Solicita a operação desejada
    operacao = input("Escolha a operação (adição, subtração, multiplicação, divisão): ").lower()

    # Executa a operação escolhida
    if operacao == "adição":
        resultado = num1 + num2
    elif operacao == "subtração":
        resultado = num1 - num2
    elif operacao == "multiplicação":
        resultado = num1 * num2
    elif operacao == "divisão":
        if num2 != 0:
            resultado = num1 / num2
        else:
            resultado = "Erro: Divisão por zero não é permitida."
    else:
        resultado = "Operação inválida. Escolha uma operação válida."

    # Exibe o resultado
    print(f"O resultado da {operacao} entre {num1} e {num2} é: {resultado}")

# Chama a função da calculadora
calculadora_basica()
