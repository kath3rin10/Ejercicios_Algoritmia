#Nombre: ingrese un año
#Entradas: 
#   los meses del año
#   el año
#Salidas:
#   indicame cuando el año sea bisiesto y dame un alerta 
#Proceso:
#   Pide que el año este vien con festivos y dias 
año = int(input("Ingrese un año: "))
if (año % 4 == 0 and año % 100 != 0) or (año % 400 == 0):
    print(f"El año {año} es bisiesto")
else:
    print(f"El año {año} no es bisiesto")