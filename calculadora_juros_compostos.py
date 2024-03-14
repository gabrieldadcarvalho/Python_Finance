import math

print("O programa calcula os juros compostos.", "\n")

# p = 10000
# n = 12
# r = 8 / 100

p_usuario = input("Valor presente: ")
r_usuario = input("Taxa de juros anual nominal: ")
n_usuario = input("Quantidade de vezes que o juros é capitalizado por ano: ")
t_usuario = input("Número de anos: ")

if p_usuario.isdigit() and r_usuario.isdigit() and n_usuario.isdigit() and t_usuario.isdigit():
    p = float(p_usuario)
    r = float(r_usuario) / 100
    n = float(n_usuario)
    t = float(t_usuario)

    a = p * (1 + r / n) ** (t * n)

    print()

    mensagem = "Total investido: %.2f      \n"
    mensagem += "Total de juros: %.3f       \n"
    mensagem += "Composição do ano: %.1f    \n"
    mensagem += "Total de anos: %d          \n"
    mensagem += "Total ganho em juros: %.2f \n"
    print(mensagem % (p, r, n, t, a))

else:
    print("Um ou mais valores informados são inválidos.")
