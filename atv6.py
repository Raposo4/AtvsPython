#Crie um algoritmo que leia um número e mostre o seu dobro, seu triplo e sua raiz quadrada

from cmath import sqrt

number = int(input("Digite um número: "))
print(f"O dobro de {number} vale {number*2}\nO triplo de {number} vale {number*3}\nA raiz quadrada de {number} é igual a {sqrt(number).real:.2f}")