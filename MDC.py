import math

# ==============================
# Máximo Divisor Comum
# ==============================

num = int(input('Digite dois números para descobrir seu MDC: '))
num2= int(input(''))
mdc = math.gcd(num, num2)

print('O máximo divisor comum entre {0} e {1} é {2}'.format(num, num2, mdc))