from tkinter import *
from PIL import ImageTk
from PIL import Image
import requests, json
import math
import locale
from datetime import date
import datetime
from settings import saved_city_name
import os

window = Tk()
window.geometry("295x640")
window.configure(bg = "#ffffff")




# Enter your API key here
api_key = "49162d983649b7cd5e7eda3473bc246d"
api_key_geo = "pk.eyJ1IjoiYmlsbGFhYWFsIiwiYSI6ImNreHJyOHA0ejFldzcybm9lbzNuNnF4bXkifQ.HMNFyMq02d_Kvf5YeHdvHA"

# base_url variable to store url
base_url = "http://api.openweathermap.org/data/2.5/weather?"

# Give city name
#city_name = input("Enter city name : ")

# complete_url variable to store
# complete url address
def update_box(cities_list):
    my_list.delete(0, END)
    for item in cities_list:
        my_list.insert(END, item)


def update__(term_to_search):
    match term_to_search:
        case " ":
            my_list.delete(0, END)
        case "":
            my_list.delete(0, END)
        case pro:
        
        
            
            #complete_url_geo= f"https://api.mapbox.com/geocoding/v5/mapbox.places/{term_to_search}.json?access_token={api_key_geo}&autocomplete=True&types=place&language=fr"
            complete_url_geo= f"https://api.mapbox.com/geocoding/v5/mapbox.places/{term_to_search}.json?access_token={api_key_geo}&autocomplete=True&types=place"

            response = requests.get(complete_url_geo)

            #penser aux numresults dans summary



            my = response.json()

            results = my["features"]

            #fetch_1 = results[0]
            #city1 = fetch_1["text"]

            #fetch_2 = results[1]
            #city2 = fetch_2["text"]

            #fetch_3 = results[2]
            #city3 = fetch_3["text"]

            #fetch_4 = results[3]
            #city4 = fetch_4["text"]

            cities_list = []
            #print(city1, city2, city3, city4)

            for yy in results:
                cities_list.append(yy["text"])

            cities_list = list(set(cities_list))   

            update_box(cities_list)
        #if textbox.entryget different:
    #    update la requete

# Update entry box with listbox clicked


def update_weather(city_name):
    complete_url = base_url  + "&lang=fr&" + "appid=" + api_key + "&q=" + city_name
    print(complete_url)
    # get method of requests module
    # return response object
    response = requests.get(complete_url)

    # json method of response object
    # convert json format data into
    # python format data
    x = response.json()

    #wind_speed = x["wind"]["speed"]
    #wind_speed = wind_speed* 3.214
    #wind_speed= math.floor(wind_speed * 10) / 10


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

    #print(math.floor(wind_speed))
    # Now x contains list of nested dictionaries
    # Check the value of "cod" key is equal to
    # "404", means city is found otherwise,
    # city is not found
    if x["cod"] != "404":
        
        try:
            # store the value of "main"
            # key in variable y
            y = x["main"]
            #print(y)
            # store the value corresponding
            # to the "temp" key of y
            wind_speed = x["wind"]["speed"]
            wind_speed = wind_speed* 3.214
            wind_speed= math.floor(wind_speed * 10) / 10

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
            
            canvas.itemconfig(temperature_label, text = (f"{current_temperature}"))
            canvas.itemconfig(date_label, text = (f"Aujourd'hui, {the_date}"))
            canvas.itemconfig(description_label, text = (weather_description))
            canvas.itemconfig(wind_speed_label, text = (f"{wind_speed} km/h"))
            canvas.itemconfig(hum_percentage, text = (f"{humidity} %"))
            
            if len(city_name) > 14:
                canvas.itemconfig(city_label, text = (f"{city_name}"), font= ('Overpass Bold', 15))
            else:
                canvas.itemconfig(city_label, text = (f"{city_name}"), font= ('Overpass Bold', 25))
            
            if len(str(current_temperature)) == 2:
                canvas.moveto(degree_label, 186.5, 275)
            elif len(str(current_temperature)) == 1:
                canvas.moveto(degree_label, 176.5, 275)
            else:
                canvas.moveto(degree_label, 206.5, 275)
            #settings.saved_city_name = city_name
            #saved_city_name.append(city_name)
            settings_file = open('settings.py', 'w')
            settings_file.writelines(f"saved_city_name = '{city_name}'")

        except KeyError:
            print("City Not Found")
    else:
        print("City Not Found")


path = os.path.dirname(os.path.abspath(__file__))+"\\"

#path = "D:/billa/Bureau/Weather_app/Proxlight_Designer_Export/"
#path_icons = "D:/billa/Bureau/Weather_app/Proxlight_Designer_Export/weather_icons/"




search_frame = Frame(window,bg="#ffffff")
search_frame.place(x=0,y=0, width=295, height=640)

home = Frame(window,bg="#ffffff")
home.place(x=0,y=0, width=295, height=640)

def btn_clicked():
    search_frame.tkraise()


#home.tkraise()


canvas = Canvas(
    home,
    bg = "#ffffff",
    height = 640,
    width = 295,
    bd = 0,
    highlightthickness = 0,
    relief = "ridge")
canvas.place(x = 0, y = 0)
#window.wm_attributes('-transparentcolor', '#ab23ff')


