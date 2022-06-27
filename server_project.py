from socket import *
import tkinter as tk
from tkinter import *
from tkinter import ttk, messagebox
import mysql.connector
#import client_project

def food_check(food_list):

    mydb = mysql.connector.connect(
        host="localhost",
        user="root",
        password="",
        database="project1"
    )

    food = mydb.cursor()
    food.execute("SELECT * FROM foods")
    food_info = food.fetchall()
    # food = []

    foodList = food_list.split()
    ingredients = []
    food_ans= ["There is no food with these ingredients on the list", ""]
    flag1 = False
    flag2 = False
    for x in food_info:
        count = 0
        indexStart = 0
        indexEnd = 0
        for t in x[1]:
            if t == ",":
                ingredients.append(x[1][indexStart:indexEnd])
                indexStart = indexEnd + 2
            indexEnd = indexEnd + 1
        if len(ingredients) == len(foodList):
            for y in ingredients:
                for i in foodList:
                    if y == i:
                        count = count + 1
                        flag1 = True
                        break
                if flag1 == False:
                    break
                flag1 = False
            if count == len(ingredients):
                flag2 = True
                food_ans[0] = x[0]
                food_ans[1] = x[2]
        if flag2:
            return food_ans
        ingredients=[]
    return food_ans




server = socket(AF_INET,SOCK_STREAM)
server.bind(("",4444))
server.listen(3)
client,addr= server.accept()

mydb = mysql.connector.connect(
        host="localhost",
        user="root",
        password="",
        database="project1"
    )

user = mydb.cursor()
user.execute("SELECT * FROM users")
user_info = user.fetchall()

data = client.recv(2048).decode()
name_ans_password=data.split(",")
name = name_ans_password[0]
password = name_ans_password[1]

ans="no"
for x in user_info:
   if x[0] == name and x[len(x) - 1] == password:
        ans="yes"
client.sendall(ans.encode())

while True:
    food_list = client.recv(2048).decode()
    name_and_recipe=food_check(food_list)
    my_ans=name_and_recipe[0]+"-"+name_and_recipe[1]
    client.sendall(my_ans.encode())




















