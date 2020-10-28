# Conversor de monedas usando un diccionario para diferenciar los distintos tipos de moneda.

def data_collection():
    pesos = {'1': 0.1, '2': 0.3, '3': 0.4, '4': 0.2}
    quantity = 0
    coin = input('''Ingresa la opción de los pesos convertir:
        1.- Pesos colombianos
        2.- Pesos chilenos
        3.- Pesos argentinos
        4.- Pesos mexicanos
Elige tu moneda: ''')
    try:
        quantity = float(input('Ingresa la cantidad de pesos: '))
    except ValueError:
        print('[[El valor de cantidad de pesos debe ser un número.]]')
        data_collection()
    if coin in pesos:
        valor = pesos[coin]*quantity
        print('Son '+str(valor)+' dolares')
    else:
        print('La moneda seleccionada no esta disponible. Vuelve a intentarlo.')
        data_collection()


if __name__ == '__main__':
    # Currrency converter funcion
    data_collection()
