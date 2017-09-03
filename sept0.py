
'''
import random
def funcion():
	opciones = ['piedra','papel','tijera']
	datos = {
		'piedra':{
			'papel':'gana pc',
			'tijera':'gana usuario' 
		},
		'papel':{
			'tijera':'gana pc',
			'piedra':'gana usuario'
		},
		'tijera':{
			'piedra':'gana pc',
			'papel':'gana usuario'
		}
	}
	userChoice = input('elige entre piedra, papel, tijera: ')
	pcChoice = random.choice(opciones)
	print("el usuario eligio {} y la pc elijio {}".format(userChoice,pcChoice))
	if(userChoice == pcChoice): return 'Empate'
	return datos[userChoice][pcChoice]
print(funcion())
'''
'''
#PALINDROMO
def palindromo(frase):
	if(frase == frase[::-1]):
		return True
	else:
		return False
print(palindromo('cosasdelavida'))
'''

'''
def invertir_cadena(texto):
	return texto[::-1]
print(invertir_cadena('ATEB SERVICIOS'))
'''

'''
def inversion(txt):
	print(txt[::-1])

inversion('coca cola')

'''
'''
edad = int(input('cual es tu edad'))
preferencia = input('Prefieres algo triste o feliz')

peliculas = {
	'triste':{
		'niño': 'toy story',
		'joven': 'la dama de negro',
		'adulto': 'la risa en vacaciones'
	},
	'feliz':{
		'niño': 'pelicula feliz niño',
		'joven': 'pelicual feliz joven',
		'adulto': 'pelicual feliz adulto'
	}
}
if(preferencia == 'triste'):
	catalogo = peliculas['triste']
	if(edad<=12):
		print('te recomiendo ver: {} '.format(catalogo['niño']))
	elif(edad>12 and edad<=17):
		print('te recomiendo ver: {} '.format(catalogo['joven']))
	elif(edad>17 and edad<=100):
		print('te recomiendo ver: {}'.format(catalogo['adulto']))
if(preferencia == 'feliz'):
	catalogo = peliculas['feliz']
	if(edad<=12):
		print('ok, feliz, te toca ver: {} '.format(catalogo['niño']))
	elif(edad>12 and edad<=17):
		print('va, feliz, ve: {} '.format(catalogo['joven']))
	elif(edad >17 and edad<=100):
		print('entendido, ve: {} '.format(catalogo['adulto']))				
'''

'''
from random import randint

#creamos una lista de opciones
opciones = ['piedra','papel','tijera']
#asignamos una opcion aleatoria a la PC
computadora = opciones[randint(0,2)]
#poner al jugador como false
jugador = False


while jugador == False: 
	jugador = input("ESCOGE ENTRE PIEDRA, PAPEL O TIJERA: ")
	if(jugador == computadora):
		print("EMPATARON ENTRE LOS DOS")
	elif(jugador == "piedra"):
		if(computadora == 'papel'):
			print("LA PC TE GANO")
		else:
			print("TU LE GANASTE A LA MAQUINA")
	elif(jugador == 'papel'):
		if(computadora == 'tijeras'):
			print("PIERDES, LA PC GANO")
		else:
			print("TU GANASTE")	
	elif(jugador == 'tijera'):
		if(computadora == 'piedra'):
			print("LA MAQUINA TE GANO")
		else:
			print("TU LE GANAS HA")
	else:
		print("OPCION NO VALIDA")
	jugador = False 
	computadora = opciones[randint(0,2)]
'''

'''
lista_numeros = [5,10,15,20,25]
resultado = 30 in lista_numeros
resultado1 = 10 in lista_numeros
print(resultado)
print(resultado1)
'''

'''
lista_de_cintas = ['roja','negra','blanca']
nombres = input('escribe tu cinta en DEVF: ')
if(nombres in lista_de_cintas):
	print('si conoces DEVF y tu cinta')
else:
	print('te equivocaste de color yo creo')

'''
'''
#ESCRIBIR UN PROGRAMA QUE REGRESE UNA LISTA QUE CONTENGA
# QUE SON COMUNES ENTRE LAS DOS LISTAS

lista1 = [0,56,33,11,47]
lista2 = [55,11,0,48,79]
resultado = [valor for valor in set(lista1) if valor in set(lista2)]
print (resultado)
'''
#ESCRIBIR UN PROGRAMA QUE DIGA SI la palabra es palindromo

def prueba(frase):
	if frase == frase[::-1]:
		return print('la palabra {} es palindromo'.format(frase))  
	else:
		return print('la palabra {} no es palindromo'.format(frase))

print(prueba('chia'))
print(prueba('sometemos'))
print(prueba('gato'))
print(prueba('rallar'))















