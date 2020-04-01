def leiaDinheiro(msg):
    ok = False
    while not ok:
        n = str(input(msg)).replace(',','.').strip()
        if n.isalpha() or n == '':
            print("\033[0;31mERRO! Digite um número válido.\033[m")
        else:
            ok = True
            return float(n)


def leiaint(msg):
    ok = False
    valor = 0
    while True:
        n = str(input(msg))
        if n.isnumeric():
            valor= int(n)
            ok = True
        else:
            print("\033[0;31mERRO! Digite um número inteiro válido.\033[m")
        if ok:
            break
    return valor
