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
        
    
    
    
