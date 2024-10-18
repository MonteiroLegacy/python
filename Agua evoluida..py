def calcular_conta(tipo_consumidor, consumo):
    if tipo_consumidor == 'Residencial':
        conta = 5.00 + (0.05 * consumo)
        tipo_consumidor == 'Comercial'
 if consumo <=80:
     conta = 500
 else:
     conta = 800.00 + (0.04 * (consumo - 100))
     return conta
 tipo_consumidor = input("digite o tipo de consumidor")
 consumo = float(input("digite o consumo em metros cubicos"))
 valor_conta = calcular_conta(tipo_consumidor, consumo)
 print (f"o valor da conta de agua e:{valor_conta.2}")
