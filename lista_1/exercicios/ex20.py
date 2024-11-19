def fibonacci(n):
    
    fib_sequence = []  # Lista para armazenar os números da sequência
    
    # Verifica se n é maior que 0
    if n > 0:
        fib_sequence.append(0)  # O primeiro número é 0
    if n > 1:
        fib_sequence.append(1)  # O segundo número é 1
    
    # Calcula os números subsequentes da sequência
    for i in range(2, n):
        next_number = fib_sequence[i-1] + fib_sequence[i-2]
        fib_sequence.append(next_number)
    
    return fib_sequence

# Solicita ao usuário o número de termos da sequência
n = int(input("Digite o número de termos da sequência de Fibonacci que você deseja: "))

# Chama a função e armazena o resultado
resultado = fibonacci(n)

# Exibe a sequência de Fibonacci gerada
print(f"Os primeiros {n} números da sequência de Fibonacci são: {resultado}")
