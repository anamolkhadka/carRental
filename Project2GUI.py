from tkinter import *
import sqlite3

# create tkinter window 
root = Tk()
root.title('Car Rental Application')
root.geometry("400x400")

# connecting database
carRental_db = sqlite3.connect('CarRental2019.db')
carRental_db_cursor = carRental_db.cursor()

def req1():
    wind = Toplevel()
    wind.geometry("300x200")
    


#label for the HomeScreen
# label_home= Label(root,text='Welcome to our Car Rental Service !',font=("Helvetica",20))
# label_home.grid(row=1,column=0)


# Creating buttons for the different queries in the main window
req1_Button = Button(root,text='Add a new customer',command=req1)
req1_Button.grid(row=2,column=1)

req2_Button = Button(root,text='Add New Vehicle Information')
req2_Button.grid(row=3,column=1)



#executes tinker components
root.mainloop()
