import requests
import json
import tkinter as tk


#Get Key
#This is a file not in my respository I don't want you to have it
file = open("..//..//API_Keys//fixerkey.txt","r")

key = file.read()


resp = requests.get('http://data.fixer.io/api/latest?access_key='+key)

#Converts response to JSON
data = resp.json()

#print(data["base"])
#print(data["date"])
#print(data["rates"]["CAD"])





#Step 1: Create two lists
country = []
value = []
rate_data = data["rates"]

def action(x):
	print(x)
	print(rate_data[x])

#Step 2 Cop all the data fron the pull into these lists
#Loop thtough all rates. using "special loop"
for key in rate_data:
	country.append(key)
	value.append(rate_data[key])
print(country)
print(value)

root = tk.TK()#this makes your root window

f1 = tk.Frame(root)
cur_label = tk.Label(f1, text = "Select Currency")
var = tk.StringVar(f1)
var.set(country[0]) #d
dropDown = tk.OptionMenu(f1,var,*country)

cur_label.pack()
dropDown.pack()

root.mainloop()
print("END")



