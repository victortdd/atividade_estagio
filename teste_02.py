def pertence_fibonacci(num):
    a, b = 0, 1
    if num == 0 or num == 1:
        return True

    while b <= num:
        if b == num:
            return True
        a, b = b, a + b
    return False


numero = int(input("Informe um numero para verificar se pertence a sequencia de Fibonacci: "))
if pertence_fibonacci(numero):
    print(f"O numero {numero} pertence a sequencia de Fibonacci.")
else:
    print(f"O numero {numero} nao pertence a sequencia de Fibonacci.")