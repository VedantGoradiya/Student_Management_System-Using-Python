def addstudent():
    def submitadd():
        id = idval.get()
        name = nameval.get()
        mob = mobval.get()
        email = emailval.get()
        address = addressval.get()
        gender = genderval.get()
        dob = dobval.get()
        addedtime = time.strftime("%H:%M:%S")
        addeddate = time.strftime("%d/%m/%y")
        try:
            strr = 'insert into studentdata values(%s,%s,%s,%s,%s,%s,%s,%s,%s)'
            mycursor.execute(strr, (id, name, mob, email, address, gender, dob, addeddate, addedtime))
            con.commit()
            res = messagebox.askyesnocancel('Notificatrions',
                                            'Id {} Name {} Added sucessfully.. and want to clean the form'.format(id,
                                                                                                                  name),
                                            parent=addroot)
            if (res == True):
                idval.set('')
                nameval.set('')
                mobval.set('')
                emailval.set('')
                addressval.set('')
                genderval.set('')
                dobval.set('')
        except:
            messagebox.showerror('Notifications', 'Id Already Exist try another id...', parent=addroot)
        strr = 'select * from studentdata'
        mycursor.execute(strr)
        datas = mycursor.fetchall()
        studenttabel.delete(*studenttabel.get_children())
        for i in datas:
            vv = [i[0], i[1], i[2], i[3], i[4], i[5], i[6], i[7], i[8]]
            studenttabel.insert('', END, values=vv)

    addroot = Toplevel(master=DataEntryFrame)
    addroot.grab_set()
    addroot.geometry('470x470+70+150')
    addroot.title('Student Management System')
    addroot.config(bg='blue')
    addroot.resizable(False, False)
    ############################################################### add student label

    idlabel = Label(addroot, text='Enter Id :', bg='gold2', font=('times', 20, 'bold'), relief=GROOVE, borderwidth=3,
                    width=12, anchor='w')
    idlabel.place(x=10, y=10)

    namelabel = Label(addroot, text='Enter Name :', bg='gold2', font=('times', 20, 'bold'), relief=GROOVE,
                      borderwidth=3, width=12, anchor='w')
    namelabel.place(x=10, y=70)

    mobilelabel = Label(addroot, text='Enter Mobile :', bg='gold2', font=('times', 20, 'bold'), relief=GROOVE,
                        borderwidth=3, width=12, anchor='w')
    mobilelabel.place(x=10, y=130)

    emaillabel = Label(addroot, text='Enter Email :', bg='gold2', font=('times', 20, 'bold'), relief=GROOVE,
                       borderwidth=3, width=12, anchor='w')
    emaillabel.place(x=10, y=190)

    addresslabel = Label(addroot, text='Enter Address :', bg='gold2', font=('times', 20, 'bold'), relief=GROOVE,
                         borderwidth=3, width=12, anchor='w')
    addresslabel.place(x=10, y=250)

    genderlabel = Label(addroot, text='Enter Gender :', bg='gold2', font=('times', 20, 'bold'), relief=GROOVE,
                        borderwidth=3, width=12, anchor='w')
    genderlabel.place(x=10, y=310)

    doblabel = Label(addroot, text='Enter D.O.B :', bg='gold2', font=('times', 20, 'bold'), relief=GROOVE,
                     borderwidth=3, width=12, anchor='w')
    doblabel.place(x=10, y=370)

    ################################################################ student entry box
    idval = StringVar()
    nameval = StringVar()
    mobval = StringVar()
    emailval = StringVar()
    addressval = StringVar()
    genderval = StringVar()
    dobval = StringVar()

    identry = Entry(addroot, font=('roman', 15, 'bold'), bd=5, textvariable=idval)
    identry.place(x=250, y=10)

    nameentry = Entry(addroot, font=('roman', 15, 'bold'), bd=5, textvariable=nameval)
    nameentry.place(x=250, y=70)

    mobileentry = Entry(addroot, font=('roman', 15, 'bold'), bd=5, textvariable=mobval)
    mobileentry.place(x=250, y=130)

    emailentry = Entry(addroot, font=('roman', 15, 'bold'), bd=5, textvariable=emailval)
    emailentry.place(x=250, y=190)

    addressentry = Entry(addroot, font=('roman', 15, 'bold'), bd=5, textvariable=addressval)
    addressentry.place(x=250, y=250)

    genderentry = Entry(addroot, font=('roman', 15, 'bold'), bd=5, textvariable=genderval)
    genderentry.place(x=250, y=310)

    dobentry = Entry(addroot, font=('roman', 15, 'bold'), bd=5, textvariable=dobval)
    dobentry.place(x=250, y=370)

    ##################################################### add button

    sumbmitbtn = Button(addroot, text='Submit', font=('roman', 15, 'bold'), width=20, bd=5, bg='red', command=submitadd)
    sumbmitbtn.place(x=150, y=420)

    addroot.mainloop()


