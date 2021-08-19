from tkinter import *
from tkinter import messagebox
import requests
from bs4 import BeautifulSoup

root = Tk()


def search_weather():
    value = str(yerkir.get())
    if value !="":
        search = f"temperature is {value}"
        url = f"https://www.google.com/search?q={search}"
        r = requests.get(url)
        s = BeautifulSoup(r.text, "html.parser")
        update = s.find("div", class_="BNeawe").text
        messagebox.showinfo("Weather in" + value,  value + " temperature is " + update)
        yerkir.delete(0, END)
    else:
        messagebox.showinfo("Weather in" + value,"Type city name please")

root.title("weather")
root["bg"]=("black")
root.resizable(width=False, height=False)

weathe = Label(root, text="Weather program", bg="green", font=("Arial", 20), fg="white").pack(pady=10)

ty_co = Label(root, text="Type country below", bg="green", font=("Arial", 15), fg="white").pack(pady=10)

yerkir = Entry(root, text="", bg="white", font=("Arial", 25), fg="white")
yerkir.pack()

srchbtn = Button(root, text="Search", bg="red", font=("Arial", 20), fg="white",
                 command=search_weather).pack(pady=10)


root.mainloop()
