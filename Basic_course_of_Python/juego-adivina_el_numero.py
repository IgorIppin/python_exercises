# El juego trata de adivinar el numero que genero la computadora. En caso de fallar
# el juego indica si el numero debe ser mayor o menor.

from random import randint

def run():
    numero_maquina = randint(0, 100)
    for i in range(100):
        apuesta = int(input('Ingresa tu número: '))
        if apuesta < numero_maquina:
            print('Ups!! El número ingresado es muy pequeño')
            continue
        elif apuesta > numero_maquina:
            print('Ups!! El número ingresado es muy grande')
            continue
        else:
            print('¡¡¡Enhorabuena has acertado!!!')
            break


if __name__ == '__main__':
    run()
