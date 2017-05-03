# -*- coding: utf-8 -*-

archivo = open("nombre.txt", "r")
instrucciones = []
parametros = []

for r in archivo:
	instrucciones.append(r.split()[0])
	parametros.append(r.split()[1])


print (instrucciones)
print (parametros)




texto = ""	