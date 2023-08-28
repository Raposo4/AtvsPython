nome = input("Digite seu nome completo: ").strip()

print("Analisando seu nome...")

print(f"Seu nome em maiúsculas é {nome.upper()}")
print(f"Seu nome em minúsculas é {nome.lower()}")
x = nome.split(" ")
y = nome.replace(" ", "")
print(f"Seu nome completo tem {len(y)} letras")
print(f"Seu primeiro nome é {x[0]} e ele tem {len(x[0])} letras")
