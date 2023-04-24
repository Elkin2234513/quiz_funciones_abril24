#Construir una función que reciba un valor entero como parámetro y que determine si su último dígito es 4.

#Definición de la función

def calcular(n):
     if n % 10 == 4:
          print("Su ultimo digito SI es 4")
     else:
          print("Su ultimo digito NO es 4")
    
#Entrada

n = int(input("DIGITE UN NUMERO: "))

#Procesamiento

calcular(n)








