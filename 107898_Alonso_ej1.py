"contraseña/clave entre 4 y 8 caracteres, sin caracteres adyasentes repetidos"


def validar_clave(clave):
    valor = False
    caracter_anterior = clave
    caracter_posterior = clave[1]
    if not 4 < len(clave) < 8:
        valor = False
    if not clave.isnumeric():
        valor = False
    else:
        for caracter in clave:
            posicion = clave.find(caracter)
            if caracter != caracter_anterior and caracter != caracter_posterior: 
                valor = True
            else:
                valor = False
                return valor
            caracter_anterior = clave[posicion]
            if posicion < len(clave) - 2:
                caracter_posterior = clave[posicion+2]
    return valor
print(validar_clave("172511"))