from tkinter import *
import sqlite3 

root = Tk()
root.title('Car Rental')
root.geometry("400x400")

connection = sqlite3.connect('CarRental2019.db')
cursor = connection.cursor()


def addCusImage():

    def addCus():
        submit_conn = sqlite3.connect('CarRental2019.db')
        submit_cur = submit_conn.cursor()

        submit_cur.execute("INSERT INTO CUSTOMER(NAME,PHONE) VALUES(:name, :phone)",
        {
            'name':name.get(),
            'phone':phone.get()
        })

        # submit_cur.execute("INSERT INTO CUSTOMER VALUES(:CustId, :name, :phone)",
        # {
        #     'CustId': 233,
        #     'name':name.get(),
        #     'phone':phone.get()
        # })

        submit_conn.commit()
        submit_conn.close()


    wind = Toplevel()
    wind.geometry("300x150")
    
    name_label = Label(wind,text="Name: ")
    name_label.grid(row=0,column=0)
    name = Entry(wind,width="30")
    name.grid(row=0, column =1, padx=20)

    phone_label = Label(wind,text="Phone: ")
    phone_label.grid(row=1,column=0)
    phone = Entry(wind,width="30")
    phone.grid(row=1,column=1,padx=20)

    newCus = Button(wind, text="Insert", command=addCus)
    newCus.grid(row=2, column=1, padx=20)

    exitButton = Button(wind,text="Close Window", command=wind.destroy)
    exitButton.grid(row=4, column=1,padx=50)

    wind.mainloop()


def addCar():

    def addNewCar():
        submit_conn = sqlite3.connect('CarRental2019.db')
        submit_cur = submit_conn.cursor()

        submit_cur.execute("INSERT INTO VEHICLE VALUES(:VehicleId, :Description, :Year, :Type, :Category)",
        {
            'VehicleId': vehicleId.get(),
            'Description': description.get(),
            'Year': int(year.get()),
            'Type': int(typeIn.get()),
            'Category': int(category.get())
        })

        submit_conn.commit()
        submit_conn.close()


    wind = Toplevel()
    wind.geometry("300x200")
    
    Id_label = Label(wind,text="Vehicle Id: ")
    Id_label.grid(row=0,column=0)
    vehicleId = Entry(wind,width="30")
    vehicleId.grid(row=0, column =1, padx=20)

    des_label = Label(wind,text="Description: ")
    des_label.grid(row=1,column=0)
    description = Entry(wind,width="30")
    description.grid(row=1,column=1,padx=20)

    year_label = Label(wind,text="Year: ")
    year_label.grid(row=2,column=0)
    year = Entry(wind,width="30")
    year.grid(row=2,column=1,padx=20)

    type_label = Label(wind,text="Type: ")
    type_label.grid(row=3,column=0)
    typeIn = Entry(wind,width="30")
    typeIn.grid(row=3,column=1,padx=20)

    cat_label = Label(wind,text="Category: ")
    cat_label.grid(row=4,column=0)
    category = Entry(wind,width="30")
    category.grid(row=4,column=1,padx=20)

    newCus = Button(wind, text="Insert", command=addNewCar)
    newCus.grid(row=5, column=1, padx=20)

    exitButton = Button(wind,text="Close Window", command=wind.destroy)
    exitButton.grid(row=7, column=1,padx=50)

    wind.mainloop()


