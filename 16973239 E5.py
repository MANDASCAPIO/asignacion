numero1_str = input("Ingresa el primer número entero: ")
numero2_str = input("Ingresa el segundo número entero: ")
numero3_str = input("Ingresa el tercer número entero: ")
numero4_str = input("Ingresa el cuarto número entero: ")

numero1 = int(numero1_str)
numero2 = int(numero2_str)
numero3 = int(numero3_str)
numero4 = int(numero4_str)

mayor = numero1 

if numero2 > mayor:
    mayor = numero2
if numero3 > mayor:
    mayor = numero3
if numero4 > mayor:
    mayor = numero4

    print("El número mayor es:", mayor)

  
