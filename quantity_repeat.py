
def validarCadena(word):
    word_list = list(word)
    letters = list()
    letters.append(word_list.pop(0))
    for i in range(0,len(word_list)-1):
        if(word_list[i]==letters[0]):
            print(word_list[i]==letters[0])
            word_list.pop(i)
        else:
            print (word_list)
            
def run():
    word = input(' Ingresa la Cadena de Caracteres: ')
    validarCadena(word)

if __name__ =='__main__':
    run()