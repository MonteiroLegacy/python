
while(True):
    try:
        CustodeFabrica = float(input("digite o custo de fabrica"))
        break
    except ValueError:
        print("Digite um valor valido")



PorcentagemDistribuidor= float(input("digite a porcentagem do distribuidor"))
PorcentagemImpostos= float(input("digite a porcentagem dos impostos"))
CustoConsumidor= CustodeFabrica + (CustodeFabrica * PorcentagemDistribuidor / 100) + (CustodeFabrica * PorcentagemImpostos / 100)
print("O custo do consumidor e:", CustoConsumidor)