#2.3.2
'''
Escribir un programa que pida al usuario un número entero positivo
muestre por pantalla todos los números impares desde 1 hasta ese número
separados por comas.
'''

def numerosImpares(numero):
    resultado=[]
    if numero < 1:
        raise ValueError("Número no válido: " + str(numero))
    
    for i in range(1,numero + 1):
        if i % 2 != 0:
            resultado.append(i)
            strResultado = ",".join(map(str,resultado))

    return strResultado
        
def mensajeSalida2(impares):
    return "Numeros impares " + str(impares)



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

    impares = numerosImpares(numero)
    mensaje = mensajeSalida2(impares)

    #devolvemos
    print(mensaje)

