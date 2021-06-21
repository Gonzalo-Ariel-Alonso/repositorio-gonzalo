#El diccionario "campeonato" tiene cargados a equipos de futbol como clave y una terna de números (lista), 
# cuyo significado es: partidos ganados (primer valor), partidos empatados (segundo valor), partidos perdidos (tercer valor).
#Se pide que hagas un programa en Python que:
 #   1 -Indique si todos los equipos tienen la misma cantidad de partidos jugados.
 #   2 -En caso que 1) sea verdadero, liste de mayor a menor los equipos por puntaje, teniendo en cuenta que obtiene 3 puntos por cada partido ganado, y un punto por cada partido empatado.
 #   3 -En caso de que 1) sea falso, liste de menor a mayor los equipos por cantidad de partidos jugados.
#Nota: a igual cantidad de partidos o puntos, el orden es indistinto.
#En cada caso se deberá indicar:
#equipo – (puntaje o cantidad de partidos)  
#def campeonatoo():
import operator
campeonato = {} 
campeonato["Boca"] = [9, 2, 0]
campeonato["River"] = [2, 3, 8]
campeonato["Racing"] = [0, 3, 8]
campeonato["Independiente"] = [6, 3, 2]
campeonato["Velez"] = [6, 3, 2]
campeonato["San Lorenzo"] = [1, 3, 7]
campeonato["Huracan"] = [3, 3, 5]
 #   return campeonato

partidos_jugados = {}
lista_partidos = []
for equipo in campeonato:
    partidos_jugados[equipo] = campeonato[equipo][0] + campeonato[equipo][1] + campeonato[equipo][2]
lista_partidos = partidos_jugados.values()

def mismos_partidos(lista_partidos):
    valor = True
    for partido_1 in lista_partidos:
        for partido_2 in lista_partidos:
            if partido_1 != partido_2:
                valor = False
                return False
    return valor

if mismos_partidos(lista_partidos) == True:
    print("Todos los esquipos tiene los mismos partidos")
    equipo_puntos = {}
    for equipo in campeonato:  
        equipo_puntos[equipo] = campeonato[equipo][0] * 3 + campeonato[equipo][1]   
    equipo_puntos_ordenado = sorted(equipo_puntos,key = lambda x: x[1])
else:
    print("No todos los equipos tiene la misma cantidad de partidos")
    partidos_ordenados = dict(sorted(partidos_jugados.items(),key = lambda x: x[1] , reverse = True))
    for equipo in partidos_ordenados:
        print(equipo,"jugo",partidos_jugados[equipo],"partidos")
