
print("um programa que recebe 12 numeros inteiros e apresenta os pares e os impares")

valores = [0] * 12

for i in range(len(valores)):
    valor = int(input(f"Digite o {i + 1}º valor: "))
    valores[i] = valor


print("os numeros pares são:")

for i in range(len(valores)):
    if valores[i] % 2 == 0:
        print(valores[i])


print("os numeros impares são:")

for i in range(len(valores)):
    if valores[i] % 2 != 0:
        print(valores[i])
