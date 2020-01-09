def read_file(path):
    with open(path,'r') as f:
        for line in f:
            print(line)



if __name__=='__main__':
    path='C:/Users/dcano/Desktop/python/Test.txt';
    read_file(path)