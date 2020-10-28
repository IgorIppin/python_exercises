# Programa para jugar al juego del ahorcado en la consola.

import random

IMAGES = ('''
  +---+
  |   |
      |
      |
      |
      |
=========''', '''
  +---+
  |   |
  O   |
      |
      |
      |
=========''', '''
  +---+
  |   |
  O   |
  |   |
      |
      |
=========''', '''
  +---+
  |   |
  O   |
 /|   |
      |
      |
=========''', '''
  +---+
  |   |
  O   |
 /|\  |
      |
      |
=========''', '''
  +---+
  |   |
  O   |
 /|\  |
 /    |
      |
=========''', '''
  +---+
  |   |
  O   |
 /|\  |
 / \  |
      |
=========''')
WORDS = ('lavadora', 'secadora', 'mueble', 'ascensor', 'trabajador', 'minusculo', 'molusco')


def random_word():
    index_word = random.randint(0, len(WORDS) - 1)
    return WORDS[index_word]


def display_board(hidden_word, tries):
    print(IMAGES[tries])
    print(hidden_word)
    print('-- -- * -- -- * -- -- * -- -- * -- -- * -- -- * -- -- * -- -- * -- --')


def run():
    word = random_word()
    # Muestra en la consola el tamaño de la palabra ocultando sus letras.
    hidden_word = ['-'] * len(word)
    # Intentos de acertas del usuario
    tries = 0

    while True:
        display_board(hidden_word, tries)
        # Pede al usuario la letra a comprobar.
        current_letter = input('Escoge una letra: ').lower().strip()
        if current_letter == 'exit':
            break
        # Compruba que el usuario solo a metido un caracter, no puede meter ni mas ni menos.
        if len(current_letter) > 1 or len(current_letter) < 1 or current_letter.isnumeric():
            print('Solo puede introducir una letra en cada intento')
            run()

        letter_indexes = []
        for i in range(len(word)):
            if word[i] == current_letter:
                letter_indexes.append(i)

        if len(letter_indexes) == 0:
            tries += 1
            # Termina el jeugo en caso de que no hacertaste en 7 intentos la palabra oculta
            if tries == 7:
                display_board(hidden_word, tries)
                print('\n¡¡¡Perdiste la partida!!!'
                      '\nLa palabra correcta es: ' + word)
                break
        else:
            for i in letter_indexes:
                hidden_word[i] = current_letter

        # En caso de que no queden guiones en el texto ganas la partida.
        try:
            hidden_word.index('-')
        except ValueError:
            print('\n¡¡¡Felicidades!!! HAs ganado la partida.')
            break


if __name__ == '__main__':
    print('BIENVENIDO AL AHORCADO')
    print('\nSi quieres salir del juego escribe exit')
    run()
