#2.3.1
'''
Escribir un programa que pregunte al usuario su edad
muestre por pantalla todos los años que ha cumplido (desde 1 hasta su edad).
'''

def secuenciaAños(edad_int):
    resultado=[]
    contador = 1
    if edad_int < 1:
        raise ValueError("Edad incorrecta: " + str(edad_int))
    while contador <= edad_int:
        resultado.append(contador)
        strResultado = ",".join(map(str,resultado))

        contador += 1
        
    return strResultado

def mensajeSalida1(resultado):
    return "Años cumplidos " + str(resultado)

if __name__ == "__main__":

    numero_correcto = False
    #proceso
    while not numero_correcto:
        try:
            #leemos
            edad = input("Introduzca su edad: ")
            edad_int = int(edad)
            numero_correcto = True
        except ValueError: #No convertible a entero
            print("Por favor introduzca un número")
    res = secuenciaAños(edad_int)    
    mensaje = mensajeSalida1(res)
    #devolvemos
    print(mensaje)

