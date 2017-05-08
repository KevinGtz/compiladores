# # este es un comentario
# #lista=[], crea un arreglo
#
# lista = ["hola", 8, 3.25, True]
#
# for e in lista: #este es como un for each
#     print (e)
#
# lista[2] = "algo"
#
# # este print hace que se imprima segun el indice
# print (lista[0:-4])
# print (lista[0:-3])
# print (lista[0:-2])
# print (lista[0:-1])
#
# #.index busca un "elemento" en un arreglo
# print(lista.index("algo"))
#
# #.count cuenta el numero de elementos encontrados en un arreglo
# print(lista.count("hola"))
#
# #.append agrega un elemento
# lista.append("hola")
#
# # in, busca un elemeto en la lista, devuelve TRUE or FALSE
# print ("hola" in lista)

#archivo=open("uno.txt","w") #abre archivo y metodos: "a" agrega, "r" lee, "w" escribe

#archivo.write(" alguna cosa \n") #.write escribe sobre el archivo

#archivo.write("otra cosa")

print ("\n\n")

archivo= open("uno.txt","r") #abre archivo y se le indica el metodo de archivo
texto = archivo.read()#.read lee el archivo
print(texto)

archivo.close() #.close() cierra el archivo

texto_2 = " "
estado = "z"

for c in texto:
    if (estado == "z"):
        if (c == "/"):
            estado = "a"
        else:
            texto_2 = texto_2 + c
    elif (estado == "a"):
        if (c == "*"):
            estado = "b"
        else:
            texto_2 = texto_2 + "/" + c
    elif (estado == "b"):
        if (c == "*"):
            estado = "c"
    elif (estado == "c"):
        if (c == "/"):
            estado = "z"
        elif(c != "*"):
            estado = "b"
print texto_2
