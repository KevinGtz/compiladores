# -*- coding: utf-8 -*-

from funtions import *

print ("\n\n")

archivo= open("uno.txt","r") #abre archivo y se le indica el metodo de archivo
texto = archivo.read()#.read lee el archivo
print("====================", texto, "==================== 1")

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
print ("====================", texto_2, "==================== 2")


texto_2 = texto_2.split()
for t in texto_2:
    et = etiqueta(t)
    print (t + " " + et )
