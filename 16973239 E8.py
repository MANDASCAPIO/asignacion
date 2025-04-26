peso_Kg = float(input("ingrese su peso en kilogramos (Kg):  "))
estatura_metros = float(input("ingrese su estatura en metros (mts): "))

if estatura_metros <=0:
  print("la estatura debe ser un valor positivo.")

imc = peso_Kg / (estatura_metros **2)
imc_redondeado = round(imc, 2)
print(f"tu indice de masa corporal es {imc_redondeado}")
