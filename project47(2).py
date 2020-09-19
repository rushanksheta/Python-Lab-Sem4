#>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>                sorts playground booking system                    <<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<

#roll no: 47

#Rushank G Sheta  ( SE IT )

#>>>>>>>>>>>>>>>   if the database file named 'booking.db' is already existing, Please delete and run :)    <<<<<<<<<<<<<<<<<<<<<

'''for admin login
                    username = admin
                    password = admin
'''

from tkinter import *
import os
import sqlite3

#file for saving login details 
creds = 'tempfile.temp'

#database
conn = sqlite3.connect('booking.db')
c = conn.cursor()

c.execute(''' SELECT count(name) FROM sqlite_master WHERE type='table' AND name='btable' ''')

#if the count is 1, then table exists
if c.fetchone()[0]==0 : 
    c.execute('''CREATE TABLE btable ([f_name] text,[l_name] text,[c_no] integer,[date] integer,[month] text,[year] integer,[hour] integer,[s_name] text)''')

#if temp != 'btable':
#creating table in database
#c.execute('''CREATE TABLE btable ([f_name] text,[l_name] text,[c_no] integer,[date] integer,[month] text,[year] integer,[hour] integer,[s_name] text)''')
    
#signup window 
def Signup():
    global pwordE
    global nameE
    global roots
 
    roots = Tk()
    roots.title('Signup')
    intruction = Label(roots, text='Please Enter new Credidentials\n') 
    intruction.grid(row=0, column=0, sticky=E) 
 
    nameL = Label(roots, text='New Username: ') 
    pwordL = Label(roots, text='New Password: ') 
    nameL.grid(row=1, column=0, sticky=W) 
    pwordL.grid(row=2, column=0, sticky=W) 
 
    nameE = Entry(roots) 
    pwordE = Entry(roots, show='*') 
    nameE.grid(row=1, column=1) 
    pwordE.grid(row=2, column=1) 
 
    signupButton = Button(roots, text='Signup',activebackground="green", command=FSSignup) 
    signupButton.grid(columnspan=2, sticky=W)
    roots.mainloop() 

#saving signup details in file 
def FSSignup():
    with open(creds, 'w') as f: 
        f.write(nameE.get())
        f.write('\n') 
        f.write(pwordE.get()) 
        f.close() 
 
    roots.destroy() 
    Login() 

#login window 
def Login():
    global nameEL
    global pwordEL 
    global rootA
 
    rootA = Tk()
    rootA.geometry('300x300')
    rootA.title('Login') 
 
    intruction = Label(rootA, text='Please Login\n') 
    intruction.grid(sticky=E) 
 
    nameL = Label(rootA, text='Username: ') 
    pwordL = Label(rootA, text='Password: ') 
    nameL.grid(row=1, sticky=W)
    pwordL.grid(row=2, sticky=W)
 
    nameEL = Entry(rootA)
    pwordEL = Entry(rootA, show='*')
    nameEL.grid(row=1, column=1)
    pwordEL.grid(row=2, column=1)
 
    loginB = Button(rootA, text='Login',activebackground="green", command=CheckLogin) 
    loginB.grid(columnspan=2, sticky=W,ipadx=100,pady=2)
 
    rmuser = Button(rootA, text='Delete User', fg='red', command=DelUser) 
    rmuser.grid(columnspan=2, sticky=W,pady=2)

    def exitwindow():
        rootA.destroy()

    button3 =Button(rootA,text='EXIT',activebackground="red",command=exitwindow)
    button3.grid(row=5,sticky=W)
    rootA.mainloop()
#to display admin login message
'''def adminmessage():
    r = Tk()
    r.title('[ ! ]')
    r.geometry('150x150')
    rlbl = Label(r, text='Logged in as Admin')
    rlbl.grid(row=1)
    def exitwindow():
        r.destroy()
    button3 =Button(r,text='EXIT',activebackground="red",command=exitwindow)
    button3.grid(row=2)
    r.mainloop()
'''

