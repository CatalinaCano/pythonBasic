import random
IMAGES = ['''
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
    |   |
        |
        =========''', '''
    +---+
    |   |
    O   |
   /|\  |
    |   |
   /    |
        =========''', '''
    +---+
    |   |
    O   |
   /|\  |
    |   |
   / \  |
        =========''', '''
''']

WORDS =['AVIONA','AVIONA','AVIONA']

def startGame():
    attempts = 0
    word = WORDS[random.randint(0,len(WORDS)-1)]
    word_list = list(word)
    joker = '*'
    secret_list= list(joker*len(word_list))
    while attempts<=7:
          print('===============  H A N G E D  G A M E  ===============')
          print('                                        Attempts: {}/7'.format(attempts))
          print(IMAGES[attempts])
          print('    Secret Word: {}'.format(secret_list))
          if attempts >= 7:
              print('You lost, Im Sorry the correct word its {}'.format(word))
              break
          letter = input('    Please insert a letter: ')
          list_index = list()
          for index in range(0,len(word_list)):
              if letter == word_list[index]:
                list_index.append(index)
          if len(list_index)==0:
              attempts = attempts+1
          else:
            for letter_index in list_index:
                secret_list[letter_index]= letter

            if(''.join(secret_list)==word):
                print ('Congratulations, You Win the correct word its {}'.format(word))
                break

   
def run():
    startGame()


if __name__=="__main__":
    run()