def searchstudent():
    def search():
        global mycursor
        id = idval.get()
        name = nameval.get()
        mob = mobval.get()
        email = emailval.get()
        address = addressval.get()
        gender = genderval.get()
        dob = dobval.get()
        addeddate = time.strftime("%d/%m/%y")
        if(id != ''):
            strr = 'select *from studentdata where id=%s'
            mycursor.execute(strr,(id))
            datas = mycursor.fetchall()
            studenttabel.delete(*studenttabel.get_children())
            for i in datas:
                vv = [i[0], i[1], i[2], i[3], i[4], i[5], i[6], i[7], i[8]]
                studenttabel.insert('', END, values=vv)
        elif(name != ''):
            strr = 'select *from studentdata where name=%s'
            mycursor.execute(strr,(name))
            datas = mycursor.fetchall()
            studenttabel.delete(*studenttabel.get_children())
            for i in datas:
                vv = [i[0], i[1], i[2], i[3], i[4], i[5], i[6], i[7], i[8]]
                studenttabel.insert('', END, values=vv)
        elif (mob != ''):
            strr = 'select *from studentdata where mobile=%s'
            mycursor.execute(strr,(mob))
            datas = mycursor.fetchall()
            studenttabel.delete(*studenttabel.get_children())
            for i in datas:
                vv = [i[0], i[1], i[2], i[3], i[4], i[5], i[6], i[7], i[8]]
                studenttabel.insert('', END, values=vv)
        elif(email != ''):
            strr = 'select *from studentdata where email=%s'
            mycursor.execute(strr,(email))
            datas = mycursor.fetchall()
            studenttabel.delete(*studenttabel.get_children())
            for i in datas:
                vv = [i[0], i[1], i[2], i[3], i[4], i[5], i[6], i[7], i[8]]
                studenttabel.insert('', END, values=vv)
        elif(address != ''):
            strr = 'select *from studentdata where address=%s'
            mycursor.execute(strr,(address))
            datas = mycursor.fetchall()
            studenttabel.delete(*studenttabel.get_children())
            for i in datas:
                vv = [i[0], i[1], i[2], i[3], i[4], i[5], i[6], i[7], i[8]]
                studenttabel.insert('', END, values=vv)
        elif(gender != ''):
            strr = 'select *from studentdata where gender=%s'
            mycursor.execute(strr,(gender))
            datas = mycursor.fetchall()
            studenttabel.delete(*studenttabel.get_children())
            for i in datas:
                vv = [i[0], i[1], i[2], i[3], i[4], i[5], i[6], i[7], i[8]]
                studenttabel.insert('', END, values=vv)
        elif(dob != ''):
            strr = 'select *from studentdata where dob=%s'
            mycursor.execute(strr,(dob))
            datas = mycursor.fetchall()
            studenttabel.delete(*studenttabel.get_children())
            for i in datas:
                vv = [i[0], i[1], i[2], i[3], i[4], i[5], i[6], i[7], i[8]]
                studenttabel.insert('', END, values=vv)

        elif(addeddate != ''):
            strr = 'select *from studentdata where addeddate=%s'
            mycursor.execute(strr,(addeddate))
            datas = mycursor.fetchall()
            studenttabel.delete(*studenttabel.get_children())
            for i in datas:
                vv = [i[0], i[1], i[2], i[3], i[4], i[5], i[6], i[7], i[8]]
                studenttabel.insert('', END, values=vv)

    searchroot = Toplevel(master=DataEntryFrame)
    searchroot.grab_set()
    searchroot.geometry('475x540+70+100')
    searchroot.title('Student Management System')
    searchroot.config(bg='blue')
    searchroot.resizable(False, False)
    ############################################################### add student label

    idlabel = Label(searchroot, text='Enter Id :', bg='gold2', font=('times', 20, 'bold'), relief=GROOVE, borderwidth=3,
                    width=12, anchor='w')
    idlabel.place(x=10, y=10)

    namelabel = Label(searchroot, text='Enter Name :', bg='gold2', font=('times', 20, 'bold'), relief=GROOVE,
                      borderwidth=3, width=12, anchor='w')
    namelabel.place(x=10, y=70)

    mobilelabel = Label(searchroot, text='Enter Mobile :', bg='gold2', font=('times', 20, 'bold'), relief=GROOVE,
                        borderwidth=3, width=12, anchor='w')
    mobilelabel.place(x=10, y=130)

    emaillabel = Label(searchroot, text='Enter Email :', bg='gold2', font=('times', 20, 'bold'), relief=GROOVE,
                       borderwidth=3, width=12, anchor='w')
    emaillabel.place(x=10, y=190)

    addresslabel = Label(searchroot, text='Enter Address :', bg='gold2', font=('times', 20, 'bold'), relief=GROOVE,
                         borderwidth=3, width=12, anchor='w')
    addresslabel.place(x=10, y=250)

    genderlabel = Label(searchroot, text='Enter Gender :', bg='gold2', font=('times', 20, 'bold'), relief=GROOVE,
                        borderwidth=3, width=12, anchor='w')
    genderlabel.place(x=10, y=310)

    doblabel = Label(searchroot, text='Enter D.O.B :', bg='gold2', font=('times', 20, 'bold'), relief=GROOVE,
                     borderwidth=3, width=12, anchor='w')
    doblabel.place(x=10, y=370)

    datelabel = Label(searchroot, text='Enter Date :', bg='gold2', font=('times', 20, 'bold'), relief=GROOVE,
                      borderwidth=3, width=12, anchor='w')
    datelabel.place(x=10, y=430)

    ################################################################ student entry box
    idval = StringVar()
    nameval = StringVar()
    mobval = StringVar()
    emailval = StringVar()
    addressval = StringVar()
    genderval = StringVar()
    dobval = StringVar()
    dateval = StringVar()

    identry = Entry(searchroot, font=('roman', 15, 'bold'), bd=5, textvariable=idval)
    identry.place(x=250, y=10)

    nameentry = Entry(searchroot, font=('roman', 15, 'bold'), bd=5, textvariable=nameval)
    nameentry.place(x=250, y=70)

    mobileentry = Entry(searchroot, font=('roman', 15, 'bold'), bd=5, textvariable=mobval)
    mobileentry.place(x=250, y=130)

    emailentry = Entry(searchroot, font=('roman', 15, 'bold'), bd=5, textvariable=emailval)
    emailentry.place(x=250, y=190)

    addressentry = Entry(searchroot, font=('roman', 15, 'bold'), bd=5, textvariable=addressval)
    addressentry.place(x=250, y=250)

    genderentry = Entry(searchroot, font=('roman', 15, 'bold'), bd=5, textvariable=genderval)
    genderentry.place(x=250, y=310)

    dobentry = Entry(searchroot, font=('roman', 15, 'bold'), bd=5, textvariable=dobval)
    dobentry.place(x=250, y=370)

    dateentry = Entry(searchroot, font=('roman', 15, 'bold'), bd=5, textvariable=dateval)
    dateentry.place(x=250, y=430)

    ##################################################### add button

    sumbmitbtn = Button(searchroot, text='Submit', font=('roman', 15, 'bold'), width=20, bd=5, bg='red', command=search)
    sumbmitbtn.place(x=150, y=480)

    searchroot.mainloop()


