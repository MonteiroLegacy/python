Nota = int(input("Digite valor da nota"))
if 9.0 <= Nota <= 10:
    conceito = "A"
elif 7.5 <= Nota <9.0:
    conceito = "B"
elif 6.0 <= Nota < 7.5:
    conceito = "C"
elif 0 <= Nota < 6.0:
    conceito = "D"
else:
    conceito = "Nota inválida"
print ("O conceito da nota e", conceito)