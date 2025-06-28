from tkinter import *
from tkinter import ttk
import requests

def data_get():
    city = city_name.get()
    data = requests.get("https://api.openweathermap.org/data/2.5/weather?q="+city+"&appid=dfad3e7e41299f77cb5c369b2f2aa572").json()
    w_label1.config(text=data["weather"][0]["main"])
    wb_label1.config(text=data["weather"][0]["description"])
    temp_label1.config(text=str(int(data["main"]["temp"]-273.15)))
    per_label1.config(text=data["main"]["pressure"])
    

win = Tk()
win.title("Weather App")
win.config(bg= 'blue')
win.geometry("500x570")

name_label = Label(win, text="Weather App", font=("Time Nee Roman",30,"bold"))
name_label.place(x=25,y=50,height=50,width=450)

city_name = StringVar()
list_name = [
    "Mumbai", "Delhi", "Bangalore", "Hyderabad", "Ahmedabad", "Chennai", 
    "Kolkata", "Pune", "Jaipur", "Surat", "Lucknow", "Kanpur", "Nagpur", 
    "Indore", "Thane", "Bhopal", "Visakhapatnam", "Patna", "Vadodara", 
    "Ghaziabad", "Ludhiana", "Agra", "Nashik", "Faridabad", "Meerut", 
    "Rajkot", "Kalyan-Dombivli", "Vasai-Virar", "Varanasi", "Srinagar", 
    "Aurangabad", "Dhanbad", "Amritsar", "Navi Mumbai", "Allahabad", 
    "Ranchi", "Howrah", "Coimbatore", "Jabalpur", "Gwalior", "Vijayawada", 
    "Jodhpur", "Madurai", "Raipur", "Kota", "Guwahati", "Chandigarh", 
    "Solapur", "Hubballi-Dharwad", "Tiruchirappalli"
]


com = ttk.Combobox(win, text="Weather App Using Tkinter", value=list_name, 
                   font=("Time Nee Roman",20,"bold"), textvariable=city_name)
com.place(x=25,y=120,height=50,width=450)

w_label = Label(win, text="Weather Climate", font=("Time Nee Roman",20,"bold"))
w_label.place(x=25,y=260,height=50,width=220)
w_label1 = Label(win, text="", font=("Time Nee Roman",20,"bold"))
w_label1.place(x=250,y=260,height=50,width=220)

wb_label = Label(win, text="Weather Descrip", font=("Time Nee Roman",20,"bold"))
wb_label.place(x=25,y=330,height=50,width=220)
wb_label1 = Label(win, text="", font=("Time Nee Roman",20,"bold"))
wb_label1.place(x=250,y=330,height=50,width=220)

temp_label = Label(win, text="Temperature", font=("Time Nee Roman",20,"bold"))
temp_label.place(x=25,y=400,height=50,width=220)
temp_label1 = Label(win, text="", font=("Time Nee Roman",20,"bold"))
temp_label1.place(x=250,y=400,height=50,width=220)

per_label = Label(win, text="Pressure", font=("Time Nee Roman",20,"bold"))
per_label.place(x=25,y=470,height=50,width=220)
per_label1 = Label(win, text="", font=("Time Nee Roman",20,"bold"))
per_label1.place(x=250,y=470,height=50,width=220)

done_button = Button(win, text="Get Weather", font=("Time Nee Roman",30,"bold"), command=data_get)
done_button.place(x=125,y=190,height=50,width=250)

win.mainloop()