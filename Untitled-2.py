#Nombre: ingrese el numero
#Entradas: 
#   empesar con numero negativo ,
#   terminar con numero positivo
#Salidas:
# Dame el resultado y aparte dame un mensaje si el numero negativo es positivo o negativo
#Proceso:
#   pide que los numeros positivos y negativos me den los resultados 

num = float(input("Ingrese un numero"))
if num < 0:
    print(f"El numero {num} es negativo")
else:
    print(f"El numero {num} no es negativo")