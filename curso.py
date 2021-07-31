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