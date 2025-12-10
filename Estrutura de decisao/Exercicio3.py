#Faça um programa que leia três números e mostre-os em ordem decrescente:
    
N1 = int(input("Digite o primeiro valor: "))
N2 = int(input("Digite o segundo valor: "))
N3 = int(input("Digite o terceiro valor: "))

if (N1 > N2 and N2 > N3):
    print("Ordem Decrescente: N1, N2, N3 = ", N1, " - ", N2, " - ", N3)
elif (N1 > N3 and N3 > N2):
    print("Ordem Decrescente: N1, N3, N2 = ", N1, " - ", N3, " - ", N2)
elif (N2 > N1 and N1 > N3):
    print("Ordem Decrescente: N2, N1, N3 = ", N2, " - ", N1, " - ", N3)
elif (N2 > N3 and N3 > N1):
    print("Ordem Decrescente: N2, N3, N1 = ", N2, " - ", N3, " - ", N1)
elif(N3 > N1 and N1 > N2):
    print("Ordem Decrescente: N3, N1, N2 = ", N3, " - ", N1, " - ", N2)
else:
    print("Ordem Decrescente: N3, N2, N1 = ", N3, " - ", N2, " - ", N1)