#to check login details 
def CheckLogin():
    with open(creds) as f:
        data = f.readlines() 
        uname = data[0].rstrip()
        pword = data[1].rstrip() 

    if nameEL.get() == 'admin' and pwordEL.get() == 'admin':
        #adminmessage()
        adminlogin()
        
        
    elif nameEL.get() == uname and pwordEL.get() == pword: 
        BookingWindow()
        
    else:
        r = Tk()
        r.title('[ ! ]')
        r.geometry('150x150')
        rlbl = Label(r, text='\n[!] Invalid Login')
        rlbl.pack()
        r.mainloop()

#to delete user 
def DelUser():
    os.remove(creds) 
    rootA.destroy() 
    Signup() 

#booking window
def BookingWindow():
    r = Tk()
    r.title('Booking window')
    r.geometry('600x600')

    top_label1=Label(r,text='Pleaase enter the booking details(Each booking will allow upto 1 hr usage of the ground)')
    top_label1.grid(row=1)
    top_label2=Label(r,text='The ground is open from 6 am upto 10 pm i.e 6 to 22')
    top_label2.grid(row=2)

    global f_name,l_name,c_no,date,month,year,hour,s_name,deleteid
    f_name=Entry(r)
    l_name=Entry(r)
    c_no=Entry(r)

    date=Entry(r)
    month=Entry(r)
    year=Spinbox(r,from_=2020,to=2022)
    hour=Spinbox(r,from_=6,to=21)
    s_name=Entry(r)

    f_name.grid(row=3)
    l_name.grid(row=4)
    c_no.grid(row=5)
    date.grid(row=6)
    month.grid(row=7)
    year.grid(row=8)
    hour.grid(row=9)

    f_nameL=Label(r,text='Name : ')
    l_nameL=Label(r,text='Last name : ')
    c_noL=Label(r,text='Contact no(10 digit) : ')
    dateL=Label(r,text='Date : ')
    monthL=Label(r,text='Month(text) : ')
    yearL=Label(r,text='Year : ')
    hourL=Label(r,text='Hour : ')
    s_nameL=Label(r,text='Pick a sport : ')

               
    f_nameL.grid(row=3,sticky=W)
    l_nameL.grid(row=4,sticky=W)
    c_noL.grid(row=5,sticky=W)
    dateL.grid(row=6,sticky=W)
    monthL.grid(row=7,sticky=W)
    yearL.grid(row=8,sticky=W)
    hourL.grid(row=9,sticky=W)
    s_nameL.grid(row=10,sticky=W)
    s_name.grid(row=10,column=0)

    book=Button(r,text='Book',activebackground="orange",background='pink', command=save_db)
    book.grid(row=11,ipadx=200)

    check=Button(r,text='Check booking status',activebackground="green",background='yellow', command=checkbookings)
    check.grid(row=12,ipadx=100)

    button4 = Button(r,text='Book for an event',activebackground="orange",background='light blue',command=eventmessage)
    button4.grid(row=13,ipadx=100,columnspan=3)
    def exitwindow():
        r.destroy()

    button3 =Button(r,text='EXIT',activebackground="red",command=exitwindow)
    button3.grid(row=14)

    r.mainloop()
#to display message for 'book for an event' button    
def eventmessage():
    r = Tk()
    r.title('[ ! ]')
    r.geometry('300x200')
    rlbl = Label(r, text='Please call 9287645681')
    rlbl.grid(row=1)
    rib2 = Label(r, text='Or mail us at bookatpfg@playfairgrounds.com')
    rib2.grid(row=2)

    def exitwindow():
        r.destroy()    
    
    b1=Button(r,text='close',activebackground='light blue',command=exitwindow)
    b1.grid(row=3)
    r.mainloop()
    
