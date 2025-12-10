'''Faça um programa que pergunte o preço de três produtos e informe qual
produto você deve comprar, sabendo que a decisão é sempre pelo mais barato: '''

prod1 = float(input("Digite o valor do primeiro produto "))
prod2 = float(input("Digite o valor do segundo produto: "))
prod3 = float(input("Digite o valor do terceiro produto: "))

if (prod1 < prod2 and prod1 < prod3):
    print("O produto mais barato é o prod1, que custa R$", prod1)
elif (prod2 < prod1 and prod2 < prod3):
    print("O produto mais barato é o prod2, que custa R$", prod2)
else:
    print("O produto mais barato é o prod3, que custa R$", prod3)