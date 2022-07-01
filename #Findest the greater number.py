#Findest the greater number
list = [9,41,12,3,74,15]

maxNumber = list[0]
minNumber = list[0]
sum =0
avg =0


for num in list:
    if num > maxNumber:
        maxNumber = num
    if num < minNumber:
        minNumber = num
    sum += sum+num

print('El mayor numero es:'+ str(maxNumber))
print('El menor numero es:'+ str(minNumber))
print('La suma de todos los elementos es: '+str(sum))
print ('EL promedio de todos los elementos es: '+str(sum /len(list)))