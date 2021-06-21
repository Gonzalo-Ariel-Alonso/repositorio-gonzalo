#Escribi una funcion que devuelva verdadero si un alumno aprobo la cursada de la materia, o de lo contrario falso.
#La funcion recibe dos listas: una de trabajos practicos (tps) y otra de notas.
#La lista de tps puede tener tres valores: "no sat", "sat", "supera"; que se corresponden con: "No Satisfactorio", "Satisfactorio" y "Supera lo esperado".
#La lista de notas es numerica con valores del 1 al 10 y puede tener desde una nota (si es 4 o mas) hasta tres notas (si las dos primeras son menores a 4).

#Se aprueba la cursada cuando:

#- La lista tps tiene TODOS los valores con "satisfactorio" o "supera lo esperado" Y 
#- la lista notas tiene por lo menos un 4 o mas.

#Comproba el correcto funcionamiento, mediante los siguientes casos de prueba usando la librería doctest.
#Ademas, agrega DOS casos de prueba adicionales,en donde uno sea Falso y el otro Verdadero.
import doctest
def aprobo_cursada(tps,notas):
    """
    >>> aprobo_cursada(["sat", "supera", "sat"], [2, 2])
    False
    >>> aprobo_cursada(["sat", "no sat", "supera", "sat"], [2, 8])
    False
    >>> aprobo_cursada(["sat"], [6])
    True
    >>> aprobo_cursada(["sat", "supera", "sat"], [8, 8])
    True
    >>> aprobo_cursada(["no sat", "supera", "sat"], [4, 2])
    False"""
    valor = False   
    for tp in tps:
        if tp != "sat" and tp != "supera":
            valor = False
            return valor
    for nota in notas:
        if nota > 3:
            valor = True
            return valor
    return valor
print(doctest.testmod())