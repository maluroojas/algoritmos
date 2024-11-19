def verificar_maioridade(idade):
    if idade >= 18:
        return "maior de idade"
    else:
        return "menor de idade"

print("👋 Olá! Vamos verificar sua maioridade. 🎉\n")

nome_usuario = input("Qual é o seu nome? ")

idade_usuario = input(f"{nome_usuario}, por favor, digite sua idade: ")

if idade_usuario.isdigit():
    idade_usuario = int(idade_usuario)
    if idade_usuario < 0:
        print("\n❌ A idade não pode ser negativa. Tente novamente com um valor válido!")
    else:
        resultado = verificar_maioridade(idade_usuario)
        print(f"\n✨ {nome_usuario}, você tem {idade_usuario} anos e é >>{resultado}<<.")
else:
    print("\n❌ O valor digitado não é válido. Certifique-se de informar um número inteiro.")

print("\nObrigado por usar o verificador! Até breve! 😊")

