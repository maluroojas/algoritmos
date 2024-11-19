def primo(numero):
    if numero <= 1:
        return False
    for i in range(2, int(numero**0.5) + 1):  # Verifica divisores até a raiz quadrada do número
        if numero % i == 0:
            return False
    return True

def numeros_primos_intervalo(inicio, fim):
    primos = []
    for num in range(inicio, fim + 1):  # Gera números no intervalo incluindo o fim
        if primo(num):
            primos.append(num)
    return primos

print("🔢 Bem-vindo ao Verificador de Números Primos! 🔢")
print("Descubra todos os números primos dentro de um intervalo informado.\n")

inicio = int(input("Digite o início do intervalo: "))
fim = int(input("Digite o fim do intervalo: "))

primos_no_intervalo = numeros_primos_intervalo(inicio, fim)

if primos_no_intervalo:
    print(f"\n✨ Os números primos entre {inicio} e {fim} são: {primos_no_intervalo}.")
else:
    print(f"\n❌ Não há números primos no intervalo entre {inicio} e {fim}.")

print("\nObrigado por usar o programa! Até breve! 😊")
