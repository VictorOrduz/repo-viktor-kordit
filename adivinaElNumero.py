#Adivina el numero

"""
crea un juego en el que la computadora elige un numero al azar entre 1 y 100 y el usuario tiene que adivinarlo, el programa debe dar pistas al usuario si su numero es mayor o menor que el numero secreto. El juego termina cuando el usuario adivina el numero
1. importa la libreria random
2. genera un numero aleatorio entre 1 y 100 y guardalo en una variable
3. inicia un bucle que se repita hasta que el usuario adivine el numero
4. dentro del bucle pide al usuario que ingrese un numero
5. compara el numero del usuario con el numero secreto y da una pista ('demasiado alto', 'demasiado bajo')
6. si el usuario adivina, imprime un mensaje de felicitacion y termina el bucle
"""
from random import randint

numero_secreto = randint(1, 100)

numero = int(input("ingrese un numero: "))

print(F"el numero secreto es: {numero_secreto}, y el numero digitado es: {numero}")

contador = 1

# comenzar con el bucle infinito