def deletestudent():
    cc = studenttabel.focus()
    content = studenttabel.item(cc)
    pp = content['values'][0]
    strr = 'delete from studentdata where id=%s'
    mycursor.execute(strr,(pp))
    con.commit()
    messagebox.showinfo('Notifications','Id {} deleted sucessfully...'.format(pp))
    strr = 'select *from studentdata'
    mycursor.execute(strr)
    datas = mycursor.fetchall()
    studenttabel.delete(*studenttabel.get_children())
    for i in datas:
        vv = [i[0], i[1], i[2], i[3], i[4], i[5], i[6], i[7], i[8]]
        studenttabel.insert('', END, values=vv)


def updatestudent():
    def update():
        id = idval.get()
        name = nameval.get()
        mobile = mobval.get()
        email = emailval.get()
        address = addressval.get()
        gender = genderval.get()
        dob = dobval.get()
        date = dateval.get()
        time = timeval.get()

        strr = 'update studentdata set name=%s,mobile=%s,email=%s,address=%s,gender=%s,dob=%s,date=%s,time=%s where id=%s'
        mycursor.execute(strr,(name,mobile,email,address,gender,dob,date,time,id))
        con.commit()
        messagebox.showinfo('Notifications', 'Id {} Modified sucessfully...'.format(id),parent=updateroot)
        strr = 'select *from studentdata'
        mycursor.execute(strr)
        datas = mycursor.fetchall()
        studenttabel.delete(*studenttabel.get_children())
        for i in datas:
            vv = [i[0], i[1], i[2], i[3], i[4], i[5], i[6], i[7], i[8]]
            studenttabel.insert('', END, values=vv)

    updateroot = Toplevel(master=DataEntryFrame)
    updateroot.grab_set()
    updateroot.geometry('500x585+70+50')
    updateroot.title('Student Management System')
    updateroot.config(bg='blue')
    updateroot.resizable(False, False)
    ############################################################### add student label

    idlabel = Label(updateroot, text='Enter Id :', bg='gold2', font=('times', 20, 'bold'), relief=GROOVE, borderwidth=3,
                    width=12, anchor='w')
    idlabel.place(x=10, y=10)

    namelabel = Label(updateroot, text='Enter Name :', bg='gold2', font=('times', 20, 'bold'), relief=GROOVE,
                      borderwidth=3, width=12, anchor='w')
    namelabel.place(x=10, y=70)

    mobilelabel = Label(updateroot, text='Enter Mobile :', bg='gold2', font=('times', 20, 'bold'), relief=GROOVE,
                        borderwidth=3, width=12, anchor='w')
    mobilelabel.place(x=10, y=130)

    emaillabel = Label(updateroot, text='Enter Email :', bg='gold2', font=('times', 20, 'bold'), relief=GROOVE,
                       borderwidth=3, width=12, anchor='w')
    emaillabel.place(x=10, y=190)

    addresslabel = Label(updateroot, text='Enter Address :', bg='gold2', font=('times', 20, 'bold'), relief=GROOVE,
                         borderwidth=3, width=12, anchor='w')
    addresslabel.place(x=10, y=250)

    genderlabel = Label(updateroot, text='Enter Gender :', bg='gold2', font=('times', 20, 'bold'), relief=GROOVE,
                        borderwidth=3, width=12, anchor='w')
    genderlabel.place(x=10, y=310)

    doblabel = Label(updateroot, text='Enter D.O.B :', bg='gold2', font=('times', 20, 'bold'), relief=GROOVE,
                     borderwidth=3, width=12, anchor='w')
    doblabel.place(x=10, y=370)

    datelabel = Label(updateroot, text='Enter Date :', bg='gold2', font=('times', 20, 'bold'), relief=GROOVE,
                      borderwidth=3, width=12, anchor='w')
    datelabel.place(x=10, y=430)

    timelabel = Label(updateroot, text='Enter Time :', bg='gold2', font=('times', 20, 'bold'), relief=GROOVE,
                      borderwidth=3, width=12, anchor='w')
    timelabel.place(x=10, y=490)

    ################################################################ student entry box
    idval = StringVar()
    nameval = StringVar()
    mobval = StringVar()
    emailval = StringVar()
    addressval = StringVar()
    genderval = StringVar()
    dobval = StringVar()
    dateval = StringVar()
    timeval = StringVar()

    identry = Entry(updateroot, font=('roman', 15, 'bold'), bd=5, textvariable=idval)
    identry.place(x=250, y=10)

    nameentry = Entry(updateroot, font=('roman', 15, 'bold'), bd=5, textvariable=nameval)
    nameentry.place(x=250, y=70)

    mobileentry = Entry(updateroot, font=('roman', 15, 'bold'), bd=5, textvariable=mobval)
    mobileentry.place(x=250, y=130)

    emailentry = Entry(updateroot, font=('roman', 15, 'bold'), bd=5, textvariable=emailval)
    emailentry.place(x=250, y=190)

    addressentry = Entry(updateroot, font=('roman', 15, 'bold'), bd=5, textvariable=addressval)
    addressentry.place(x=250, y=250)

    genderentry = Entry(updateroot, font=('roman', 15, 'bold'), bd=5, textvariable=genderval)
    genderentry.place(x=250, y=310)

    dobentry = Entry(updateroot, font=('roman', 15, 'bold'), bd=5, textvariable=dobval)
    dobentry.place(x=250, y=370)

    dateentry = Entry(updateroot, font=('roman', 15, 'bold'), bd=5, textvariable=dateval)
    dateentry.place(x=250, y=430)

    timeentry = Entry(updateroot, font=('roman', 15, 'bold'), bd=5, textvariable=timeval)
    timeentry.place(x=250, y=490)

    ##################################################### add button

    sumbmitbtn = Button(updateroot, text='Submit', font=('roman', 15, 'bold'), width=20, bd=5, bg='red', command=update)
    sumbmitbtn.place(x=150, y=540)

    cc = studenttabel.focus()
    content = studenttabel.item(cc)
    pp = content['values']
    if(len(pp) != 0):
        idval.set(pp[0])
        nameval.set(pp[1])
        mobval.set(pp[2])
        emailval.set(pp[3])
        addressval.set(pp[4])
        genderval.set(pp[5])
        dobval.set(pp[6])
        dateval.set(pp[7])
        timeval.set(pp[8])


    updateroot.mainloop()


