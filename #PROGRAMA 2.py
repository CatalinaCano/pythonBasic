#PROGRAMA 2 

try:
    hrs = float(input('Ingrese la cantidad de Horas trabajadas: '))
    rate = float(input('Ingrese la Tasa por hora:'))
except:
    print('Los valores ingresados no son validos')
    quit()

if hrs <= 40:
    print('Debes Pagar: '+ str(hrs*rate))
else:
    total = hrs*rate
    comision = (hrs-40.0)*(0.5*rate)
    print ('Debes Pagar:'+ str(total+comision))