cantidad_invertir = float(input("ingrese la cantidad a invertir: "))
interes_anual = float(input("Ingrese el interes anual (en porcentaje: "))
numeros_años = int(input("ingrese el numero de años de la inversion: "))

tasa_interes = interes_anual / 100

Capital_final = cantidad_invertir * (1 + tasa_interes) ** numeros_años
print(f"El capital obtenido en la inversion en años {numeros_años} año es: {Capital_final:.2f}")
