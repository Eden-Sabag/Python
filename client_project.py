from socket import *
import tkinter as tk
from tkinter import *
from tkinter import ttk, messagebox
import mysql.connector


client = socket(AF_INET, SOCK_STREAM)
client.connect(("192.168.56.1", 4444))

foodList = []
# Screen clear button

def clearFoodList():
    foodList.clear()

def recip(ans):
    window7 = Tk()
    window7.title('Recipes')
    window7.geometry('500x500')
    window7.resizable(False, False)
    name = Label(window7, text=ans[1], font="ar 10 bold")
    name.place(x=30, y=70)
    name = Label(window7, text=ans[0], font="ar 10 bold")
    name.place(x=30, y=10)
    class Closure:
            def __init__(self):
                self.button = Button(window7, text='Close the window', command=self.close)
                self.button.place(x=350, y=370)

            def close(self):
                window7.destroy()
                clearFoodList()
    e = Closure()
    window7.mainloop()


# Read once for each ingredients
def commodity(General_commodity):
    flag = True
    for x in foodList:
        if x == General_commodity:
            flag = False
    if flag:
        foodList.append(General_commodity)

# Ingredient list
def Data():
    window2 = Tk()
    window2.title('DATA')
    window2.geometry('750x500')
    window2.resizable(False, False)
    window2.protocol('WM_DELETE_WINDOW',)

    Label(window2, text="Ingredients :", font="ar 15 bold").grid(row=0, column=3)
    btn = ttk.Button(window2, text="water", command=lambda: commodity("water"))
    btn.place(x=40, y=40, width=120, height=50)
    btn = ttk.Button(window2, text="oil", command=lambda: commodity("oil"))
    btn.place(x=40, y=90, width=120, height=50)
    btn = ttk.Button(window2, text="egg", command=lambda: commodity("egg"))
    btn.place(x=40, y=140, width=120, height=50)
    btn = ttk.Button(window2, text="salt", command=lambda: commodity("salt"))
    btn.place(x=40, y=190, width=120, height=50)
    btn = ttk.Button(window2, text="sugar", command=lambda: commodity("sugar"))
    btn.place(x=40, y=240, width=120, height=50)
    btn = ttk.Button(window2, text="black pepper", command=lambda: commodity("black pepper"))
    btn.place(x=40, y=290, width=120, height=50)
    btn = ttk.Button(window2, text="paprika", command=lambda: commodity("paprika"))
    btn.place(x=40, y=340, width=120, height=50)
    btn = ttk.Button(window2, text="chicken", command=lambda: commodity("chicken"))
    btn.place(x=40, y=390, width=120, height=50)
    btn = ttk.Button(window2, text="fish", command=lambda: commodity("fish"))
    btn.place(x=40, y=440, width=120, height=50)
    btn = ttk.Button(window2, text="garlic", command=lambda: commodity("garlic"))
    btn.place(x=180, y=40, width=120, height=50)
    btn = ttk.Button(window2, text="bell pepper", command=lambda: commodity("bell pepper"))
    btn.place(x=180, y=90, width=120, height=50)
    btn = ttk.Button(window2, text="potato", command=lambda: commodity("potato"))
    btn.place(x=180, y=140, width=120, height=50)
    btn = ttk.Button(window2, text="parsley", command=lambda: commodity("parsley"))
    btn.place(x=180, y=190, width=120, height=50)
    btn = ttk.Button(window2, text="coriander", command=lambda: commodity("coriander"))
    btn.place(x=180, y=240, width=120, height=50)
    btn = ttk.Button(window2, text="onion", command=lambda: commodity("onion"))
    btn.place(x=180, y=290, width=120, height=50)
    btn = ttk.Button(window2, text="eggplant", command=lambda: commodity("eggplant"))
    btn.place(x=180, y=340, width=120, height=50)
    btn = ttk.Button(window2, text="lemon", command=lambda: commodity("lemon"))
    btn.place(x=180, y=390, width=120, height=50)
    btn = ttk.Button(window2, text="rice", command=lambda: commodity("rice"))
    btn.place(x=180, y=440, width=120, height=50)
    btn = ttk.Button(window2, text="chicken soup", command=lambda: commodity("chicken soup"))
    btn.place(x=320, y=40, width=120, height=50)
    btn = ttk.Button(window2, text="white pepper", command=lambda: commodity("white pepper"))
    btn.place(x=320, y=90, width=120, height=50)
    btn = ttk.Button(window2, text="turmeric", command=lambda: commodity("turmeric"))
    btn.place(x=320, y=140, width=120, height=50)
    btn = ttk.Button(window2, text="flour", command=lambda: commodity("flour"))
    btn.place(x=320, y=190, width=120, height=50)
    btn = ttk.Button(window2, text="yeast", command=lambda: commodity("yeast"))
    btn.place(x=320, y=240, width=120, height=50)
    btn = ttk.Button(window2, text="pickled cucumber", command=lambda: commodity("pickled cucumber"))
    btn.place(x=320, y=290, width=120, height=50)
    btn = ttk.Button(window2, text="garlic powder", command=lambda: commodity("garlic powder"))
    btn.place(x=320, y=340, width=120, height=50)
    btn = ttk.Button(window2, text="tomato", command=lambda: commodity("tomato"))
    btn.place(x=320, y=390, width=120, height=50)
    btn = ttk.Button(window2, text="hot pepper", command=lambda: commodity("hot pepper"))
    btn.place(x=320, y=440, width=120, height=50)
    btn = ttk.Button(window2, text="mayonnaise", command=lambda: commodity("mayonnaise"))
    btn.place(x=460, y=40, width=120, height=50)
    btn = ttk.Button(window2, text="cucumber", command=lambda: commodity("cucumber"))
    btn.place(x=460, y=90, width=120, height=50)
    but = Button(window2, text="Clear", height=2, width=11, command=clearFoodList)
    but.place(x=600, y=40)
    but = Button(window2, text="Search", height=2, width=11,  command=abs)
    but.place(x=600, y=90)
    entry = Entry(window2)
    entry.place(x=460, y=180, height=300, width=250)
    text = Label(window2, text="Recipe list:", font=("arial 15 bold"), fg="red")
    text.place(x=460, y=150)
    text = Label(window2, text="*omelet", font=("arial 12 bold"))
    text.place(x=480, y=185)
    text = Label(window2, text="*Rice", font=("arial 12 bold"))
    text.place(x=480, y=220)
    text = Label(window2, text="*Chicken in the oven", font=("arial 12 bold"))
    text.place(x=480, y=255)
    text = Label(window2, text="*Moroccan fish", font=("arial 12 bold"))
    text.place(x=480, y=290)
    text = Label(window2, text="*Bread", font=("arial 12 bold"))
    text.place(x=480, y=325)
    text = Label(window2, text="*Eggplant in mayonnaise", font=("arial 12 bold"))
    text.place(x=480, y=360)
    text = Label(window2, text="*Vegetable Salad", font=("arial 12 bold"))
    text.place(x=480, y=395)
    text = Label(window2, text="*Matbucha", font=("arial 12 bold"))
    text.place(x=480, y=430)
    text = Label(window2, text="*Baked potatos", font=("arial 12 bold"))
    text.place(x=480, y=465)

