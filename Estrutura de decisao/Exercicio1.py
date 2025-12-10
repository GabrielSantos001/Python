#Faça um programa que leia três números e mostre o maior e o menor deles:
    
n1 = int(input("Digite o valor de N1: "))
n2 = int(input("Digite o valor de N2: "))
n3 = int(input("Digite o valor de N3: "))

if (n1 > n2 and n1 > n3):
    print("O maior valor digitado é ", n1, " que representa a variavel n1")
elif (n2 > n1 and n2 > n3):
    print("O maior valor digitado é ", n2, " que representa a variavel n2")
else:
    print("O maior valor digitado é ", n3, " que representa a variavel n3")


if (n1 < n2 and n1 < n3):
    print("O menor valor digitado é ", n1, " que representa a variavel n1")
elif (n2 < n1 and n2 < n3):
    print("O menor valor digitado é ", n2, " que representa a variavel n2")
else:
    print("O menor valor digitado é ", n3, " que representa a variavel n3")
