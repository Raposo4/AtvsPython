#Faça um programa que leia o comprimento do cateto oposto e do adjascente de um triângulo retângulo, calcule e mostre sua hipotenusa 

from math import sqrt

op = float(input('Digite o comprimento do cateato oposto: '))
ad = float(input('Digite o comprimento do cateato adjascente: '))

print(f"O valor da hipotenusa é de {sqrt((op**2)+(ad**2))}")