Valor= float(input("Digite um valor em reais: "))
notasde100 = Valor // 100
notasde50 = (Valor % 100) // 50
notasde10 = ((Valor % 100) % 50) // 10
moeda1 = ((((Valor % 100) % 50) % 20) % 10) // 1
print("Notas de 100:", notasde100)
print("Notas de 50:", notasde50)
print("Notas de 10:", notasde10)
print("Moedas de 1:", moeda1)