canvas_search = Canvas(
    search_frame,
    bg = "#ffffff",
    height = 640,
    width = 295,
    bd = 0,
    highlightthickness = 0,
    relief = "ridge")
canvas_search.place(x = 0, y = 0)



home.tkraise()


background_img = PhotoImage(file = path + "background.png")
background = canvas.create_image(
    148, 320,
    image=background_img)


img1 = PhotoImage(file = path + "img1.png")
b1 = Button(
    canvas,
    image = img1,
    borderwidth = 0,
    highlightthickness = 0,
    command = lambda:btn_clicked(),
    relief = "flat",
    activebackground="#48b4e7")

b1.place(
    x = 17, y = 37,
    width = 31,
    height = 30)

img2 = PhotoImage(file = path + "img2.png")
b2 = Button(
    canvas,
    image = img2,
    borderwidth = 0,
    highlightthickness = 0,
    command = lambda:print("Bell button clicked !"),
    relief = "flat",
    activebackground="#48b9e4")

b2.place(
    x = 252, y = 37,
    width = 24,
    height = 25)







my_entry = Entry(canvas_search, font=("Helvetica", 20))
my_entry.place(x = 0, y = 0)

# Create a listbox
my_list = Listbox(canvas_search, width=50, selectmode="browse")
my_list.place(x = 0, y = 40)

# Create a list of pizza toppings


def select_city(event):
    #selected_city = my_list.curselection()
    #selected_city = my_list.get(ANCHOR)
    selected_city= my_list.curselection()
    selected_city=my_list.get(selected_city)
    my_entry.delete(0, END)
    my_entry.insert("end", selected_city)
    update_weather(selected_city)
    home.tkraise()
# Add the toppings to our list
global state
state = 0


def my_function_up(where):
    my_list.selection_set(first=where)
    #my_entry.unbind("<KeyRelease-Down>")
    #root.after(10000, my_entry.unbind("<KeyRelease-Down>"))
    
#/def my_function_down(where):
    #my_list.selection_set(first=where)


# Create a binding on the listbox onclick
my_list.bind("<<ListboxSelect>>", select_city)
#my_entry.bind("<KeyRelease-Up>", lambda e: my_function_down(0)) 
#my_entry.bind("<KeyRelease-Down>", lambda e: my_function_down(1))      ####### my_list.focus() my_list.focus() my_list.focus()


def get_value(e):
    update__(my_entry.get())


#update__("Trappes")
# Create a binding on the entry box
my_entry.bind("<KeyRelease>", get_value)












#match weather_description:
    #case ""





sun_image = ImageTk.PhotoImage(file= path + "cloudy.png")
canvas.create_image(60.5, 75, image=sun_image, anchor=NW)

#sun_image_ = ImageTk.PhotoImage(file= path_icons + "sun.png")
#canvas.create_image(60.5, 75, image=sun_image_, anchor=NW)

image_panel = ImageTk.PhotoImage(file= path + "panel.png")

#my_lbl = Label(canvas,  text="34",image = test,  compound='center',font= ('Overpass', 50), fg= "#ffffff",width = 260, height =247, bg="#7fc4f1").place(x=18, y=254)
main_panel = canvas.create_image(148, 374, image=image_panel)
#˚˚˚˚˚˚˚˚

temperature_label = canvas.create_text(0,0, font= ('Overpass', 55), fill = "#ffffff")
x1_t,y1_t,x2_t,y2_t = canvas.bbox(temperature_label)
temperature_label_x = (296-(x2_t-x1_t))/2
canvas.moveto(temperature_label, temperature_label_x, 270)
#print(temperature_label_x)


date_label = canvas.create_text(0,200, font= ('Overpass', 10), fill = "#ffffff")
x1_d,y1_d,x2_d,y2_d = canvas.bbox(date_label)
date_label_x = (296-(x2_d-x1_d))/2
canvas.moveto(date_label, date_label_x, 270)




degree_label = canvas.create_text(206.5,325,text = ("˚"), font= ('Overpass', 50), fill = "#ffffff")   #######penser a bien centrer le signe selon la taille de la temperature (1 ou 2 caractères)


description_label = canvas.create_text(0,200, font= ('Overpass Bold', 14), fill = "#ffffff")
x1_des,y1_des,x2_des,y2_des = canvas.bbox(description_label)
description_label_x = (296-(x2_des-x1_des))/2
canvas.moveto(description_label, description_label_x, 376)
#print(x2_des-x1_des)



wind_label = canvas.create_text(116,435,text = ("Vent"), font= ('Overpass', 10), fill = "#ffffff")

hum_label = canvas.create_text(116,467,text = ("Hum."), font= ('Overpass', 10), fill = "#ffffff")


wind_speed_label = canvas.create_text(187,435, font= ('Overpass', 10), fill = "#ffffff")


hum_percentage = canvas.create_text(179,467, font= ('Overpass', 10), fill = "#ffffff")




city_label = canvas.create_text(0,0, font= ('Overpass Bold', 25), fill = "#ffffff")
x1_ci,y1_ci,x2_ci,y2_ci = canvas.bbox(city_label)
city_label_x = (296-(x2_ci-x1_ci))/2
canvas.moveto(city_label, city_label_x, 200)



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

######## ajouter une photo de la ville

if saved_city_name == None:
    search_frame.tkraise()
else:
    update_weather(saved_city_name)


window.resizable(False, False)
window.mainloop()
