import math

def area_triangulo (x:float, y:float, z: float) -> float:
    s = (x+y+z)/2
    x = s*(s-x)*(s-y)*(s-z)
    area = round(math.sqrt(x),1)
    return area