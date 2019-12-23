
poblacion = {
    'mexico': 122,
    'colombia': 56,
    'argentina': 43,
    'chile':18,
    'peru':31
}

def countries():
    flag = True
    while flag:
        try:
            country = str(input('Ingresa el nombre del Pais: ')).lower()
            print('La poblacion del pais {} es de {} Millones de Habitantes'.format(country,poblacion[country]))
        except KeyError:
           add = str(input('El pais {} no se encuentra en nuesta BD , Solo contamos con los siguientes paises: {}\n Deseas agregar la informacion de este pais S/N \n'.format(country, poblacion.keys()))).upper()
           if add=='S':
                value= int(input('Ingrese el numero de la poblacion: \n'))
                poblacion.update( {country : value} )
            
        finally :
             flag = bool(int(input('Deseas continuar 1 (Si) / 0 (No)  \n')))



if __name__ == "__main__":
    countries()