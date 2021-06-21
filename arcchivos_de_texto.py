def archivos_de_texto():
    """Toma el texto de 3 archivos de texto diferentes"""
    palabra = ""
    palabras_candidatas = []
    palabra_cantidad = {}
    with open("Cuentos.txt","r") as Cuentos:
        for linea_Cuentos in Cuentos:
            for caracter in linea_Cuentos:
                if caracter.isalpha():
                    palabra += caracter
                if not caracter.isalpha():
                    if len(palabra) >= 5:
                        palabras_candidatas.append(palabra)
                    palabra = ""
            for palabra_en_lista in palabras_candidatas:
                if palabra_en_lista not in palabra_cantidad:
                    palabra_cantidad[palabra_en_lista] = [1,0,0]
                else:
                    palabra_cantidad[palabra_en_lista] = [int(palabra_cantidad[palabra_en_lista][0]) +1 , 0, 0]
            palabras_candidatas = []
    with open("La araña negra - tomo 1.txt","r") as La_arana_negra:
        for linea_Cuentos in La_arana_negra:
            for caracter in linea_Cuentos:
                if caracter.isalpha():
                    palabra += caracter
                if not caracter.isalpha():
                    if len(palabra) >= 5:
                        palabras_candidatas.append(palabra)
                    palabra = ""
            for palabra_en_lista in palabras_candidatas:
                if palabra_en_lista not in palabra_cantidad:
                    palabra_cantidad[palabra_en_lista] = [0,1,0]
                else:
                    palabra_cantidad[palabra_en_lista] = [palabra_cantidad[palabra_en_lista][0] , int(palabra_cantidad[palabra_en_lista][1]) + 1, 0]
            palabras_candidatas = [] 
    with open("Las 1000 Noches y 1 Noche.txt","r") as muchas_noches:   
        for linea_Cuentos in muchas_noches:
            for caracter in linea_Cuentos:
                if caracter.isalpha():
                    palabra += caracter
                if not caracter.isalpha():
                    if len(palabra) >= 5:
                        palabras_candidatas.append(palabra)
                    palabra = ""
            for palabra_en_lista in palabras_candidatas:
                if palabra_en_lista not in palabra_cantidad:
                    palabra_cantidad[palabra_en_lista] = [0,0,1]
                else:
                    palabra_cantidad[palabra_en_lista] = [palabra_cantidad[palabra_en_lista][0] ,palabra_cantidad[palabra_en_lista][1], int(palabra_cantidad[palabra_en_lista][2]) + 1]
            palabras_candidatas = []         

    palabra_cantidad = dict(sorted(palabra_cantidad.items()))
    print(palabra_cantidad)            



archivos_de_texto()