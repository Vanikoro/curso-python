# -*- coding: utf-8 -*-
import calculadora_indices as ic

def iniciar_programa () -> None:
    print('')
    print ("En esta función se van a calcular las calorias en actividad de una persona")
    peso = float(input("Ingrese el peso de la persona en kilogramos: "))
    altura = float(input("Ingrese la altura de la persona en centimetros: "))
    edad = int(input("Ingrese la edad de la persona en años: "))
    v_genero = int(input("Ingrese el valor de 5 en caso de ser hombre o -161 en caso de ser mujer: "))
    print('')
    print("1.2: poco o ningun ejercicio \n1.375: ejercicio ligero (1 a 3 días a la semana) \n1.55: ejercicio moderado (3 a 5 días a la semana) \n1.725: deportista (6 a 7 días a la semana) \n1.9: atleta (entrenamientos mañana y tarde)")
    v_actividad = float(input("Ingrese la actividad: "))
    c_actividad = ic.calcular_calorias_en_actividad(peso, altura, edad, v_genero, v_actividad)
    print('')
    print("Las calorias en actividad son: "+str(c_actividad))
    
iniciar_programa()