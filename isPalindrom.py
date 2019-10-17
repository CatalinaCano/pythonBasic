def is_palindrom(word):
    inverse_word = word[::-1]
    print('Palabra Original: {}'.format(word))
    print('Palabra Inversa: {}'.format(inverse_word))
    for i in range(0,len(word)):
        if(word[i]==inverse_word[i]):
            return True
        else:
            return False
def run():
    word = input('Ingresa una palabra: ')
    if(is_palindrom(word.lower())):
        print('La palabra es un palindromo')
    else:
        print('La palabra no es un palindromo')

if __name__ =="__main__":
    run()
