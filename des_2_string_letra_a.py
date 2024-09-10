# Solicitando uma string do usuário
texto = input("Digite uma string (NÃO USE CARACTERES ESPECIAS): ")

# Convertendo a string para minúsculas para tratar 'A' e 'a' como iguais e conseguir contar ambos
texto_lower = texto.lower()

# Contando quantas vezes a letra 'a' foi escrita
contagem = texto_lower.count('a')

# Verificando se a letra 'a' está presente e imprimindo a quantidade
if contagem > 0:
    print(f"A letra 'a' aparece {contagem} vez(es) na string.")
else:
    print("A letra 'a' não aparece na string.")
