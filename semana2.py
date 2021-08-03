def es_divisible (n:int,d:int) -> int:
    if d != 0:
        if n%(2*d) == 0:
            resultado = 2
        elif n%d == 0 and n%(2*d) !=0:
            resultado = 1
        else:
            resultado = 0
    else:
         resultado = 0
    return resultado    

def es_palindromo (id:int) -> int:
    u = id % 10
    id //= 10
    d = id % 10
    id //= 10
    c = id % 10
    inv = (u * 100) + (d * 10) + c
    return inv
  
def clasificar_regalo (id:int) -> str:
    if id > 100 and id < 999:
        numero = es_palindromo(id)
        if numero == id:
            if id % 2 != 0:
                res = "girl"
            else:
                res = "boy"
        else:
            if id % 2 != 0:
                res = "woman"
            else:
                res = "man"
    return res

def movimiento_robot (orientacion_actual:str, giro_1:str, giro_2:str, giro_3:str) -> str:
    if giro_1 == "L":
        a = g_izq(orientacion_actual)
    if giro_1 == "R":
        a = g_der(orientacion_actual)
    if giro_1 == "H":
        a = media(orientacion_actual)
    if giro_1 == ".":
        a = orientacion_actual
    if giro_2 == "L":
        b = g_izq(a)
    if giro_2 == "R":
        b = g_der(a)
    if giro_2 == "H":
        b = media(a)
    if giro_2 == ".":
        b = a
    if giro_3 == "L":
        c = g_izq(b)
    if giro_3 == "R":
        c = g_der(b)
    if giro_3 == "H":
        c = media(b)
    if giro_3 == ".":
        c = b
    return str(c)
    
def g_izq (a:str) -> str:
    if a == "N":
        p_final = "W"
    if a == "W":
        p_final = "S"
    if a == "S":
        p_final = "E"
    if a == "E":
        p_final = "N"
    return p_final

def g_der (a:str) -> str:
    if a == "N":
        p_final = "E"
    if a == "E":
        p_final = "S"
    if a == "S":
        p_final = "W"
    if a == "W":
        p_final = "N"
    return p_final

def media (a:str) -> str:
    if a == "N":
        p_final = "S"
    if a == "W":
        p_final = "E"
    if a == "S":
        p_final = "N"
    if a == "E":
        p_final = "W"
    return p_final    
    
def conteo_de_materias (nombre_materia_1:str, nombre_materia_2:str, nombre_materia_3:str) -> int:
    contador = 0
    if "programacion" in nombre_materia_1 :
        contador += 1
    if "programacion" in nombre_materia_2:
        contador += 1
    if "programacion" in nombre_materia_3:
        contador +=1
    if "matematica" in nombre_materia_1:
        contador += 1
    if "matematica" in nombre_materia_2:
        contador +=1
    if "matematica" in nombre_materia_3:
        contador +=1
    if "filosofia" in nombre_materia_1:
        contador += 1
    if "filosofia" in nombre_materia_2:
        contador +=1
    if "filosofia" in nombre_materia_3:
        contador +=1
    if "literatura" in nombre_materia_1:
        contador += 1
    if "literatura" in nombre_materia_2:
        contador +=1
    if "literatura" in nombre_materia_3:
        contador +=1
    return contador
    
                

    
    
    
