# -*- coding: utf-8 -*-
import calculadora_indices as ic

def iniciar_programa () -> None:
    print('')
    print ("En esta función se va a calcular el porcentaje de grasa corporal de una persona")
    peso = float(input("Ingrese el peso de la persona en kilogramos: "))
    altura = float(input("Ingrese la altura de la persona en metros: "))
    edad = int(input("Ingrese la edad de la persona en años: "))
    v_genero = float(input("Ingrese el valor de 10.8 en caso de ser hombre o 0 en caso de ser mujer: "))
    GC = ic.calcular_porcentaje_grasa(peso, altura, edad, v_genero)
    print('')
    print("El porcentaje de grasa corporal es: "+str(GC)+"%")
    
iniciar_programa()