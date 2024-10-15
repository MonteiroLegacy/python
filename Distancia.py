X1 = float(input("Insira x1"))
X2 = float(input("insira x2"))
Y1 = float(input("insira Y1"))
Y2 = float(input("insira Y2"))
import math
def calcular_distancia(X1, Y1, X2, Y2):
  return math.sqrt((X2 - X1)**2 + (Y2 - Y1)**2)
Distancia = calcular_distancia(X1, Y1, X2, Y2)
print("A distância entre os pontos é:", Distancia)