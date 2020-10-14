# Esta funcion comprueba que el string es un palindromo
# Palindromo: significa que se lee igual tanto izquierda a derecha como al reves.

def palindromo(text):
    if text == text[::-1]:
        print('El string es un palindromo.')
    else:
        print('El texto no es un palindromo.')


if __name__ == '__main__':
    text = input('Escribe el texto para comprobar si es un palindromo: ').lower().replace(' ', '')
    palindromo(text)