def showstudent():
    strr = 'select *from studentdata'
    mycursor.execute(strr)
    datas = mycursor.fetchall()
    studenttabel.delete(*studenttabel.get_children())
    for i in datas:
        vv = [i[0], i[1], i[2], i[3], i[4], i[5], i[6], i[7], i[8]]
        studenttabel.insert('', END, values=vv)


def exportstudent():
    print('Student Exported')


def exitstudent():
    res = messagebox.askyesnocancel('Notification', 'Do you want to exit?')
    if (res == True):
        root.destroy()


################################################################## connection function
def Connectdb():
    def submitdb():
        global con, mycursor
        host = hostval.get()
        user = userval.get()
        password = passwordval.get()
        try:
            con = pymysql.connect(host=host, user=user, password=password)
            mycursor = con.cursor()
        except:
            messagebox.showerror('Notifications', 'Data is incorrect please try again', parent=dbroot)
            return
        try:
            strr = 'create database studentmanagementsystem'
            mycursor.execute(strr)
            strr = 'use studentmanagementsystem'
            mycursor.execute(strr)
            strr = 'create table studentdata(id int,name varchar(20),mobile varchar(12),email varchar(30),address varchar(100),gender varchar(50),dob varchar(50),date varchar(50),time varchar(50))'
            mycursor.execute(strr)
            strr = 'alter table studentdata modify column id int not null'
            mycursor.execute(strr)
            strr = 'alter table studentdata modify column id int primary key'
            mycursor.execute(strr)
            messagebox.showinfo('Notification',
                                'database created and now you are connected connected to the database ....',
                                parent=dbroot)

        except:
            strr = 'use studentmanagementsystem'
            mycursor.execute(strr)
            messagebox.showinfo('Notification', 'Now you are connected to the database ....', parent=dbroot)
        dbroot.destroy()

    dbroot = Toplevel()
    dbroot.grab_set()
    dbroot.geometry('470x250+680+230')
    dbroot.resizable(False, False)
    dbroot.config(bg='grey')

    #################################################################### creating label

    hostlabel = Label(dbroot, text='Enter Host:', bg='gold2', font=('times', 20, 'bold'), relief=GROOVE, borderwidth=3,
                      width=12, anchor='w')
    hostlabel.place(x=10, y=10)

    userlabel = Label(dbroot, text='Enter User:', bg='gold2', font=('times', 20, 'bold'), relief=GROOVE, borderwidth=3,
                      width=12, anchor='w')
    userlabel.place(x=10, y=70)

    passwordlabel = Label(dbroot, text='Enter Password:', bg='gold2', font=('times', 20, 'bold'), relief=GROOVE,
                          borderwidth=3, width=12, anchor='w')
    passwordlabel.place(x=10, y=130)

    ####################################################################### creating entry label

    hostval = StringVar()
    userval = StringVar()
    passwordval = StringVar()

    hostentry = Entry(dbroot, font=('roman', 15, 'bold'), bd=5, textvariable=hostval)
    hostentry.place(x=250, y=10)

    userentry = Entry(dbroot, font=('roman', 15, 'bold'), bd=5, textvariable=userval)
    userentry.place(x=250, y=70)

    passwordentry = Entry(dbroot, font=('roman', 15, 'bold'), bd=5, textvariable=passwordval)
    passwordentry.place(x=250, y=130)

    #################################################### submit button

    subitbutton = Button(dbroot, text='Submit', font=('roman', 15, 'bold'), widt=20, bd=5, command=submitdb)
    subitbutton.place(x=150, y=190)

    dbroot.mainloop()


