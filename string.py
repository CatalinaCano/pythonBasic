def check_word(letter,word):
    cont = 0
    for i in range(0,len(word)):
        if word[i]==letter:
            cont+= 1
    return cont;

def run():
    word = input('Ingrese la cadena de texto: ')
    for i in range(0,len(word)):
        if(check_word(word[i],word)==1):
            print('La letra {} es la primera letra en ser unica en la cadena'.format(word[i]))
            break

if __name__ =='__main__':
    run()
