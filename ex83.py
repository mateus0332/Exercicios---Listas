
print("um programa que recebe 18 números inteiros e apresenta em ordem inversa")

valores = [0] * 18

for i in range(len(valores)):
    valor = int(input(f"Digite o {i + 1}º valor: "))
    valores[i] = valor

valores.reverse()

print("os valores em ordem inversa sao:")

for i in range(len(valores)):
    print(valores[i])
