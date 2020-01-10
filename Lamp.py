# -*- coding: utf-8 -*-

class Lamp:

    # DEFINCION DE ATRIBUTOS
    # El nombre del atributo empieza com _ para indicar que es privado
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

    #Constructor de la Clase SIEMPRE debe ir, primer metodo que se ejecuta
    #cuando se genera una instancia
    #Se pronuncia donder init
    def __init__(self):
        self.is_turnet_on = False

    #Metodos Publicos reciben una intancia de Lamp con la palabra reservada self
    def turn_on(self):
        self.is_turnet_on = True
        self._show_lamp()

    def turn_off(self):
        self.is_turnet_on = False
        self._show_lamp()

    #Metodo Privado
    def _show_lamp(self):
        if self.is_turnet_on:
            print(self._LAMPS[0])
        else:
            print(self._LAMPS[1])

def run():
    lamp = Lamp()

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
        else:
            break

if __name__ == "__main__":
    run()
