continuar = "s"
localidad_personas = {}
desocupacion_localidad = {}
localidad_empleados = {}
empleados = 0
while continuar != "n":
    localidad = input("Ingrese localidad: ")
    personas = int(input("Ingrese la cantidad de personas que pueden trabajar: "))
    if localidad not in localidad_personas:
        localidad_personas[localidad] = personas
        localidad_empleados[localidad] = int(input("Ingrese la cantidad de empleados: "))
    else:
         localidad_personas[localidad] += int(personas)
         localidad_empleados[localidad] += int(input("Ingrese la cantidad de empleados: "))
    continuar = input("Desea seguir ingresando?(s/n): ")
for loc in localidad_personas:
    print("En la localidad de", loc , "hay",localidad_personas[loc],
    "personas en edad laboral y",localidad_empleados[loc],"trabajando.")
    desocupacion = (1 - int(localidad_empleados[loc]) / int(localidad_personas[loc])) * 100
    desocupacion_localidad[desocupacion] = loc
    empleados +=1
desocupacion_localidad_ordenada = sorted(desocupacion_localidad,reverse=True)
for desocup in desocupacion_localidad_ordenada:
    print("La tasa de desocupacion en",desocupacion_localidad[desocup],"es "+str(desocup)+"%.")