def exit_function(window):
    window.destroy()

def abs():
    food_list=""
    for x in foodList:
        food_list=x+" "+food_list
    client.sendall(food_list.encode())
    my_ans=(client.recv(2048).decode()).split("-")
    recip(my_ans)
    clearFoodList()


# Login after registration
def login():

    name_and_password = name_entry.get() + "," + password_entry.get()

    client.sendall(name_and_password.encode())
    ans = client.recv(2048).decode()
    if ans=="yes":
        window1.destroy()
        Data()

    else:
        pass

# First login
def register():
    window5 = Tk()
    window5.title('register')
    window5.geometry('300x250')
    window5.resizable(False, False)
    mydb = mysql.connector.connect(
        host="localhost",
        user="root",
        password="",
        database="project1"
    )

    mycursor = mydb.cursor()

    def ppp():
        sql = "INSERT INTO users (name, password) VALUES (%s, %s)"
        val = (name_entry.get(), password_entry.get())
        mycursor.execute(sql, val)

        mydb.commit()

    name = Label(window5, text="Name:", font="ar 10 bold")
    name.place(x=30, y=70)
    name_entry = Entry(window5, width=20)
    name_entry.place(x=120, y=70)

    password = Label(window5, text="Password:", font="ar 10 bold")
    password.place(x=30, y=130)
    password_entry = Entry(window5, width=20, show='*')
    password_entry.place(x=120, y=130)

    selects = Button(window5, text="Save Data", command=ppp)
    selects.place(x=90, y=190)
    window5.mainloop()


window1 = Tk()
window1.title('user name')
window1.geometry("350x350")
window1.resizable(False, False)


lbltitle = Label(window1, text="Login from :", font=("arial 20 bold"), fg="red").grid(row=0, column=3)
name = Label(window1, text="Name:", font="ar 10 bold")
name.place(x=30, y=70)
name_entry = Entry(window1, width=20)
name_entry.place(x=140, y=70)

password = Label(window1, text="Password:", font="ar 10 bold")
password.place(x=30, y=130)
password_entry = Entry(window1, width=20, show='*')
password_entry.place(x=140, y=130)

btn = ttk.Button(window1, text="Login",  command=login)
btn.place(x=160, y=160, width=100, height=30)

btn = ttk.Button(window1, text="Register", command=register)
btn.place(x=200, y=280, width=110, height=50)



window1.mainloop()
