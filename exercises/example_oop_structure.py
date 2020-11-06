# Estructura para crear un objeto en el paradigma OOP

class Lamp:

    # Constante privada con el estado visual de la lampara
    _LAMPS = ['''
          .
     .    |    ,
      \   '   /
       ` ,-. '
    --- (   ) ---
         \ /
        _|=|_
       |_____|
    ''',
    '''
         ,-.
        (   )
         \ /
        _|=|_
       |_____|
    ''']

    # Constructor de la clase (primer metodo que se ejcuta cuando se llama la clase)
    def __init__(self, is_turned_on):
        self._is_turned_on = is_turned_on

    # Metodo público que se usara al crear el objeto lampara
    def turn_on(self):
        self._is_turned_on = True
        self._display_image()

    # Metodo público que se usara al crear el objeto lampara
    def turn_off(self):
        self._is_turned_on = False
        self._display_image()

    # Metodo privado
    def _display_image(self):
        if self._is_turned_on:
            print(self._LAMPS[0])
        else:
            print(self._LAMPS[1])


def run():
    # Creamos el objeto lamp a partir de la clase Lamp
    lamp = Lamp(is_turned_on=False)

    # El usuario indica por consola si quiere encender o apagar la lampara
    while True:
        command = str(input('''
            ¿Qué deseas hacer?
            
            [p]render
            [a]pagar
            [s]alir
        '''))
        if command == 'p':
            lamp.turn_on()
        elif command == 'a':
            lamp.turn_off()
        elif command == 's':
            break
        else:
            print('El comando no esta dentro de las opciones')


if __name__ == '__main__':
    run()
