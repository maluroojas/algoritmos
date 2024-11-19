def verificar_anagrama(palavra1, palavra2):
    
    # Remove espaços e coloca as palavras em minúsculas para garantir a comparação correta
    palavra1 = palavra1.replace(" ", "").lower()
    palavra2 = palavra2.replace(" ", "").lower()

    # Ordena as letras das palavras e compara
    if sorted(palavra1) == sorted(palavra2):
        return True
    else:
        return False

# Solicita as duas palavras do usuário
palavra1 = input("Digite a primeira palavra: ")
palavra2 = input("Digite a segunda palavra: ")

# Verifica se são anagramas e exibe o resultado
if verificar_anagrama(palavra1, palavra2):
    print(f"As palavras '{palavra1}' e '{palavra2}' são anagramas.")
else:
    print(f"As palavras '{palavra1}' e '{palavra2}' NÃO são anagramas.")
