from tkinter import *
from PIL import ImageTk
from PIL import Image
import requests, json
import math
import locale
from datetime import date
import time
import datetime

# Enter your API key here
api_key = "49162d983649b7cd5e7eda3473bc246d"

# base_url variable to store url
base_url = "http://api.openweathermap.org/data/2.5/weather?"

# Give city name
city_name = input("Enter city name : ")

# complete_url variable to store
# complete url address
complete_url = base_url  + "&lang=fr&" + "appid=" + api_key + "&q=" + city_name
print(complete_url)

# get method of requests module
# return response object
response = requests.get(complete_url)

# json method of response object
# convert json format data into
# python format data
x = response.json()

wind_speed = x["wind"]["speed"]
wind_speed = wind_speed* 3.214
wind_speed= math.floor(wind_speed * 10) / 10


locale.setlocale(
    category=locale.LC_ALL,
    locale="French"  # Note: do not use "de_DE" as it doesn't work
)
dateee = str(datetime.datetime.now())
year, month, day = dateee.split("-") 
day, rest = day.split(" ")
day = int(day)
month = int(month)
year = int(year)

the_date = date(day=day, month=month, year=year).strftime('%d %B %Y').title()
print(the_date)
#print(math.floor(wind_speed))
# Now x contains list of nested dictionaries
# Check the value of "cod" key is equal to
# "404", means city is found otherwise,
# city is not found
if x["cod"] != "404":

	# store the value of "main"
	# key in variable y
	y = x["main"]
	#print(y)
	# store the value corresponding
	# to the "temp" key of y
	current_temperature = y["temp"]
	# store the value corresponding
	# to the "pressure" key of y
	current_pressure = y["pressure"]

	# store the value corresponding
	# to the "humidity" key of y
	humidity = y["humidity"]

	


	# store the value of "weather"
	# key in variable z
	z = x["weather"]

	# store the value corresponding
	# to the "description" key at
	# the 0th index of z
	weather_description = z[0]["description"]
	weather_description= weather_description.title()
	current_temperature = (current_temperature-273.15)
	current_temperature=math.floor(current_temperature)

else:
	print(" City Not Found ")

def btn_clicked():
    print("Button Clicked")

path = "D:/billa/Bureau/Weather_app/Proxlight_Designer_Export/"
path_icons = "D:/billa/Bureau/Weather_app/Proxlight_Designer_Export/weather_icons/"

window = Tk()

window.geometry("295x640")
window.configure(bg = "#ffffff")
canvas = Canvas(
    window,
    bg = "#ffffff",
    height = 640,
    width = 295,
    bd = 0,
    highlightthickness = 0,
    relief = "ridge")
canvas.place(x = 0, y = 0)
window.wm_attributes('-transparentcolor', '#ab23ff')



background_img = PhotoImage(file = path + "background.png")
background = canvas.create_image(
    148, 320,
    image=background_img)



img1 = PhotoImage(file = path + "img1.png")
b1 = Button(
    image = img1,
    borderwidth = 0,
    highlightthickness = 0,
    command = btn_clicked,
    relief = "flat",
    activebackground="#48b4e7")

b1.place(
    x = 17, y = 37,
    width = 31,
    height = 30)

img2 = PhotoImage(file = path + "img2.png")
b2 = Button(
    image = img2,
    borderwidth = 0,
    highlightthickness = 0,
    command = btn_clicked,
    relief = "flat",
    activebackground="#48b9e4")

b2.place(
    x = 252, y = 37,
    width = 24,
    height = 25)



#match weather_description:
    #case ""









sun_image = ImageTk.PhotoImage(file= path_icons + "cloudy.png")
canvas.create_image(60.5, 75, image=sun_image, anchor=NW)

#sun_image_ = ImageTk.PhotoImage(file= path_icons + "sun.png")
#canvas.create_image(60.5, 75, image=sun_image_, anchor=NW)

#temperature = str(input("Température : "))
temperature = "34"
image_panel = ImageTk.PhotoImage(file= path + "panel.png")

#my_lbl = Label(canvas,  text="34",image = test,  compound='center',font= ('Overpass', 50), fg= "#ffffff",width = 260, height =247, bg="#7fc4f1").place(x=18, y=254)
main_panel = canvas.create_image(148, 374, image=image_panel)
#˚˚˚˚˚˚˚˚

temperature_label = canvas.create_text(0,0,text = (f"{current_temperature}"), font= ('Overpass', 55), fill = "#ffffff")
x1_t,y1_t,x2_t,y2_t = canvas.bbox(temperature_label)
temperature_label_x = (296-(x2_t-x1_t))/2
canvas.moveto(temperature_label, temperature_label_x, 270)
#print(temperature_label_x)


date_label = canvas.create_text(0,200,text = (f"Aujourd'hui, {the_date}"), font= ('Overpass', 10), fill = "#ffffff")
x1_d,y1_d,x2_d,y2_d = canvas.bbox(date_label)
date_label_x = (296-(x2_d-x1_d))/2
canvas.moveto(date_label, date_label_x, 270)



degree_label = canvas.create_text(206.5,325,text = ("˚"), font= ('Overpass', 50), fill = "#ffffff")



description_label = canvas.create_text(0,200,text = (weather_description), font= ('Overpass Bold', 14), fill = "#ffffff")
x1_des,y1_des,x2_des,y2_des = canvas.bbox(description_label)
description_label_x = (296-(x2_des-x1_des))/2
canvas.moveto(description_label, description_label_x, 376)
#print(x2_des-x1_des)



wind_label = canvas.create_text(116,435,text = ("Vent"), font= ('Overpass', 10), fill = "#ffffff")

hum_label = canvas.create_text(116,467,text = ("Hum."), font= ('Overpass', 10), fill = "#ffffff")


wind_speed = canvas.create_text(187,435,text = (f"{wind_speed} km/h"), font= ('Overpass', 10), fill = "#ffffff")


hum_percentage = canvas.create_text(179,467,text = (f"{humidity} %"), font= ('Overpass', 10), fill = "#ffffff")










#temperature_label = canvas.create_text(148,325, text = "34°", font= ('Overpass', 50), fill = "#ffffff")

#my_lbl_ = Label(canvas, text="34", font= ('Overpass', 50), fg= "#ffffff").place(x=106,y=280)    ########, bg="#7fc4f1





#Label(canvas, text= "34°", font= ('Overpass 71'), bg= '#ab23ff').place(x=0,y=0)
#temperature_label = canvas.create_text(106,280, text= "34", font= ('Overpass', 50), fill = "#ffffff")
#my_lbl_.lift()
#canvas.tag_lower(b0)

#canvas.tag_raise(my_lbl_)

#canvas.tag_raise(temperature_label)
#b0.lower(canvas)
#canvas.tag_raise(temperature_label,'all')
#x1,y1,x2,y2 = canvas.bbox(temperature_label)
#print(x2-x1)





window.resizable(False, False)
window.mainloop()
