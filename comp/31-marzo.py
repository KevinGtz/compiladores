texto = []
texto.append("var string inicio")
texto.append("var int fin")
texto.append("var string nombre")

listaVar = []

for c in texto:
	instruccion =  c.split()
	if instruccion[0] == "var":
		tipo = instruccion[1]
		nombreVar = instruccion[2]
		i = []
		i.append(tipo)
		i.append(nombreVar)
		i.append("0")
		repetido = False
		for e in listaVar:
			if nombreVar == e[1]:
				repetido = True
		if not(repetido):
			listaVar.append(i)
		else:
			print("Error" + nombreVar + "redeclarada")
		listaVar.append(i)
print("\t\tnombre \t\ttipo")
for c in listaVar:
	print ("\t\t"+c[1]+"\t\t"+c[0])

