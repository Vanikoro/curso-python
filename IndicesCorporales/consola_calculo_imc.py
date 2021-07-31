# -*- coding: utf-8 -*-
import calculadora_indices as ic

def iniciar_programa () -> None:
    print('')
    print ("En esta función se va a calcular el valor del IMC de una persona")
    peso = float(input("Ingrese el peso de la persona en kilogramos: "))
    altura = float(input("Ingrese la altura de la persona en metros: "))
    IMC = ic.calcular_IMC(peso, altura)
    print('')
    print("El valor del IMC es: "+str(IMC))
    
iniciar_programa()