sort_list = []
def order_list(list):
    position= 0
    if len(list)>0:
        min = list[0]
        for index in range(1,len(list)):
            if list[index] <= min:
                min = list[index]
                position=index
        sort_list.append(min)
        list.pop(position)
        order_list(list)
    return sort_list

def run():
    list = [7,2, 6, 3, 10, 1, 4,0]
    #list = [29,2,3,5,7,11,13,17,19,23,29]
    print('Lista Original: {}'.format(list))
    res= order_list(list)
    print('Lista Ordenada: {}'.format(res))

if __name__ == "__main__":
    run()