############################################################## clock function
def tick():
    date_string = time.strftime("%d/%m/%y")
    time_string = time.strftime("%H/%M")
    clock.config(text="Date :" + date_string + "\n" + "Time :" + time_string)
    clock.after(200, tick)

#########################################################################################  main
from tkinter import *
from tkinter import Toplevel, messagebox
from tkinter.ttk import Treeview
from tkinter import ttk
import pymysql
import time



root = Tk()
root.title('Student Management System')
root.config(bg='gold2')
root.geometry('1174x640+50+0')
root.resizable(False, False)

######################################################################### Data entry Frame

DataEntryFrame = Frame(root, bg='gold2', relief=GROOVE, borderwidth=5)
DataEntryFrame.place(x=10, y=80, width=500, height=560)

frontlabel = Label(DataEntryFrame, text='**************** Welcome ****************', width=30,
                   font=('arial', 22, 'italic bold'), bg='gold2')
frontlabel.pack(side=TOP, expand=True)

addbtn = Button(DataEntryFrame, text='1. Add Student', width=24, font=('chiller', 20, 'bold'), bd=6, bg='skyblue3',
                relief=RIDGE, command=addstudent)
addbtn.pack(side=TOP, expand=True)

searchbtn = Button(DataEntryFrame, text='2. Search Student', width=24, font=('chiller', 20, 'bold'), bd=6,
                   bg='skyblue3', relief=RIDGE, command=searchstudent)
