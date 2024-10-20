Numero = int(input("coloque um numero"))
def inverter_numero (Numero):
    Numero_invertido = int(str(Numero)[::-1])
    return Numero_invertido
print ("Numero invertido", inverter_numero(Numero))