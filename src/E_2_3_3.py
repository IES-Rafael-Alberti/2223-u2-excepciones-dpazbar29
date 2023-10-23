#2.3.3
'''
Escribir un programa que pida al usuario un número entero positivo
muestre por pantalla la cuenta atrás desde ese número hasta cero
separados por comas.
Deberá solicitar el número hasta introducir uno correcto.
'''

def cuentaAtras(numero):
    resultado  = []
    contador = numero
    if numero < 0:
        raise ValueError("Numero incorrecto: " + str(numero))
    
    while contador >= 1:
        resultado.append(contador)
        strResultado = ",".join(map(str,resultado))
        contador -= 1

    return strResultado

def mensajeSalida3(cuenta):
    return "Resultado: " + str(cuenta)
if __name__ == "__main__":

    numero_correcto = False
    #proceso
    while not numero_correcto:
        try:
            #leemos
            numero = input("Numero entero positivo: ")
            numero = int(numero)
            numero_correcto = True
        except ValueError: #No convertible a entero
            print("Por favor introduzca un número")

    cuenta = cuentaAtras(numero)
    mensaje = mensajeSalida3(cuenta)

    #devolvemos
    print(mensaje)