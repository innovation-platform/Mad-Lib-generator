import tkinter
from tkinter import *
main=Tk()
main.geometry("500x500")
main.title("Mad Libs Generator")
Label(main,text="Mad Libs Generator",font="arial",bg="black",fg="white").pack()
Label(main,text="Click one:",font="italic",bg="white",fg="black").place(x=40,y=80)
def madlib1():
    name=input("Enter a name of a boy:")
    color=input("Enter a color name")
    food=input("Enter a food name")
    adjective=input("Enter an adjective")
    profession=input("Enter a professsion")
    print("Once upon a time there lived a person called "+name+".He was "+color+"colored. He always ate "+food+".He was a very "
          +adjective+". He was a "+profession+".")
def madlib2():
    animal=input("Enter name of an animal")
    color=input("Enter color of an animal")
    food=input("Enter food")
    adjective=input("Enter an adjective")
    print(animal+" is an animal which is in "+color+" color. It eats "+food+". It is a very "+adjective+" animal.")
Button(main,text="A Person",font="italic",command=madlib1,bg="black",fg="white").place(x=40,y=160)
Button(main,text="An Animal",font="italic",command=madlib2,bg="black",fg="white").place(x=40,y=240)

    

main.mainloop()
