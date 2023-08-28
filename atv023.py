#Faça um programa que leia m número de 0 a 9999 e mostre na tela cada um dos números separados

numero = str(input("Digite um número: "))

print(f'Unidade: {numero[len(numero)-1]}')
    
if(len(numero)-2 >= 0):
    print(f'Dezena: {numero[len(numero)-2]}')

if(len(numero)-3 >= 0 and (int(numero[len(numero)-3]) != 0 and not (int(numero[len(numero)-4]) != 0))):
    print(f'Centena: {numero[len(numero)-3]}')

if(len(numero)-4 >= 0 and int(numero[len(numero)-4]) != 0):
    print(f'Milhar: {numero[len(numero)-4]}')

