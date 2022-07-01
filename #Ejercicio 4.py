#Ejercicio 4

def max(list):
    value = list[0]
    for num in list:
        if num > value:
            value = num
    return value

def min(list):
    value = list[0]
    for num in list:
        if num < value:
            value = num
    return value

largest = None
smallest = None
list = []
while True:
    num = input("Enter a number: ")
    if(num == "done"):
       if len(list)>0:
        largest= max(list)
        smallest = min(list)
        print("Maximum is", largest)
        print("Minimum is", smallest)
        break
    try:
       
        list.append(int(num))
    except:
        print("Invalid input")
        continue