searchbtn.pack(side=TOP, expand=True)

deletebtn = Button(DataEntryFrame, text='3. Delete Student', width=24, font=('chiller', 20, 'bold'), bd=6,
                   bg='skyblue3', relief=RIDGE, command=deletestudent)
deletebtn.pack(side=TOP, expand=True)

updatebtn = Button(DataEntryFrame, text='4. Update Student', width=24, font=('chiller', 20, 'bold'), bd=6,
                   bg='skyblue3', relief=RIDGE, command=updatestudent)
updatebtn.pack(side=TOP, expand=True)

showallbtn = Button(DataEntryFrame, text='5. Show All Student', width=24, font=('chiller', 20, 'bold'), bd=6,
                    bg='skyblue3', relief=RIDGE, command=showstudent)
showallbtn.pack(side=TOP, expand=True)

exportdatabtn = Button(DataEntryFrame, text='6. Export Data ', width=24, font=('chiller', 20, 'bold'), bd=6,
                       bg='skyblue3', relief=RIDGE, command=exportstudent)
exportdatabtn.pack(side=TOP, expand=True)

exitbtn = Button(DataEntryFrame, text='7. Exit', width=24, font=('chiller', 20, 'bold'), bd=6, bg='skyblue3',
                 relief=RIDGE, command=exitstudent)
