def verificar_numero(numero):
    if numero > 0:
        return "O número é positivo."
    elif numero < 0:
        return "O número é negativo."
    else:
        return "O número é zero."

numero = float(input("Digite um número: "))

mensagem = verificar_numero(numero)
print(f"{mensagem}")