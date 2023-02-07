#Faça um programa que leia um valor em metros e o exiba convertido em centímetros e milímetros

dist = float(input("Digite um distância em metros: "))
print(f"A medida de 3.0m corresponde a: ")
print(f"{dist/1000}km")
print(f"{dist/100}hm")
print(f"{dist/10}dam")
print(f"{dist*10:.0f}dm")
print(f"{dist*100:.0f}cm")
print(f"{dist*1000:.0f}mm")
