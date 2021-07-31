# -*- coding: utf-8 -*-

def calcular_IMC (peso:float,altura:float) -> float:
    """
    Calcula el indice de masa corporal de una persona a partir de la ecuación definida anteriormente.

    Parameters
    ----------
    peso : float
        DESCRIPTION.
    altura : float
        DESCRIPTION.

    Returns
    -------
    float
        DESCRIPTION.

    """
    a = peso
    b = altura
    IMC = round(a/b**2,2)
    return IMC
    
def calcular_porcentaje_grasa (peso:float,altura:float,edad:int,valor_genero:float) ->float:
    """
    Calcula el porcentaje de grasa de una persona a partir de la ecuación definida anteriormente.

    Parameters
    ----------
    peso : float
        DESCRIPTION.
    altura : float
        DESCRIPTION.
    edad : int
        DESCRIPTION.
    valor_genero : float
        DESCRIPTION.

    Returns
    -------
    float
        DESCRIPTION.

    """
    a = peso
    b = altura
    c = edad
    d = valor_genero
    IMC = round(a/b**2,2)
    GC = round(1.2 * IMC + 0.23 * edad - 5.4 - valor_genero,2)
    return GC
    
def calcular_calorias_en_reposo (peso:float,altura:float,edad:int,valor_genero:int) -> float:
    """
    Calcula la cantidad de calorías que una persona quema estando en reposo (esto es, su tasa metabólica basal), a partir de la ecuación definida anteriormente.

    Parameters
    ----------
    peso : float
        DESCRIPTION.
    altura : float
        DESCRIPTION.
    edad : int
        DESCRIPTION.
    valor_genero : int
        DESCRIPTION.

    Returns
    -------
    float
        DESCRIPTION.

    """
    a = peso
    b = altura
    c = edad
    d = valor_genero
    TBM = round(10 * a + 6.25 * b - 5 * c + d,2)
    return TBM
    
def calcular_calorias_en_actividad (peso:float,altura:float,edad:int, valor_genero:float, valor_actividad:float) ->float:
    """
    Calcula la cantidad de calorías que una persona quema al realizar algún tipo de actividad física (esto es, su tasa metabólica basal según actividad física), a partir de la ecuación definida anteriormente.

    Parameters
    ----------
    peso : float
        DESCRIPTION.
    altura : float
        DESCRIPTION.
    edad : int
        DESCRIPTION.
    valor_genero : float
        DESCRIPTION.

    Returns
    -------
    float
        DESCRIPTION.

    """
    a = peso
    b = altura
    c = edad
    d = valor_genero
    e = valor_actividad
    TBM = round(10 * a + 6.25 * b - 5 * c + d,2)
    TBMa = round(TBM * e,2)
    return TBMa
    
    
def consumo_calorias_recomendado_para_adelgazar (peso:float,altura:float,edad:int,valor_genero:float) ->str:
    """
    Calcula el rango de calorías recomendado, que debe consumir una persona diariamente en caso de que desee adelgazar, a partir de la ecuación definida anteriormente.

    Parameters
    ----------
    peso : float
        DESCRIPTION.
    edad : float
        DESCRIPTION.
    edad : int
        DESCRIPTION.
    valor_genero : float
        DESCRIPTION.

    Returns
    -------
    str
        DESCRIPTION.

    """
    a = peso
    b = altura
    c = edad
    d = valor_genero
    TBM = round(10 * a + 6.25 * b - 5 * c + d,2)
    c_min = round(TBM * 0.8,2)
    c_max = round(TBM * 0.85,2)
    return "Para adelgazar es recomendado que consumas entre: "+str(c_min)+" y "+str(c_max)+" calorías al día"
    
    