NUMBERS_LIST = list()

def sort_list(NUMBERS_LIST):
    print (NUMBERS_LIST)

def check_option (option):
    
    if option == 1:
        number = int(input('Please add the number:  '))
        NUMBERS_LIST.append(number)
        run()
    elif option==2:
       number = int(input('Please write the number:  '))
       list = sort_list(NUMBERS_LIST)
    else:
        print('Invalid option')
        run()

def run(): 
    print ('==============  B I N A R Y  S E A R C H  ==============')
    option = int(input('    1. Add Number \n    2. Find Number\n    >: '))
    check_option(option)

    
if __name__ == '__main__':
    run()