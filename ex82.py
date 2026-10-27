
print("um programa que recebe 11 valores e apresenta eles com um separador")

valores = [0] * 11

for i in range(len(valores)):
    valor = int(input(f"digite o {i + 1}º valor: "))
    valores[i] = valor

print("Os valores digitados são:")

for i in range(len(valores)):
    print(valores[i])
    print("----------------")
