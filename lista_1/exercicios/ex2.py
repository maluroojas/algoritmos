def par_ou_impar(numero):
    
    # Verifica o resto da divisão por 2 para determinar se o número é par ou ímpar
    if numero % 2 == 0:
        print(f"✅ O número {numero} é >>par<<.")
    else:
        print(f"✅ O número {numero} é >>ímpar<<.")

# Mensagem inicial para orientar o usuário
print("=== Verificador de Par ou Ímpar ===")
print("Informe um número inteiro e eu direi se ele é par ou ímpar.\n")

# Solicita um número inteiro ao usuário com uma mensagem clara
valor = int(input("Por favor, insira um número inteiro: "))

# Chama a função para realizar a verificação
print("\nAnalisando o número...")
par_ou_impar(valor)

# Mensagem final de agradecimento
print("Espero que tenha ajudado :) Até logo!")
