PESO_MEXICANO = 175.09


def run():
    print("============== BIENVENIDO ===============")
    print("Elige una de las siguientes opciones \n")
    print("1. Pesos Colombianos a Pesos Mexicanos.")
    print("2. Pesos Mexicanos a Pesos Colombianos.")
    print("3. Terminar.")
    option = int(input("Ingrese una opcion: \n \t"))
    validateOption(option)

def validateOption(option):
    if option == 1 :
        ammount = float(input(
            "Ingrese la cantidad de Pesos Colombianos que desea convertir a Pesos Mexicanos  \n \t"))
        print("${} Pesos Colombianos equivalen a ${} Pesos Mexicanos ".format(
            ammount, round(ammount/PESO_MEXICANO, 0)))
        run()
    elif option== 2:
        ammount = float(input(
            "Ingrese la cantidad de Pesos Mexicanos que desea convertir a Pesos Colombianos  \n \t"))
        print("${} Pesos Mexicanos equivalen a ${} Pesos Colombianos".format(
            ammount,round(ammount*PESO_MEXICANO)))
        run()
    elif option==3:
        return
    else:
        print("Opcion no disponible")
        run()

if __name__ =="__main__":
    run();