#to display bookings    
def checkbookings():

    r1=Tk()
    r1.title('Booking Status')
    r1.geometry('600x600')
    button1 = Button(r1, text= 'Book more',background='light blue',activebackground="green",command= BookingWindow)
    button1.grid(row=2,ipadx=200)

    label1 = Label(r1, text='Booking successful for')
    label1.grid(row=3)
        
    conn = sqlite3.connect('booking.db')
    c = conn.cursor()
    label2 = Label(r1,text='First name\t\tLast name\tContact no\tDate\tMonth\tYear\tTime\tSport')
    label2.grid(row=4,sticky=W)
    label3 = Label(r1,text='Booking Status is : ')
    label3.grid(row=1)
    
    c.execute("SELECT * FROM btable")
    records=c.fetchall()
    #print(records)
    
    print_records = ''
    for record in records:
        print_records += str(record[0]) + "\t\t\t" + str(record[1]) + "\t\t" + str(record[2]) + "\t" + str(record[3]) + "\t" + str(record[4]) + "\t" + str(record[5]) + "\t" + str(record[6]) + "\t" + str(record[7]) + "\n"   
         
    
    label3 = Label(r1,text=print_records)
    label3.grid(row=5,columnspan=2,sticky=W)

    def exitwindow():
        r1.destroy()

    button3 =Button(r1,text='EXIT',activebackground="red",command=exitwindow)
    button3.grid(row=6,ipadx=200)

    r1.mainloop()

#to save data into table in database
def save_db():
    conn = sqlite3.connect('booking.db')
    c = conn.cursor()

    #c.execute('''CREATE TABLE btable ([f_name] text,[l_name] text,[c_no] integer,[date] integer,[month] integer,[year] integer,[hour] integer)''')
    

    c.execute("INSERT INTO btable VALUES (:f_name, :l_name, :c_no, :date, :month, :year, :hour, :s_name)",
            {
                    'f_name': f_name.get(),
                    'l_name': l_name.get(),
                    'c_no': c_no.get(),
                    'date': date.get(),
                    'month': month.get(),
                    'year': year.get(),
                    'hour': hour.get(),
                    's_name': s_name.get()
            })
    conn.commit()
    conn.close()

    f_name.delete(0,END)
    l_name.delete(0,END)
    c_no.delete(0,END)
    date.delete(0,END)
    month.delete(0,END)
    #year.delete(0,END)
    #hour.delete(0,END)
    s_name.delete(0,END)

#ro delete data from database
def delete_db():

    
    conn = sqlite3.connect('booking.db')
    c = conn.cursor()

    c.execute("Delete from btable WHERE c_no= " +e1.get())


    conn.commit()
    conn.close()
    e1.delete(0,END)

#for admin login
def adminlogin():
    r = Tk()
    r.geometry('600x600')

    l = Label(r,text='Welcome Admin :)')
    l.grid(row=1,sticky=W,pady=2)

    bl = Label(r,text='Enter contact no for booking to delete : ')
    bl.grid(row=2,sticky=W)

    global e1
    e1=Entry(r)
    e1.grid(row=2,column=2)
    
    b1 = Button(r,text='Delete Bookings',activebackground='green',background='yellow',command=delete_db)
    b1.grid(row=2,column=3,padx=2)

    #to display bookings in admin window
    def check_bookings():
        r.geometry('900x600')
        conn = sqlite3.connect('booking.db')
        c = conn.cursor()
        label2 = Label(r,text='First name\t\tLastname\tContact no\tDate\tMonth\tYear\tTime\tSport')
        label2.grid(row=4,sticky=W)
    
        c.execute("SELECT * FROM btable")
        records=c.fetchall()
        #print(records)
        
        print_records = ''
        for record in records:
            print_records += str(record[0]) + "\t\t\t" + str(record[1]) + "\t\t" + str(record[2]) + "\t" + str(record[3]) + "\t" + str(record[4]) + "\t" + str(record[5]) + "\t" + str(record[6]) + "\t" + str(record[7]) + "\n"   
             
        
        label3 = Label(r,text=print_records)
        label3.grid(row=5,columnspan=2,sticky=W)
        
    check_bookings()    
    c_b = Button(r,text='Refresh Bookings',activebackground='green',background='yellow',command=check_bookings)
    c_b.grid(row=2,column=4,padx=2)

    b2 = Button(r,text='Sign in as user to book',background='light blue',activebackground='green',command=BookingWindow)
    b2.grid(row=3)

    def exitwindow():
        r.destroy()

    button3 =Button(r,text='EXIT',activebackground="red",command=exitwindow)
    button3.grid(row=6,pady=20)

    r.mainloop()
    



#start of program 
if os.path.isfile(creds):
    Login()
else:
    Signup()

