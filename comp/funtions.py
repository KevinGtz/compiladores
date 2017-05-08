# -*- coding: utf-8 -*-

def es_separador(c):
    separadores = (" \n\t")
    if c in separadores:
        return
    else:
        return False

def es_pal_res(cad):
    palabraRes = ["main", "for", "import", "def", "from", "int", "str", "Class", "print"]
    return (cad in palabraRes)

def es_tipo(cad):
    tipos = ["int","long","float", "string", "double"]
    return (cad in tipos)

def es_id(c):
    ids = ["a", "b", "c", "d", "e", "f"]
    return (c in ids)

def operador_aritmetico(c):
    operadores_aritmeticos = ["+", "-", "/", "//", "%", "*", "**"]
    return (c in operadores_aritmeticos)

def operadores_logico(cad):
    operadores_logicos = ["and", "or", "xor", "not"]
    return  (cad in operadores_logicos)

def operadores_relacional(cad):
    operadores_relacionales = ["==", "!=", "<", ">", "<=", ">="]
    return (cad in operadores_relacionales)

def s_especial(c):
    simbolos_especiales = ["{","}","(",")","[","]",";","=",":","!", "@", "#", "$", "^", "«", "æ", "»", "~", ",", "."]
    return (c in simbolos_especiales)

def etiqueta(token):
    tipo_token = ""
    if operador_aritmetico(token):
        tipo_token = "Operador Aritmetico"
    elif operadores_logico(token):
        tipo_token = "Operador Logico"
    elif operadores_relacional(token):
        tipo_token = "Operador Relacional"
    elif es_id(token):
        tipo_token = "ID"
    elif es_pal_res(token):
        tipo_token = "Palabra reservada"
    elif es_tipo(token):
        tipo_token = "Tipo"
    elif s_especial(token):
        tipo_token = "Simbolo especial"
    else:
        tipo_token = "Numero"
    return tipo_token
