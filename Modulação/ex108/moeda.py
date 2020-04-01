def aumentar(n=0, porcento=10):
    resp = n + ((porcento/100)*n)
    return resp


def diminuir(n=0, porcento=10):
    resp = n - ((porcento/100)*n)
    return resp


def dobro(n=0):
    return n *2


def metade(n = 0):
    resp = n/2
    return resp


def moeda(n= 0, moeda= 'R$'):
    return f'{moeda}{n:.2f}'.replace('.',',')
