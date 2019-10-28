import sys
KEYS = {
    'a': 'w',
    'b': 'E',
    'c': 'x',
    'd': '1',
    'e': 'a',
    'f': 't',
    'g': '0',
    'h': 'C',
    'i': 'b',
    'j': '!',
    'k': 'z',
    'l': '8',
    'm': 'M',
    'n': 'I',
    'o': 'd',
    'p': '.',
    'q': 'U',
    'r': 'Y',
    's': 'i',
    't': '3',
    'u': ',',
    'v': 'J',
    'w': 'N',
    'x': 'f',
    'y': 'm',
    'z': 'W',
    'A': 'G',
    'B': 'S',
    'C': 'j',
    'D': 'n',
    'E': 's',
    'F': 'Q',
    'G': 'o',
    'H': 'e',
    'I': 'u',
    'J': 'g',
    'K': '2',
    'L': '9',
    'M': 'A',
    'N': '5',
    'O': '4',
    'P': '?',
    'Q': 'c',
    'R': 'r',
    'S': 'O',
    'T': 'P',
    'U': 'h',
    'V': '6',
    'W': 'q',
    'X': 'H',
    'Y': 'R',
    'Z': 'l',
    '0': 'k',
    '1': '7',
    '2': 'X',
    '3': 'L',
    '4': 'p',
    '5': 'v',
    '6': 'T',
    '7': 'V',
    '8': 'y',
    '9': 'K',
    '.': 'Z',
    ',': 'D',
    '?': 'F',
    '!': 'B',
    ' ':'*'
}

def encrypt(mensaje):
    message_list = list(mensaje)
    encrypt_message = ''

    for letter in message_list:
        encrypt_message+= KEYS.get(letter)

    print('Encriptando... {} El mensaje ha quedado encriptado como {}\n'.format(mensaje,encrypt_message))
    play()


def desencrypt(mensaje):
   message_list = list(mensaje)
   message = ''
   for l in message_list:
    for key, value in KEYS.items():
        if l == value:
            message+= key
   
   print('El mensaje {} desencriptado significa {}'.format(mensaje,message))
   play()

def play():
    option = input('========================== C R Y P T O G R A P H Y ========================== \n === (E)ncriptar \n === (D)esencriptar \n === (S)alir \n \t')
    if option.upper() =='E':
        mensaje = input('Escribe el Mensaje que deseas cifrar. \n \t')
        encrypt(mensaje)
    elif option.upper() =='D':
        mensaje = input('Escribe el Mensaje que deseas descifrar. \n \t')
        desencrypt(mensaje)
    elif option.upper()=='S':
        sys.exit()
    else:
        print('Upss!! opción no valida por favor seleccione una opción valida.')
        play()

if __name__ =="__main__":
    play();