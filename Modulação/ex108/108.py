import moeda

num = float(input("Digite um valor : R$  "))
print(f"Aumentando 10%, temos : {moeda.moeda(moeda.aumentar(num))}")
print(f"Diminuindo 10%, temos: {moeda.moeda(moeda.diminuir(num))}")
print(f"O dobro de {moeda.moeda(num)} é {moeda.moeda(moeda.dobro(num))}")
print(f"A metade de {moeda.moeda(num)} é R$ {moeda.moeda(moeda.metade(num))} ")
