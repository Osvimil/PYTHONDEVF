from random import randint
'''
actores = {
	'orlando x': ['peli 1','peli 2'],
	'chabelo x': ['peli 3','peli 4'],
	'silvia x': ['peli 5','peli 6']
}

#print(actores['silvia x'])

#for actor in actores:
#	print("el actor {} a participado en: {}".format(actor,actores[actor]))

#ACTOR TOMA LAS LLAVES DEL DICCIONARIO
#actores[actor]

print(actores['orlando x'])
print (len(actores))
print(actores.keys())

actores['garcia'] = ['peli 7','peli 8']
print(actores)
actores['garcia'].remove('peli 8')
print(actores)
'''
'''
SE VA ACOMPLETAR CON EL CODIGO QUE ENVIARÁ ELIEL
peliculas = {
	'tristes':{
		'niño': 'viaje de chaquira',
		'joven': 'harry poter',
		'adulto': 'una porno'
	},

	'feliz':{
		'niño': 'bob esponja',
		'joven':'porno2',
		'adulto';'de miedo'
	}
}
'''


'''
def invertir_cadena(frase):
	#print(frase[::-1]) 0
	return frase[::-1] # 1

print(invertir_cadena('Soy oswaldo')) # 1
#invertir_cadena('Soy oswaldo') 0
'''
'''
def palindromo(frase):
	if frase==frase[::-1]: 
		return True
	else:
		return False

print(palindromo('aguacate'))
'''

opciones = ['piedra','papel','tijeras']
maquina = opciones[randint(0,2)]
jugador = False

while jugador == False:
	jugador = input("piedra papel o tijera escoges: ")
	if jugador == maquina:
		print("empate paps")
	elif jugador == "piedra":
		if maquina == "papel":
			print("la maquina gana")
		else:
			print("tu ganaste")
	elif jugador == "papel":
		if maquina == "tijeras":
			print("la maquina gana")
		else:
			print("tu ganas")
	elif jugador == "tijeras":
		if maquina == "piedra":
			print("la maquina gana")
		else:
			print("tu ganaste")
	else:
		print("no pongas otra cosa")










