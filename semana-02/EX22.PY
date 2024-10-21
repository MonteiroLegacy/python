
horas = int(input("Digite a quantidade de horas que a charrete foi usada: "))
blocos_3_horas = horas // 3
horas_restantes = horas % 3
# Cálculo do valor a pagar
valor_a_pagar = (blocos_3_horas * 10) + (horas_restantes * 5)
print(f"O valor total a pagar é: R$ {valor_a_pagar:.2f}")
