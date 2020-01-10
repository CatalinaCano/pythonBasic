
# El metodo Open recibe dos Parametros
# 1. Nombre del Archivo
# 2. El modo en que vamos a manipularlo.
  # 'r': Read
  # 'w': Write
  # 'a': Append
  # 'r+': Read and Write
# Siempre se debe cerrar el Archivo con el metodo Close.
# Debe usarse utilizando un manejador de contextos como WITH
# Un MANEJADOR de contexto es un objeto que se notifica cuando un contexto (un bloque de código) comienza y termina

def search_word(buscar_palabra):
    counter = 0
    with open("alphet.txt", encoding="utf8") as f:
        for i in f:
            counter += i.count(buscar_palabra)
        if counter == 0:
            print("La palabra {} no esta en el texto".format(buscar_palabra))
        else:
            print("La palabra {} se repite {} en el texto".format(buscar_palabra, counter))

def appendText():
    with open('C:\\Users\\catal\\Documents\\numbers.txt',"a") as f:
        for i in range(5):
            f.writelines('Hola Mundo')


def writeFile():
    with open('C:\\Users\\catal\\Documents\\numbers.txt','w') as f:
        for num in range(10):
            f.write(str(num))



def readFile():
    with open('C:\\Users\\catal\\Documents\\test.txt','r') as f:
        for line in f:
            print(line)


if __name__ == "__main__":
    buscar_palabra = str(input("Digita la palabra: "))
    search_word(buscar_palabra)

 

         