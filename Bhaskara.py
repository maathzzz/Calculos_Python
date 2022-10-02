import math

# ==============================
# Bhaskara!
# ==============================

a = float(input('Digite o "a": '))
b = float(input('Digite o "b": '))
c = float(input('Digite o "c": '))

delta = ((b ** 2) - (4 * a) * c)
raizDelta = math.sqrt(delta)

x1 = ((-b + raizDelta) / (2 * a))
x2 = ((-b - raizDelta) / (2 * a))

if delta <= 0:
    print('Solução inválida; equação não possui raizes reais')
else: 
    print('Os resultados são: {0} e {1}'.format(x1, x2))