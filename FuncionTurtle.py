# -*- coding: utf-8 -*-
import turtle

def main():
    window = turtle.Screen()
    cata = turtle.Turtle()
    make_square(cata)
    window.mainloop()

def make_square(cata):
    length = int(input("Ingrese el tamaño tio:\n"))
    for i in range (4):
        make_line(cata, length)

def make_line(cata,length):
    cata.forward(length)
    cata.left(90)

if __name__ == '__main__':
    main()
