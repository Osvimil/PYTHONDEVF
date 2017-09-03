'''
pregunta = int(input("dime tu edad "))
#pregunta2 = input("pon un numero")
print(pregunta)
#print(pregunta2)
operacion = 2017-pregunta+100
print("en el anio {} tendras 100 anios".format(operacion))
'''
question = input("cual es tu edad: ")
question = int(question)
print(question)

if(question>=18 and question<=50):
	print("bienvenido a la fiesta")
elif(question>50 and question<=60):
	print("ensename tu tarjeta del insen")
else:
	print("No. no valido")