# Conversor de monedas usando if para diferenciar los distintos tipos de moneda.

def currency_exchange(coin, quatity):
    if coin == 1:  # Moneda chilena
        result = quatity * 0.0013
        print(f'Los {quatity} pesos chilenos equivalen a {result} dolares')
    elif coin == 2:  # Moneda colombiana
        result = quatity * 0.00027
        print(f'Los {quatity} pesos colombianos equivalen a {result} dolares')
    elif coin == 3:  # Moneda Argentina
        result = quatity * 0.014
        print(f'Los {quatity} pesos argentinos equivalen a {result} dolares')
    elif coin == 4:  # Moneda mexicana
        result = quatity * 0.044
        print(f'Los {quatity} pesos mexicanos equivalen a {result} dolares')
    else:  # Otro
        print('La opcion ingresada no esta disponible')


if __name__ == '__main__':
    try:
        user_coin = int(input('''
        Ingresa el indice de la moneda que quieres convertira  dolar:
            [1] Moneda chilena a Dolar
            [2] Moneda colombiana a Dolar
            [3] Moneda argentida a Dolar
            [4] Moneda mexicana a Dolar
        Selecciona: '''))
        print('********************************')
        user_quantity = int(input('Ingresa la cantidad que quieres convertir: '))
        currency_exchange(user_coin, user_quantity)
    except:
        print('* * * * * * E R R O R * * * * * *')
        print('Por favor, Ingresa solo valores numericos')
