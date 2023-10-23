#2.3.5
'''
Escribir que solicite una contraseña
si no coincide con la que se tiene:
lance la excepción NameError con el mensaje, "Incorrect Password!!"
'''

def contraseña5(contraseña):
    contraseña_verdadera = "contraseña_segura"

    if contraseña != contraseña_verdadera:
        raise ValueError("Incorrect Password!!")
    return "La contraseña correcta es: " + str(contraseña)




if __name__ == "__main__":

    #proceso
    numero_correcto = False
    while not numero_correcto:
        try:
            #leemos
            contraseña = input("Introduce la contraseña: ")
            contraseña = str(contraseña)
            numero_correcto = True
        except:
            raise ValueError("La entrada no es un número válido")

    mensaje = contraseña5(contraseña)

    #devolvemos
    print(mensaje)
