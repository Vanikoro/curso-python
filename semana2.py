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
    
def picas_y_fijas (numero_secreto:int, intento:int) -> dict:
    num_1 = {}
    num_2 = {}
    num_1 = con_num(numero_secreto)
    num_2 = con_num(intento)
    p_f = {"PICAS":0, "FIJAS":0}
    if num_2[1] == num_1[1]:
        p_f["FIJAS"] += 1
    elif num_2[1] == num_1[2] or num_2[1] == num_1[3] or num_2[1] == num_1[4]: 
        p_f["PICAS"] += 1
    if num_2[2] == num_1[2]:
        p_f["FIJAS"] += 1
    elif num_2[2] == num_1[1] or num_2[2] == num_1[3] or num_2[2] == num_1[4]: 
        p_f["PICAS"] += 1
    if num_2[3] == num_1[3]:
        p_f["FIJAS"] += 1
    elif num_2[3] == num_1[1] or num_2[3] == num_1[2] or num_2[3] == num_1[4]: 
        p_f["PICAS"] += 1
    if num_2[4] == num_1[4]:
        p_f["FIJAS"] += 1
    elif num_2[4] == num_1[1] or num_2[4] == num_1[2] or num_2[4] == num_1[3]: 
        p_f["PICAS"] += 1
    return p_f
    
def con_num (num_conv:int) -> dict:
    num = {}
    num[1] = num_conv // 1000
    num[2] = (num_conv // 100) % 10
    num[3] = (num_conv // 10) % 10
    num[4] = num_conv % 10
    return num

def mejor_del_salon (estudiante1:dict, estudiante2:dict, estudiante3:dict, estudiante4:dict, estudiante5:dict) ->str:
    prom1 = cal_prom(estudiante1)
    prom2 = cal_prom(estudiante2)
    prom3 = cal_prom(estudiante3)
    prom4 = cal_prom(estudiante4)
    prom5 = cal_prom(estudiante5)
    mejor = estudiante1["nombre"]
    if prom1 < prom2:
        mejor = estudiante2["nombre"]
    elif prom2 < prom3:
        mejor = estudiante3["nombre"]
    elif prom3 < prom4:
        mejor = estudiante4["nombre"]
    elif prom4 < prom5:
        mejor = estudiante5["nombre"]
    return mejor
   
def cal_prom (est:dict) -> float:
    x = round((est["matematicas"] + est["español"] + est["ciencias"] + est["literatura"] + est["arte"])/5,2)
    return x

estudiante1 = {'nombre': 'pedro', 'matematicas': 4.7, 'español': 4.2, 'ciencias': 4.3, 'literatura': 2.5, 'arte': 4.2}
x = cal_prom(estudiante1)
print(x)                

    
    
    
