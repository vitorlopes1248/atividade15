# Crie um programa que receba dois números e uma operação (soma, subtração, multiplicação ou divisão) e execute a operação desejada.

num1 = float(input("Digite o numero de sua escolha: "))
num2 = float(input("Digite o segundo numero de sua escolha: "))
escolha=str(input("escolha entre soma, subtração, multiplicação ou divisão: "))

if escolha == "soma":
    print(num1 + num2)

elif escolha == "subtração":
    print(num1 - num2)

elif escolha == "multiplicação":
    print(num1*num2)

elif escolha == "divisão":
    print(num1/num2)
