def Sistema_Ano_Bissexto(ano):
    # Se o ano for menor que 1582, ele não é bissexto
    if ano < 1582:
        return False
    # Se o ano for múltiplo de 4, verificar as demais condições
    if ano % 4 == 0:
        # Anos múltiplos de 100 só são bissextos se também forem múltiplos de 400
        if ano % 100 == 0 and ano % 400 != 0:
            return False
        else:
            return True
    else:
        return False

# Lê o ano e o converte para inteiro
ano = int(input("Colocar ano: "))

# Chama a função e imprime se é bissexto ou não
if Sistema_Ano_Bissexto(ano):
    print(f"O ano {ano} é bissexto.")
else:
    print(f"O ano {ano} não é bissexto.")


