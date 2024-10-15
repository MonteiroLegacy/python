import math
Peso = float(input("Peso em toneladas do avião"))
Aceleração = float(input("Aceleração do avião"))
Tempo = float(input("Tempo em segundos gasto na decolagem"))
Velocidade = Aceleração * Tempo
Peso_kg = Peso * 1000
Deslocamento = (1/2) * Aceleração * Tempo**2
Força = Peso_kg * Aceleração
print ("Os resultados são respectivamente",Velocidade, Força, Deslocamento)