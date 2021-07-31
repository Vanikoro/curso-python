# -*- coding: utf-8 -*-
import calculadora_indices as ic

def iniciar_programa () -> None:
    print('')
    print ("En esta función se va a calcular la cantidad de calorías recomendadaas que una persona debe consumir a diario, en caso que desee adelgazar")
    peso = float(input("Ingrese el peso de la persona en kilogramos: "))
    altura = float(input("Ingrese la altura de la persona en centimetros: "))
    edad = int(input("Ingrese la edad de la persona en años: "))
    v_genero = int(input("Ingrese el valor de 5 en caso de ser hombre o -161 en caso de ser mujer: "))
    c_adelgazar = ic.consumo_calorias_recomendado_para_adelgazar(peso, altura, edad, v_genero)
    print('')
    print(c_adelgazar)
    
iniciar_programa()