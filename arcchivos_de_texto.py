def quitar_tilde_y_may(caracter):
    """Funcion que transforma las mayusculas en minusculas y obvia los acentos"""
    caracter = caracter.lower()
    if caracter == "á": caracter = "a"
    if caracter == "é": caracter = "e"
    if caracter == "í": caracter = "i"
    if caracter == "ó": caracter = "o"
    if caracter == "ú": caracter = "u"
    return caracter

def archivos_de_texto():
    """Toma el texto de 3 archivos, divide las palabras candidatas a utilizar en un diccionario cuyo valor es
    una lista de 3 elementos donde cada uno reprecenta la cantidad de veces que esta repetida la palabra en 
    cada texto """
    palabra = "" 
    palabras_candidatas = [] #lista donde se guardara las palabras candidatas de cada linea
    palabra_cantidad = {} #diccionario con la palabra candidata de clave y las veces que esta repetida en cada texto de valor
    with open("Cuentos.txt","r") as Cuentos: 
        for linea_Cuentos in Cuentos: #cada ciclo del for es una linea del texto
            for caracter in linea_Cuentos: #cada ciclo del for es una caracter de la linea 
                if caracter.isalpha():
                    caracter = quitar_tilde_y_may(caracter) #se transformas caracteres mayusculas y tildes
                    palabra += caracter #cada caracter ira formando la palabra
                if not caracter.isalpha():
                    if len(palabra) >= 5: #se analiza que la palabra tenga 5 o mas caracteres
                        palabras_candidatas.append(palabra) 
                    palabra = "" #se vacia la palabra ya analizada
            for palabra_en_lista in palabras_candidatas: #se introduce las palabras candidatas a un diccionario
                if palabra_en_lista not in palabra_cantidad:
                    palabra_cantidad[palabra_en_lista] = [1,0,0]
                else:
                    palabra_cantidad[palabra_en_lista] = [int(palabra_cantidad[palabra_en_lista][0]) + 1 , 0, 0]
            palabras_candidatas = []
    with open("La araña negra - tomo 1.txt","r") as La_arana_negra:#se repite el mismo proceso con los otros dos textos
        for linea_Cuentos in La_arana_negra:
            for caracter in linea_Cuentos:
                if caracter.isalpha():
                    caracter = quitar_tilde_y_may(caracter)
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
                    caracter = quitar_tilde_y_may(caracter)
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
    palabra_cantidad = dict(sorted(palabra_cantidad.items())) #se ordena el diccionario alfabeticamente
    with open("palabras.csv","w") as palabras_csv: # se agrga el diccionario a un arcivo .csv
        for palabra in palabra_cantidad:
            palabras_csv.write(palabra)
            palabras_csv.write(",")
            palabras_csv.write(str(palabra_cantidad[palabra][0]))
            palabras_csv.write(",")
            palabras_csv.write(str(palabra_cantidad[palabra][1]))
            palabras_csv.write(",")
            palabras_csv.write(str(palabra_cantidad[palabra][2]))
            palabras_csv.write("\n")
    return palabra_cantidad

print(archivos_de_texto())            


