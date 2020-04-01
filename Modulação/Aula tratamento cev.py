# Erros e exceções
try:
    a = int(input('Numerador: '))
    b = int(input("Denominador :"))
    r = a/b
except (TypeError, ValueError):
    print('\033[0;31mTivemos um erro com os tipos de dados que você digitou.\033[m')
except Exception as erro:
    print(f"O erro foi {erro.__class__}!")
except KeyboardInterrupt:
    print("\033[0;31mO usuário não desejou digitar um número.\033[m")
else:
    print(f"O resultado é {r:.1f}.")
finally:
    print("Volte Sempre!")
