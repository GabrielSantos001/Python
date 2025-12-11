'''Faça um programa que leia um número e exiba o dia correspondente da semana.
(1-Domingo, 2- Segunda, etc.), se digitar outro valor deve aparecer valor inválido. '''

dia_da_semana = int(input("Digite o dia da semana (1 ao 7): "))

if (dia_da_semana == 1):
    print("Hoje é Domingo!")
elif (dia_da_semana == 2):
    print("Hoje é segunda-feira!")
elif (dia_da_semana == 3):
    print("Hoje é terça-feira!")
elif (dia_da_semana == 4):
    print("Hoje é quarta-feira!")
elif (dia_da_semana == 5):
    print("Hoje é quinta-feira!")
elif (dia_da_semana == 6):
    print("Hoje é sexta-feira!")
elif (dia_da_semana == 7):
    print("Hoje é Sabado!")
else:
    print("Você digitou um número invalido, por favor tente novamente!")
