# -*- coding: utf-8 -*-
import calculadora_indices as ic

def iniciar_programa () -> None:
    print('')
    print ("En esta función se van a calcular las calorias en reposo de una persona")
    peso = float(input("Ingrese el peso de la persona en kilogramos: "))
    altura = float(input("Ingrese la altura de la persona en centimetros: "))
    edad = int(input("Ingrese la edad de la persona en años: "))
    v_genero = int(input("Ingrese el valor de 5 en caso de ser hombre o -161 en caso de ser mujer: "))
    c_reposo = ic.calcular_calorias_en_reposo(peso, altura, edad, v_genero)
    print('')
    print("Las calorias en reposo son: "+str(c_reposo))
    
iniciar_programa()