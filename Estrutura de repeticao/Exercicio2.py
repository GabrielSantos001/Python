'''Faça um programa que leia um nome de usuário e a sua senha e não aceite
 a senha igual ao nome do usuário, mostrando uma mensagem de erro e voltando 
 a pedir as informações. '''
 
Nome = str(input("Digite um nome de usuário: "))
Senha = str(input("Digite a senha para o usuário: "))

while (Senha == Nome):
    print("A senha não pode ser igual ao nome de usuario, insira uma senha diferente!")
    Senha = input("Digite a senha: ")