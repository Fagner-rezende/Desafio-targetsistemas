# Vamos solicitar o usuário para colocar um número qualquer
n = int(input("Informe um número: "))

# Vamos inicar os dois primeiros números da sequência de Fibonacci
a, b = 0, 1

# Verificando se o número informado pertence à sequência de Fibonacci, o "n" é o número informado pelo usário
while b < n:
    a, b = b, a + b  # Calculando os próximos números da sequência

# Verifica se o número informado pertence à sequência de Fibonacci
if b == n or n == 0:
    print(f"O número {n} pertence à sequência de Fibonacci.")
else:
    print(f"O número {n} NÃO pertence à sequência de Fibonacci.")