exitbtn.pack(side=TOP, expand=True)

######################################################################### Show data frame

ShowDataFrame = Frame(root, bg='gold2', relief=GROOVE, borderwidth=5)
ShowDataFrame.place(x=550, y=80, width=620, height=560)

style = ttk.Style()
style.configure('Treeview.Heading', font=('chiller', 20, 'bold'), foreground='black')
style.configure('Treeview', font=('times', 15, 'bold'), foreground='black')
scroll_x = Scrollbar(ShowDataFrame, orient=HORIZONTAL)
scroll_y = Scrollbar(ShowDataFrame, orient=VERTICAL)
studenttabel = Treeview(ShowDataFrame, column=(
'Id', 'Name', 'Mobile No', 'Email', 'Address', 'Gender', 'D.O.B', 'Added Date', 'Added Time'),
                        yscrollcommand=scroll_y.set, xscrollcommand=scroll_x.set)
scroll_x.pack(side=BOTTOM, fill=X)
scroll_y.pack(side=RIGHT, fill=Y)
scroll_x.config(command=studenttabel.xview)
scroll_y.config(command=studenttabel.yview)
studenttabel.heading('Id', text='Id')
studenttabel.heading('Name', text='Name')
studenttabel.heading('Mobile No', text='Mobile N0')
studenttabel.heading('Email', text='Email')
studenttabel.heading('Address', text='Address')
studenttabel.heading('Gender', text='Gender')
studenttabel.heading('D.O.B', text='D.O.B')
studenttabel.heading('Added Date', text='Added Data')
studenttabel.heading('Added Time', text='Added Time')
studenttabel['show'] = 'headings'
studenttabel.column('Id', width=100)
studenttabel.column('Name', width=200)
studenttabel.column('Mobile No', width=200)
studenttabel.column('Email', width=300)
studenttabel.column('Address', width=200)
studenttabel.column('Gender', width=100)
studenttabel.column('D.O.B', width=150)
studenttabel.column('Added Date', width=150)
studenttabel.column('Added Time', width=150)
studenttabel.pack(fill=BOTH, expand=1)

######################################################################### slider

ss = 'Welcome To Student Management System'
count = 0
text = ''

######################################################################### Decoration slide bar

SliderLabel1 = Label(root, text=ss, font=('chiller', 30, 'italic bold'), relief=RIDGE, borderwidth=5, width=34)
SliderLabel1.place(x=145, y=0)

############################################################################ clock
clock = Label(root, font=('times', 14, 'bold'), relief=RIDGE, borderwidth=4)
clock.place(x=0, y=0)
tick()

######################################################################### data base button

connectionbutton = Button(root, text='Connect DB',width=10, font=('chiller', 20, 'italic bold'), relief=RIDGE,
                          borderwidth=4, bd=6, command=Connectdb,)
connectionbutton.place(x=985, y=0)
root.mainloop()
