def celsius_para_fahrenheit(celsius):
    
    fahrenheit = celsius * 1.8 + 32  # Aplica a fórmula de conversão
    return fahrenheit

# Saudação e explicação inicial
print("=== Conversor de Temperatura: Celsius para Fahrenheit ===")
print("Este programa converte a temperatura informada em Celsius para Fahrenheit.\n")

# Solicita a temperatura em Celsius ao usuário
celsius = float(input("Por favor, informe a temperatura em graus Celsius: "))

# Converte a temperatura e exibe o resultado de forma formatada
fahrenheit = celsius_para_fahrenheit(celsius)
print(f"\n🌡️  {celsius}°C equivalem a **{fahrenheit:.2f}°F**.\n")

# Agradecimento 
print("Realize outra conversão ou saia do programa. Volte sempre! :)")
