'''Faça um programa que peça uma nota, entre zero e dez. Mostre uma mensagem caso o 
valor seja inválido e continue pedindo até que o usuário informe um valor válido. '''

Nota = int(input("Digite a nota do aluno: "))

while (Nota > 10 or Nota < 0):
    print("\nO valor inserido é invalido, por favor digite a nota correta!")
    Nota = int(input("Digite a nota corretamente: "))