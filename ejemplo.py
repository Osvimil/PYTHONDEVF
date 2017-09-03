#!/usr/bin/env python
# - * - coding: utf-8 - * -
'''
metro = input("cual es tu edad de nuevo: ")
if(int(metro)<50):
	print("joven")
else:
	print("rucanroll")
'''

'''
edad = int(input("cual es tu edad: "))

if(edad<=12):
	print("ve toy story")
elif(edad>12 and edad<=17):
	print("ve harry poter")
elif(edad>17 and edad<=100):
	print("ve the matrix")
else:
	print("pues no hay peliculas para ti")
	'''

'''
#uso de RANGE
a = range(10)
print (a)
'''

'''
calificaciones = [5,6,3,9,10,6]
#print (len(calificaciones))
for x in calificaciones:
	#print (x)
	#print('HOLA')
	pass

alumnos = ['carmen','cecilia','jorge','beatriz']
for nombre in alumnos:
	print(nombre)

print (range(5))

for numero in range(100):
	print(numero)
'''

'''
cantidad = int(input('hasta donde quieres contar: '))
#print (range(cantidad))

for numero in range(cantidad):
	if(numero%2==0):
		print(numero)
'''

'''
mensaje = 'Vamos a realizar un codigo muy bonito'
print(mensaje)
lista_de_palabras = mensaje.split(' ')
#print(lista_de_palabras)

lista_de_palabras_con_mayusculas = []

for palabra in lista_de_palabras:
	palabra_con_mayuscula = palabra.capitalize()
	#print(palabra_con_mayuscula)
	lista_de_palabras_con_mayusculas.append(palabra_con_mayuscula)
#print(lista_de_palabras_con_mayusculas)

print (' '.join(lista_de_palabras_con_mayusculas))
'''

'''
lista = [1,23,4,5,67,8,9,10]
lista_intermedios = []
lista_extremos = []

lista_extremos.append(lista[0])
lista_extremos.append(lista[len(lista)-1])
print(lista_extremos)

lista_intermedios = lista[1:len(lista)-1]
print(lista_intermedios)
'''


'''
listilla = [1,23,4,5,6,7,8,9,10]
numero = 23
if(numero in listilla):
	print (True)
else:
	print (False)
'''







