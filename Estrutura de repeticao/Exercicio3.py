'''Faça um programa que leia e valide as seguintes informações:

Nome: maior que 3 caracteres;
Idade: entre 0 e 150;
Salário: maior que zero;
Estado Civil: 's', 'c', 'v', 'd';  '''

Nome = str(input("Digite o seu nome: "))
Idade = int(input("Digite a sua idade: "))
Salario = float(input("Digite o seu salário: "))
Estado_Civil = str(input("Qual seu estado civil (solteiro(a), casado(a), viuvo(a), divorciado(a): "))

#Validação do nome
while len(Nome) <= 3:
    print("\nO nome deve conter mais de 3 caracteres:")
    Nome = str(input("Digite o seu nome: "))
    
#Validação da idade    
while Idade < 0 or Idade > 150:
    print("\nVocê digitou uma idade falsa, por favor insira a sua idade verdadeira!")
    Idade = int(input("Digite a sua idade: "))

#Validação do salário
while Salario < 0.0:
    print("\nVocê digitou um salário invalido, por favor insira um valor valido!")
    Salario = float(input("Digite o seu salário: "))
    
#Validação do estado civil
while Estado_Civil not in ["s", "c", "v", "d"]:
          print("\nVocê digitou um caractere invalido, por favor insira um caracter valido\
                correspondente ao seu estado civil!")
          Estado_Civil = str(input("Digite o seu estado civil (s, c, v, d): "))
          
          
print("\n=== Dados Validados com sucesso ===")
print(f"Nome: {Nome}")
print(f"Idade: {Idade}")
print(f"Salário: {Salario}")
print(f"Estado Civil: {Estado_Civil}") 
