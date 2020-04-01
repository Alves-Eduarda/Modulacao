import moeda

num = float(input("Digite um valor : R$  "))
print(f"Aumentando 10%, temos : R$ {moeda.aumentar(num)}")
print(f"Diminuindo 10%, temos: R$ {moeda.diminuir(num)}")
print(f"O dobro de R$ {num} é R$ {moeda.dobro(num)}")
print(f"A metade de R$ {num} é R$ {moeda.metade(num)} ")
