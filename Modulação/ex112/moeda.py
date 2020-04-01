def aumentar(n=0, porcento=0, formato=False):
    """
    ==> Função utilizada para aumentar em porcentagem um valor
    :param n: valor que será realizado a operação de aumento
    :param porcento: valor que será retirado o percentual
    :param formato: parâmetro opcional que indica a presença ou não da formatação
    :return: retorna o valor com o aumento percentual
    """
    resp = n + ((porcento/100)*n)
    return resp if formato is False else moeda(resp)


def diminuir(n=0, porcento=0, formato=False):
    resp = n - ((porcento/100)*n)
    return resp if formato is False else moeda(resp)


def dobro(n=0, formato=False):
    resp = n*2
    return resp if not formato else moeda(resp)


def metade(n = 0, formato=False):
    resp = n/2
    return resp if not formato else moeda(resp)


def moeda(n= 0, moeda='R$'):
    return f'{moeda}{n:.2f}'.replace('.',',')

def titulo(msg):
    t = len(msg) + 20
    print("~"*t)
    print(f"{msg:^{t}}")
    print("~"*t)

def resumo(n=0,taxaa=10,taxar=5):
    print("~"*30)
    #O center() deixa a string centrada
    print("RESUMO DO VALOR".center(30))
    print("~"*30)
    #O \t deixa os valores tabulados
    print(f'{"Preço analisado:"}\t{moeda(n)}')
    print(f"{'Dobro do preço: '}\t{dobro(n,True)}")
    print(f'{"Metade do preço: "}\t{metade(n,True)}')
    print(f'{f"{taxaa}% de aumento: "}\t{aumentar(n,taxaa,True)}')
    print(f'{f"{taxar}% de redução: "}\t\t{diminuir(n,taxar,True)}')
    print("~"*30)
