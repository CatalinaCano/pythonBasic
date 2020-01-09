def check_number(list,sort_list):
    print(list)
    print(sort_list)
    list.pop(0)

def run():
    list = [2,4,1,5,7,9,3]
    sort_list=[]
    
    if len(sort_list)==0:
        number=list[0]
        sort_list.append(number)
        list.pop(0)

    while len(list)>0:
        check_number(list,sort_list)




if __name__ == "__main__":
    run()