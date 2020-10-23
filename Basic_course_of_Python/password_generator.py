# Algotritmo para generar una constraseña aleatoriamente.
# Es el mismo algoritmo que usa Firefox

import random


def generator():
    mayus = ['A', 'B', 'C', 'D']
    minus = ['a', 'b', 'c', 'd']
    simbolos = ['º', '!', '$', '·']
    numeros = ['1', '2', '3', '4']

    total = mayus + minus + simbolos + numeros
    password = []
    for i in range(15):
        password.append(random.choice(total))
    password = "".join(password)
    return password

def run():
    password = generator()
    print('Tu nueva contraseña es: ' + password)


if __name__ == '__main__':
    run()
