# Standardwerte von Parametern
def fmac(a=1.0, b=2.0, c=3.0):
    result = a * b + c
    return result

result_1 = fmac(4.0, 5.0)
print(result_1)

result_2 = fmac(b=4.0, c=5.0)
result_3 = fmac(c=6.0)
result_4 = fmac()
print(result_2, result_3, result_4)

# Rückgabewert ohne return in einer Funktion

def fun():
    print('fun')
