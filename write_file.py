# -*- coding: utf-8 -*-
def read_file():
    #Context Manager que pemirte llevar juntas las operaciones open and close de un archivo
    with open('numeros.txt','w') as fl:
        for num in range(1,11):
            fl.write('El numero es {} \n'.format(num))


if __name__=='__main__':
    read_file()