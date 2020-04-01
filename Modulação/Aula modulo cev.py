from Uteis import Numeros
#Programa principal
num = int(input("Digite um valor: "))
fat = Numeros.fatorial(num)
d = Numeros.dobro(num)
t = Numeros.triplo(num)
print(f"O fatorial de {num} é {fat}.")
print(f"O dobro de {num} é {d}.")
print(f"O triplo de {num} é {t}.")
