def obtencion_datos():
    pesos = {'1': 0.1, '2': 0.3, '3': 0.4, '4': 0.2}
    cantidad = 0
    moneda = input('''Ingresa la opción de los pesos convertir:
        1.- Pesos colombianos
        2.- Pesos chilenos
        3.- Pesos argentinos
        4.- Pesos mexicanos
Elige tu moneda: ''')
    try:
        cantidad = float(input('Ingresa la cantidad de pesos: '))
    except ValueError:
        print('[[El valor de cantidad de pesos debe ser un número.]]')
        obtencion_datos()
    if moneda in pesos:
        valor = pesos[moneda]*cantidad
        print('Son '+str(valor)+' dolares')
    else:
        print('La moneda seleccionada no esta disponible. Vuelve a intentarlo.')
        obtencion_datos()


if __name__ == '__main__':
    # Currrency converter funcion
    obtencion_datos()
