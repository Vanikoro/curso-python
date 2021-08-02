"""
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
  """
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
        
                

    
    
    
