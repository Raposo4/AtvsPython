#Crie um programa que leia o nome da sua cidade e diga se ela começa ou não com o nome "SANTO"

name = str(input("Em que cidade você mora? ")).strip()

name = name.upper()

if(name.find("SANTO") == 0):
    print('True');
else: 
    print('False');
