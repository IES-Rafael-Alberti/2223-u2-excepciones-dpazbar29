#2.3.4
'''
Escribir un programa que pida al usuario un número entero
si la entrada no es correcta, mostrará el mensaje "La entrada no es correcta"
lanzará la excepción capturada.
'''
def mensajeSalida4(numero):
    if not int(numero):
        raise ValueError("La entrada no es un número válido")
    return "El número ingresado es: " + str(numero)

if __name__ == "__main__":

    #proceso
    numero_correcto = False
    while not numero_correcto:
        try:
            #leemos
            numero = input("Introduzca un número entero: ")
            numero = int(numero)
            numero_correcto = True
        except:
            raise ValueError("La entrada no es un número válido")

    mensaje = mensajeSalida4(numero)

    #devolvemos
    print(mensaje)