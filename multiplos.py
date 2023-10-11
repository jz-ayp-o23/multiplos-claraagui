#Múlltiplos

# Entradas
n1 = int(input("Introduzca un número: "))
n2 = int(input("Introduzca otro número: "))

# Proceso
if n1 % n2 == 0:
    print(f"El número {n1} es múltiplo del {n2}")
else:
    print(f"Ninguno de los números es múltiplo del otro")