def addRental():

    def find():
        submit_conn = sqlite3.connect('CarRental2019.db')
        submit_cur = submit_conn.cursor()

        start = rentS.get()
        end = rentE.get()

        submit_cur.execute("SELECT V.VehicleID as VIN, V.Description, V.Year From VEHICLE as V, RENTAL as R Where V.type = ? AND V.Category = ? AND ((CAST(R.StartDate as DATE) >= CAST(\""+start+"\" as DATE) and CAST(R.StartDate as Date) <= CAST(\""+end+"\" as Date) OR (CAST(R.ReturnDate as DATE) >= CAST(\""+start+"\" as DATE) and CAST(R.ReturnDate as Date) <= CAST(\""+end+"\" as Date)))AND R.VehicleID = V.VehicleID)",
        (int(carType.get()), int(cat.get()), ))
        

        res = submit_cur.fetchall()
        printRes = ""
        for i in range(len(res)):
            printRes += ' '.join(map(str,res[i])) +"\n"


        title_label = Label(wind,text="Free Vehicles")
        title_label.grid(row=5,column=1)
        res_label = Label(wind,text=printRes)
        res_label.grid(row=6, column=1)

        submit_conn.commit()
        submit_conn.close()


    def addNewRent():

        submit_conn = sqlite3.connect('CarRental2019.db')
        submit_cur = submit_conn.cursor()

        submit_cur.execute("INSERT INTO RENTAL VALUES(:CustId, :VehicleID, :StartDate, :OrderDate, :RentalType, :Qty, :ReturnDate, :TotalAmount, :PaymentDate)",
        {
            'CustId': cusId.get(),
            'VehicleID': carID.get(),
            'StartDate': rentS2.get(),
            'OrderDate': order.get(),
            'RentalType': int(typE.get()),
            'Qty': int(cat2.get()),
            'ReturnDate': retDate.get(), 
            'TotalAmount': float(total.get()),
            'PaymentDate': payDate.get()
        })

        submit_conn.commit()
        submit_conn.close()


    wind = Toplevel()
    wind.geometry("400x400")
    
    type_label = Label(wind,text="Car Type: ")
    type_label.grid(row=0,column=0)
    carType = Entry(wind,width="30")
    carType.grid(row=0, column =1, padx=20)

    cat_label = Label(wind,text="Car Category: ")
    cat_label.grid(row=1,column=0)
    cat = Entry(wind,width="30")
    cat.grid(row=1,column=1,padx=20)

    rentS_label = Label(wind,text="Rent Start Date: ")
    rentS_label.grid(row=2,column=0)
    rentS = Entry(wind,width="30")
    rentS.grid(row=2,column=1,padx=20)

    rentE_label = Label(wind,text="Rent End Date: ")
    rentE_label.grid(row=3,column=0)
    rentE = Entry(wind,width="30")
    rentE.grid(row=3,column=1,padx=20)   

    Search = Button(wind, text="Search", command=find)
    Search.grid(row=4, column=1, padx=20)

    cusId_label = Label(wind,text="Customer Id: ")
    cusId_label.grid(row=9,column=0)
    cusId = Entry(wind,width="30")
    cusId.grid(row=9, column =1, padx=20)

    carId_label = Label(wind,text="Vehicle Id: ")
    carId_label.grid(row=10,column=0)
    carID = Entry(wind,width="30")
    carID.grid(row=10,column=1,padx=20)

    rentS2_label = Label(wind,text="Rent Start Date: ")
    rentS2_label.grid(row=11,column=0)
    rentS2 = Entry(wind,width="30")
    rentS2.grid(row=11,column=1,padx=20)

    order_label = Label(wind,text="Order Date: ")
    order_label.grid(row=12,column=0)
    order = Entry(wind,width="30")
    order.grid(row=12,column=1,padx=20)   

    type_label = Label(wind,text="Rental Type: ")
    type_label.grid(row=13,column=0)
    typE = Entry(wind,width="30")
    typE.grid(row=13,column=1,padx=20)

    cat_label = Label(wind,text="Category: ")
    cat_label.grid(row=14,column=0)
    cat2 = Entry(wind,width="30")
    cat2.grid(row=14,column=1,padx=20)

    ret_label = Label(wind,text="Return Date: ")
    ret_label.grid(row=15,column=0)
    retDate = Entry(wind,width="30")
    retDate.grid(row=15,column=1,padx=20)

    tot_label = Label(wind,text="Total Amount: ")
    tot_label.grid(row=16,column=0)
    total = Entry(wind,width="30")
    total.grid(row=16,column=1,padx=20)

    pay_label = Label(wind,text="Payment Date: ")
    pay_label.grid(row=17,column=0)
    payDate = Entry(wind,width="30")
    payDate.grid(row=17,column=1,padx=20)

    insert = Button(wind, text="Insert", command=addNewRent)
    insert.grid(row=18,column=1,padx=50)

    exitButton = Button(wind,text="Close Window", command=wind.destroy)
    exitButton.grid(row=19, column=1,padx=50)

    wind.mainloop()

newCus = Button(root, text="Add New Customer", command=addCusImage)
newCus.pack()

newCar = Button(root, text="Add New Vehicle", command=addCar)
newCar.pack()

rent = Button(root, text="Add New Rental Reservation", command=addRental)
rent.pack()

root.mainloop()

