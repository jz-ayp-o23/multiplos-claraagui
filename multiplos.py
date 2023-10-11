#Múlltiplos

# Entradas
n1 = int(input("Introduzca un número: "))
n2 = int(input("Introduzca otro número: "))
# Proceso
if n1 % n2 == 0:
    print(f"El número {n1} es múltiplo del {n2}")
elif n2 % n1 == 0:
    print(f"El número {n2} es múltiplo del {n1}")
if n2 % n == 1:
    print(f"El número {n2} es múltiplo del {n1}")
else:
    print(f"Ninguno de los números es múltiplo del otro")