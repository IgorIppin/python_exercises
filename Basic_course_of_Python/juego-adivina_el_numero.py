# El juego trata de adivinar el numero que genero la computadora. En caso de fallar
# el juego indica si el numero debe ser mayor o menor.

from random import randint

def run():
    machine_number = randint(0, 100)
    for i in range(100):
        bet = int(input('Ingresa tu número: '))
        if bet < machine_number:
            print('Ups!! El número ingresado es muy pequeño')
            continue
        elif bet > machine_number:
            print('Ups!! El número ingresado es muy grande')
            continue
        else:
            print('¡¡¡Enhorabuena has acertado!!!')
            break


if __name__ == '__main__':
    run()
