# -*- coding: utf-8 -*-

def infija2postfija(infija):
    '''Convierte una expresión infija a una posfija, devolviendo una lista.'''
    prioridad = {'(':1, ')':2, '+': 3, '-': 3, '*': 4, '/':4, '^':5}
    pila = []
    salida = []
    for e in infija:
        if e == '(':
            pila.append(e)
        elif e == ')':
            while pila[len(pila) - 1 ] != '(':
                salida.append(pila.pop())
            pila.pop()
        elif e in ['+', '-', '*', '/', '^']:
            while (len(pila) != 0) and (prioridad.get(e)) <= prioridad.get(pila[len(pila) - 1]):
                salida.append(pila.pop())
            pila.append(e)
        else:
            salida.append(e)
    while len(pila) != 0:
        salida.append(pila.pop())
    return salida

def evaluaPosfija(expresion_posfija):
    '''Si la posfija tiene valores, recibe la lista Posfija y devuelve el resultado.'''
    pila = []
    for i in expresion_posfija:
        if not(i in ['+', '-', '*', '/']):
            pila.append(float(i))
        else:
            op2 = pila.pop()
            op1 = pila.pop()
            if i == '+':
                pila.append(op1 + op2)
            elif i == '-':
                pila.append(op1 - op2)
            elif i == '*':
                pila.append(op1 * op2)
            elif i == '/':
                pila.append(op1 / op2)
            elif i == '^':
                pila.append(op1 ** op2)
    return pila.pop()


expresion1 = ["a","*","b","*","c","*","d","*","e"]
expresion2 = ["a","*","b","+","c","*","d"]
expresion3 = ["2","*","3","+","4","*","5"]
print (infija2postfija(expresion2))

res1  = infija2postfija(expresion3)
salida = evaluaPosfija(res1)
print (salida)

