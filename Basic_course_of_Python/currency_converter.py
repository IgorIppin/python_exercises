def conversor(moneda, cantidad, error):
    moneda = moneda.lower()
    pesos = {'pesos colombianos': 0.1, 'pesos argentinos': 0.3, 'pesos chilenos': 0.4, 'pesos mexicanos': 0.2}
    if moneda not in pesos:
        error = True
        return ('[[La '+moneda+' elegida no esta disponible.]]'), error
    try:
        cantidad = float(cantidad)
    except:
        error = True
        return('[[La '+cantidad+' de pesos debe ser un número.]]'), error

    return pesos[moneda]*cantidad, error


def obtencion_datos():
    moneda = input('''Ingresa el tipo de pesos al que quieres convertir:
        Pesos colombianos
        Pesos chilenos
        Pesos argentinos
        Pesos mexicanos
Elige tu moneda: ''')
    cantidad = input('Ingresa la cantidad de pesos: ')
    error = False
    valor, error = conversor(moneda, cantidad, error)
    if error == True:
        print(valor+'\nVuelve a intentarlo.')
        obtencion_datos()
    else:
        print(str(cantidad)+' '+moneda.lower()+' equivale a '+str(valor)+' dolares')
