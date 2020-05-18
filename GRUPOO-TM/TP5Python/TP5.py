lista=[]
nueva_lista = []
nueva_lista2 = []
num_menor = 0
num_mayor = 0
ingreso_usuario=int(input("Ingrese un numero de 4 digitos:"))
lista.append(ingreso_usuario)

#Array num menor
for i in str(ingreso_usuario):
    nueva_lista.append(i)

#Array Num mayor
for x in str(ingreso_usuario):
    nueva_lista2.append(x)

#Numero menor
for recorrido in range(1,len(nueva_lista)):
   for posicion in range(len(nueva_lista)- recorrido):
       if nueva_lista[posicion]> nueva_lista[posicion  + 1]:
           temp = nueva_lista[posicion]
           nueva_lista[posicion]=nueva_lista[posicion + 1]
           nueva_lista[posicion + 1] = temp

#Numero mayor
for recorrido in range(1,len(nueva_lista)):
   for posicion in range(len(nueva_lista)- recorrido):
       if nueva_lista2[posicion] < nueva_lista2[posicion  + 1]:
           temp = nueva_lista2[posicion]
           nueva_lista2[posicion]= nueva_lista2[posicion + 1]
           nueva_lista2[posicion + 1]=temp
#Numero mayor - menor


num_menor = "".join(nueva_lista)
num_mayor = "".join(nueva_lista2)

print("")
print("Numero menor posible: "+ num_menor)
print("")
print("Numero mayor posible: "+ num_mayor)
print("")
print("La resta de los numeros dan: "+ resta)
