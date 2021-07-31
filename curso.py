import math

def area_triangulo (x:float, y:float, z: float) -> float:
    s = (x+y+z)/2
    x = s*(s-x)*(s-y)*(s-z)
    area = round(math.sqrt(x),1)
    return area

def calcular_BMI (x:float, y:float) -> float:
    b = x*0.45
    c = y*0.025
    a = b/c**2
    BMI = round(a,2)
    return BMI

def calcular_cambio(a:int)->str:

    cantidad_500 = int(a/500)
    x = a%500
    cantidad_200 = int(x/200)
    x = x%200
    cantidad_100 = int(x/100)
    x = x%100
    cantidad_50 = int(x/50)
    return str(cantidad_500)+','+str(cantidad_200)+','+str(cantidad_100)+','+str(cantidad_50)