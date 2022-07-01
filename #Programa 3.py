def computepay(h, r):
    if h <= 40:
        return h*r
    else:
        total = h*r
        comision = (h-40.0)*(0.5*r)
        return total + comision
    
    


try:
    hrs = float(input("Enter Hours:"))
    rate = float(input("Enter Rate:"))

except:
    print('Error en los valores ingresados')
    quit()

total = computepay(hrs,rate)
print(total)