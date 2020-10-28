# Prueba de primalidad que comprueba que el número ingresado sea un número primo

def is_prime_number(number):
    counter = 0
    if number == 1:
        return False

    for i in range(1, number + 1):
        if i == 1 or i == number:
            continue
        if number % i == 0:
            counter += 1
    if counter == 0:
        return True
    else:
        return False


def run():
    number = int(input('Escribe un número: '))
    if is_prime_number(number):
        print('El '+str(number)+' es un número primo')
    else:
        print('El '+str(number)+' no es un número primo')


if __name__ == '__main__':
    run()
