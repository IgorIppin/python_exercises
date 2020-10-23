# Prueba de primalidad que comprueba que el número ingresado sea un número primo

def es_primo(numero):
    contador = 0
    if numero == 1:
        return False

    for i in range(1, numero + 1):
        if i == 1 or i == numero:
            continue
        if numero % i == 0:
            contador += 1
    if contador == 0:
        return True
    else:
        return False


def run():
    numero = int(input('Escribe un número: '))
    if es_primo(numero):
        print('El '+str(numero)+' es un número primo')
    else:
        print('El '+str(numero)+' no es un número primo')


if __name__ == '__main__':
    run()
