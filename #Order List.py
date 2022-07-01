#Order List

def getValue(list, criterio):
    val= list[0] #None representa ausencia de valor
    for num in list:
        if criterio == 1 and num < val:
            val = num
        elif criterio == 2 and num > val:
            val =num
    return val

def deleteValue(list, num):
    list.remove(num)

def start(list,criterio):
    orderlist = []
    for i in range (len(list)):
        temp = getValue(list,criterio)    
        orderlist.append(temp)
        deleteValue(list,temp)
    return orderlist


try:
    crit = int(input('ORDENAMIENTO DE LISTAS \n Ingrese una de las siguientes opciones: \n 1. Ordena Ascendente \n 2. Ordene Descendente \n'))
    if(crit<1 or crit >2):
        print('Opcion no  válida')
        quit()
    else:  
        list = [9,41,12,3,74,15]
        print('Lista Original:'+ str(list))
        print('Lista Ordenada:' + str(start(list,crit)))
except:
    quit()

