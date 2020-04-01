def aumentar(n, porcento=10):
    resp = n + ((porcento/100)*n)
    return resp


def diminuir(n, porcento=10):
    resp = n - ((porcento/100)*n)
    return resp


def dobro(n):
    return n *2


def metade(n):
    resp = n/2
    return resp


def moeda(n):
    resp = str(n)

    return resp