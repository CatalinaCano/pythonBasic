

def convert(ammount):
    return ammount * 150

def main():
    print('CALCULADORA DE DIVISAS')
    ammount = float(
        input('Ingrese el valor que quiere convertir a pesos Colombianos:'))
    result = convert(ammount)
    #print(f"{ammount} Pesos Mexicanos son {result} Pesos Colombianos")
    print('{} Pesos Mexicanos son {} Pesos Colombianos'.format(ammount, result))

if __name__ == "__main__":
    main()
