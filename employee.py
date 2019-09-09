#Employee Management System Usinf Python Tkinter and SQL


from tkinter import *
from tkinter import messagebox as tkMessageBox
from tkinter import messagebox
from tkinter.ttk import Combobox
import sqlite3
from sqlite3 import Error
from tkinter import ttk
from sqlite3 import OperationalError

database = "C:\\Users\\purne\\Desktop\\emp.db"


# functions


def create_connection(db_file):
    try:
        conn = sqlite3.connect(db_file)
        return conn
    except Error as e:
        print(e)

    return None


def create_table(conn, create_table_sql):
    try:
        c = conn.cursor()
        c.execute(create_table_sql)
    except Error as e:
        print(e)


def create_project(conn, project):
    sql = ''' INSERT INTO data(first_name, mid_name, lst_name, employee_id,gender,b_date
               ,email,qualification,work_exp,mob_num,job_title,job_des
               ,address)
              VALUES(?,?,?,?,?,?,?,?,?,?,?,?,?) '''
    cur = conn.cursor()

    cur.execute(sql, project)
    return cur.lastrowid

def search(val):
    reset()
    conn = sqlite3.connect(database)
    c = conn.cursor()
    c.execute("SELECT * FROM 'data'")
    fetch = c.fetchall()
    found = False
    for data in fetch:
        if str(data[3]) == str(val):
            txt_result.config(text="Data Found", fg="green")
            found = True
            enter(data)
        elif str(data[1]) == str(val):
            txt_result.config(text="Data Found", fg="green")
            found = True
            enter(data)
    if not found:
        txt_result.config(text="Data Not Found", fg="red")
    c.close()
    conn.close()


def get_data():
    first_name = name.get()
    mid_name = middle_name.get()
    lst_name = last_name.get()
    employee_id = emp_entry.get()
    gender = str(var.get())
    b_date = str(day.get() + "/" + mon.get() + "/" + year.get())
    email = eentery.get()
    qualification = qual_box.get()
    work_exp = work_entry.get()
    job_title = wrk_post.get()
    mob_num = mentery.get()
    job_des = departmnt.get()
    address = add_entry.get()
    project = [first_name, mid_name, lst_name, employee_id, gender, b_date
        , email, qualification, work_exp, mob_num, job_title, job_des
        , address]
    return project


def read():
    conn = create_connection(database)
    cursor = conn.cursor()
    try:
        tree.delete(*tree.get_children())
        cursor.execute("SELECT * FROM `data`")
        fetch = cursor.fetchall()
        for data in fetch:
            tree.insert('', 'end', values=(data[0], data[1], data[2], data[3], data[4], data[5], data[6]
                                           , data[7], data[8], data[9], data[10], data[11], data[12]))
        cursor.close()
        conn.close()
    except OperationalError:
        pass

def Exit():
    result = tkMessageBox.askquestion('Exit', 'Are you sure you want to exit?', icon="warning")
    if result == 'yes':
        root.destroy()


def update():
    conn = create_connection(database)
    if not tree.selection():
        print("ERROR")
    else:
        if call_me():
            curItem = tree.focus()
            contents = (tree.item(curItem))
            selecteditem = contents['values']
            print("_____________________________")
            print(selecteditem)
            data = get_data()
            sql = ''' UPDATE data SET
                          first_name = ? ,
                          mid_name = ? ,
                          lst_name = ? ,
                          employee_id= ? ,
                          gender= ? ,
                          b_date= ? ,
                          email= ? ,
                          qualification= ?,
                          work_exp= ?,
                          mob_num= ?,
                          job_title= ?,
                          job_des= ? ,
                          address= ?
                          WHERE first_name = ?'''
            data.append(selecteditem[0])
            print(data)
            cur = conn.cursor()
            cur.execute(sql, data)
            conn.commit()
            cur.close()
            conn.close()
            reset()
            read()


def delete():
    conn = create_connection(database)
    cursor = conn.cursor()
    if not tree.selection():
        print("ERROR")
    else:
        result = messagebox.askquestion('Are you sure you want to delete this record?',
                                        icon="warning")
        if result == 'yes':
            curItem = tree.focus()
            print(str(curItem))
            contents = (tree.item(curItem))
            print(contents)
            selecteditem = contents['values']
            print(selecteditem)

            tree.delete(curItem)
            cursor.execute("DELETE FROM data WHERE employee_id = ?", (selecteditem[3],))
            conn.commit()
            cursor.close()
            conn.close()
            reset()
            read()

def f_nameck(self):
    if not f_name.get():
        txt_result.config(text="Please fill the required field!: First Name",fg="red")
    else:
        txt_result.config(text=" ")
        return True
    return False

def m_nameck(self):
    if not m_name.get():
        txt_result.config(text="Please fill the required field!: Middle Name",fg="red")
    else:
        txt_result.config(text=" ")
        return True
    return False

def l_nameck(self):
    if not l_name.get():
        txt_result.config(text="Please fill the required field!: Last Name",fg="red")
    else:
        txt_result.config(text=" ")
        return True
    return False


def IDck(self):
    if not empid.get() or not empid.get().isdigit():
        txt_result.config(text="Please fill the required field!: Employee ID",fg="red")
    else:
        txt_result.config(text="")
        return True
    return False


def dobck(self):
    if day.get() == 'Date' and mon.get() == 'Month' and year.get() == 'Year':
        txt_result.config(text="Please fill the required field!: Date of Birth",fg="red")
    else:
        txt_result.config(text=" ")
        return True
    return False


def genderck(self):
    if not var.get():
        txt_result.config(text="Please fill the required field!: Gender",fg="red")
    else:
        txt_result.config(text=" ")
        return True
    return False


def emailck(self):
    if not eentery.get() or not re.match("^[a-zA-Z0-9_.+-]+@[a-zA-Z0-9-]+\.[a-zA-Z0-9-.]+$", eentery.get(),
                                           re.IGNORECASE):
        txt_result.config(text="Please fill the required field!: EMAIL Address",fg="red")
    else:
        txt_result.config(text=" ")
        return True
    return False


def mobileck(self):
    if not mentery.get() or not re.match("(0/91)?[7-9][0-9]{9}",str(mentery.get())):
        txt_result.config(text="Please fill the required field!: Mobile Number ",fg="red")
    else:
        txt_result.config(text=" ")
        return True
    return False


def workexpck(self):
    if not wrk_exp.get() or not wrk_exp.get().isdigit():
        txt_result.config(text="Please fill the required field!: Work Experience ",fg="red")
    else:
        txt_result.config(text=" ")
        return True
    return False


def Qualificationck(self):
    if quaificn.get()=='Select Qualification':
        txt_result.config(text="Please fill the required field!: Qualification",fg="red")
    else:
        txt_result.config(text=" ")
        return True
    return False


def jobdepartck(self):
    if departmnt.get()=='':
        txt_result.config(text="Please fill the required field!:  Department",fg="red")
    else:
        txt_result.config(text=" ")
        return True
    return False


def jobpostck(self):
    if wrk_post.get()=='':
        txt_result.config(text="Please fill the required field!: Post",fg="red")
    else:
        txt_result.config(text=" ")
        return True
    return False

def addressck(self):
    if not add_entry.get():
        txt_result.config(text="Please fill the required field!: Address",fg="red")
    else:
        txt_result.config(text=" ")
        return True
    return False

def call_me():
    if name.get() == '' and last_name.get() == '' and middle_name.get() == '' and emp_entry.get() == '' and add_entry.get() == '' and mentery.get() == '' and eentery.get() == '' and work_entry.get() == '':
        messagebox.showerror('Error', 'All Details are compulsory')
    elif name.get() == '' and last_name.get() == '' and middle_name.get() == '':
        messagebox.showerror('Error', 'Fill your name')
    elif emp_entry.get() == '' or not emp_entry.get().isdigit():
        messagebox.showerror('Error', 'Fill employee ID')
    elif add_entry.get() == '':
        messagebox.showerror('Error', 'Fill your Address')
    elif mentery.get() == '' or not re.match("(0/91)?[7-9][0-9]{9}", str(mentery.get())):
        messagebox.showerror('Error', 'Fill your Mobile number')
    elif eentery.get() == '' or not re.match("^[a-zA-Z0-9_.+-]+@[a-zA-Z0-9-]+\.[a-zA-Z0-9-.]+$", eentery.get(),
                                             re.IGNORECASE):
        messagebox.showerror('Error', 'Fill your Email ID')
    elif work_entry.get() == ''or not work_entry.get().isdigit():
        messagebox.showerror('Error', 'Fill your Work Experience')
    else:
        messagebox.showinfo('Success', str(name.get()) + ' Your response successfully submitted.')
        return True
    return False


def submit():
    sql_create_projects_table = """ CREATE TABLE IF NOT EXISTS data (first_name TEXT PRIMARY KEY NOT NULL,
                                                                                    mid_name TEXT NOT NULL,
                                                                                    lst_name TEXT NOT NULL,
                                                                                    employee_id TEXT NOT NULL,
                                                                                    gender TEXT NOT NULL,
                                                                                    b_date TEXT NOT NULL,
                                                                                    email TEXT NOT NULL,
                                                                                    qualification TEXT NOT NULL,
                                                                                    work_exp TEXT NOT NULL,
                                                                                    mob_num TEXT NOT NULL,
                                                                                    job_title TEXT NOT NULL,
                                                                                    job_des TEXT NOT NULL,
                                                                                    address TEXT NOT NULL
                                                                                ); """

    # create a database connection
    conn = create_connection(database)
    cursor = conn.cursor()

    if call_me():
        data = get_data()
        if conn is not None:
            # create projects table
            create_table(conn, sql_create_projects_table)
        else:
            print("Error! cannot create the database connection.")

        with conn:
            create_project(conn, data)

    tree.delete(*tree.get_children())
    cursor.execute("SELECT * FROM `data`")
    fetch = cursor.fetchall()
    for data in fetch:
        tree.insert('', 'end', values=(data[0], data[1], data[2], data[3], data[4], data[5], data[6]
                                       , data[7], data[8], data[9], data[10], data[11], data[12]))
    cursor.close()
    conn.close()

def enter(selecteditem):
    reset()

    f_name.set(selecteditem[0])
    m_name.set(selecteditem[1])
    l_name.set(selecteditem[2])
    empid.set(selecteditem[3])

    dob = " ".join(str(x) for x in str(selecteditem[5]).split("/"))
    print(dob)
    dob = list(dob.split(" "))
    year.set(dob[2])
    mon.set(dob[1])
    day.set(dob[0])
    if selecteditem[4] == 'male':
        male.select()
    else:
        female.select()
    Email_id.set(selecteditem[6])
    quaificn.set(selecteditem[7])
    wrk_exp.set(selecteditem[8])
    mob_number.set(selecteditem[9])
    wrk_post.set(selecteditem[10])
    departmnt.set(selecteditem[11])
    address.set(selecteditem[12])


def sel(a):
    curItem = tree.focus()
    contents = (tree.item(curItem))
    selecteditem = contents['values']
    try:
        enter(selecteditem)
    except IndexError:
        pass


def reset():
    f_name.set('')
    l_name.set('')
    m_name.set('')
    empid.set('')
    departmnt.set('')
    address.set('')
    mob_number.set('')
    Email_id.set('')
    day.set('Date')
    mon.set('Month')
    year.set('Year')
    male.deselect()
    female.deselect()
    wrk_exp.set('')
    wrk_post.set('')
    quaificn.set('Select Qualification')


root = Tk()
root.title('Employee System')
lf = LabelFrame(root, text='Employee form', width=450, height=650, font=('bold', 15), relief="raise")
lf.pack(side=LEFT)
Right = Frame(root, width=700, height=500, bd=8, relief="raise")
Right.pack(side=RIGHT)

Name_label = Label(lf, text='Enter your name:', font=('bold', 11))
f_name = StringVar()
name = Entry(lf, textvariable=f_name, bd=5)
l_name = StringVar()
last_name = Entry(lf, textvariable=l_name, bd=5)
m_name = StringVar()
middle_name = Entry(lf, textvariable=m_name, bd=5)
Name_label.place(x=10, y=10)
name.place(x=10, y=40)
name.bind('<FocusOut>', f_nameck)
middle_name.place(x=270, y=40)
middle_name.bind('<FocusOut>', m_nameck)
last_name.place(x=140, y=40)
last_name.bind('<FocusOut>', l_nameck)

empid = IntVar()
emp_id = Label(lf, text='Employee ID:', font=('bold', 11))
emp_id.place(x=10, y=70)
empid.set('')
emp_entry = Entry(lf, textvariable=empid, bd=5)
emp_entry.place(x=10, y=100)
emp_entry.bind('<FocusOut>',IDck)

list2 = ['Production', 'Assembly', 'Quality Control', 'Sales']
departmnt = StringVar()
dlist = Combobox(lf, textvariable=departmnt, value=list2)
departmnt.set('')
dep_label = Label(lf, text="Department:", font=('bold', 11))
dep_label.place(x=200, y=70)
dlist.place(x=200, y=100)
dlist.bind("<<ComboboxSelected>>", jobdepartck)

add_label = Label(lf, text='Address:', font=('bold', 11))
address = StringVar()
add_entry = Entry(lf, textvariable=address, bd=5)
add_label.place(x=10, y=130)
add_entry.place(x=10, y=160, width=400)
add_entry.bind('<FocusOut>', addressck)

Mobile_number = Label(lf, text='Mobile number:', font=('bold', 11))
emailid = Label(lf, text='Email id:', font=('bold', 11))
mob_number = StringVar()
Email_id = StringVar()
mentery = Entry(lf, textvariable=mob_number, bd=5)
eentery = Entry(lf, textvariable=Email_id, bd=5)
mob_number.set('')
Mobile_number.place(x=10, y=190)
emailid.place(x=200, y=190)
mentery.place(x=10, y=220)
mentery.bind('<FocusOut>', mobileck)
eentery.place(x=200, y=220, width=200)
eentery.bind('<FocusOut>', emailck)

d_list = [int(a) for a in range(1, 32)]
day = StringVar()
day_list = Combobox(lf, textvariable=day, value=d_list)
day.set('Date')
mon = StringVar()
m_list = ['JAN', 'FEB', 'MAR', 'APR', 'MAY', 'JUN', 'JUL', 'AUG', 'SEP', 'OCT', 'NOV', 'DEC']
mon_list = Combobox(lf, textvariable=mon, value=m_list)
mon.set('Month')
year = StringVar()
y_list = [int(a) for a in range(1985, 2020)]
year_list = Combobox(lf, textvariable=year, value=y_list)
year.set('Year')
y_label = Label(lf, text='Date Of Birth:', font=('bold', 11))
y_label.place(x=10, y=250)
day_list.place(x=10, y=280)
day_list.bind("<<ComboboxSelected>>", dobck)
mon_list.place(x=150, y=280)
mon_list.bind("<<ComboboxSelected>>", dobck)
year_list.place(x=290, y=280)
year_list.bind("<<ComboboxSelected>>", dobck)
gender_label = Label(lf, text='Select Gender:', font=('bold', 11))
var = StringVar()
male = Radiobutton(lf, text='Male', value='male', variable=var)
ale.deselect()
female = Radiobutton(lf, text='Female', value='female', variable=var)
female.deselect()
gender_label.place(x=10, y=320)
male.place(x=10, y=340)
female.place(x=110, y=340)
male.bind('<FocusOut>', genderck)
female.bind('<FocusOut>', genderck)
workex_label = Label(lf, text='Working Experience:', font=('bold', 11))
wrk_exp = StringVar()
work_entry = Entry(lf, textvariable=wrk_exp, bd=5)
workex_label.place(x=10, y=430)
work_entry.place(x=10, y=450)
work_entry.bind('<FocusOut>', workexpck)
wpost_label = Label(lf, text='Post:', font=('bold', 11))
wp_list = ['Manager', 'S/W Tester', 'Coder', 'Developer', 'Labour']
wrk_post = StringVar()
post_list = Combobox(lf, textvariable=wrk_post, value=wp_list)
wpost_label.place(x=200, y=430)
post_list.place(x=200, y=450)
post_list.bind("<<ComboboxSelected>>", jobpostck)
qual_label = Label(lf, text='Qualification:', font=('bold', 11))
Qualifications = ['SSC', 'HSC', 'DIPLOMA', 'B.E', 'BSC IT', 'M.E', 'PHD']
quaificn = StringVar()
qual_box = Combobox(lf, textvariable=quaificn, value=Qualifications)
quaificn.set('Select Qualification')
qual_label.place(x=10, y=370)
qual_box.place(x=10, y=400)
qual_box.bind("<<ComboboxSelected>>", Qualificationck)
yscroll = Scrollbar(Right)
yscroll.pack(side=RIGHT, fill=Y)
xscroll = Scrollbar(Right, orient="horizontal")
xscroll.pack(side=BOTTOM, fill=X)
style = ttk.Style(Right)
style.theme_use("alt")
style.configure("Treeview",
                fieldbackground="black", foreground="grey")
tree = ttk.Treeview(Right, selectmode="browse", height=100, yscrollcommand=yscroll.set, xscrollcommand=xscroll.set)
tree.pack(side='left')
yscroll.config(command=tree.yview)
xscroll.config(command=tree.xview)
tree["columns"] = (
    "First Name", "Middle Name", "Last Name", "EMPLOYEE ID", "Gender", "DOB", "EMPLOYEE EMAIL", "QUALIFICATION"
    , "WORK EXPERIENCE", "MOBILE NUMBER", "JOB TITLE", "JOB DEPARTMENT"
    , "EMPLOYEE  ADDRESS")
tree['show'] = 'headings'
tree.heading('First Name', text="FIRST NAME", anchor=W)
tree.heading('Middle Name', text="MIDDLE NAME", anchor=W)
tree.heading('Last Name', text="LAST NAME", anchor=W)
tree.heading('EMPLOYEE ID', text="EMPLOYEE ID", anchor=W)
tree.heading('DOB', text="DOB", anchor=W)
tree.heading('Gender', text="Gender", anchor=W)
tree.heading('EMPLOYEE EMAIL', text="EMPLOYEE EMAIL", anchor=W)
tree.heading('QUALIFICATION', text="QUALIFICATION", anchor=W)
tree.heading('WORK EXPERIENCE', text="WORK EXPERIENCE", anchor=W)
tree.heading('MOBILE NUMBER', text="MOBILE NUMBER", anchor=W)
tree.heading('JOB TITLE', text="JOB TITLE", anchor=W)
tree.heading('JOB DEPARTMENT', text="JOB DEPARTMENT", anchor=W)
tree.heading('EMPLOYEE  ADDRESS', text="EMPLOYEE  ADDRESS", anchor=W)
tree.column('#0', stretch=NO, minwidth=0, width=1)
tree.column('#1', stretch=NO, minwidth=0, width=120)
tree.column('#2', stretch=NO, minwidth=0, width=120)
tree.column('#3', stretch=NO, minwidth=0, width=120)
tree.column('#4', stretch=NO, minwidth=0, width=120)
tree.column('#5', stretch=NO, minwidth=0, width=120)
tree.column('#6', stretch=NO, minwidth=0, width=120)
tree.column('#7', stretch=NO, minwidth=0, width=120)
tree.column('#8', stretch=NO, minwidth=0, width=120)
tree.column('#9', stretch=NO, minwidth=0, width=120)
tree.column('#10', stretch=NO, minwidth=0, width=120)
tree.column('#11', stretch=NO, minwidth=0, width=120)
tree.column('#12', stretch=NO, minwidth=0, width=120)
tree.bind('<ButtonRelease-1>', sel)
read()
b1 = Button(lf, text='Add', font=('bold', 11), command=submit, bg='green', fg='white', bd=5)
b1.place(x=0, y=540, width=100, height=30)
b2 = Button(lf, text='Reset', command=reset, bg='brown', fg='white', bd=5, font=('bold', 11))
b2.place(x=220, y=540, width=100, height=30)
exit_button = Button(lf, text="Exit", bg="red", fg='white', font=('bold', 11), border=5, command=Exit)
exit_button.place(x=330, y=580, width=100, height=30)
rvari = StringVar()
r_entry = Entry(lf, textvariable=rvari, bd=5)
r_entry.place(x=0,y=580,width=200,height=30)
search_button = Button(lf, text="Search", bg="grey", fg='white', font=('bold', 11), border=5, command=lambda: search(r_entry.get()))
search_button.place(x=220, y=580, width=100, height=30)
#r_entry.bind('<FocusIn>', txt_result.config(text='Enter Employee name OR Employee ID', fg='black'))
txt_result = Label(lf)
txt_result.place(x=100,y=500)
update = Button(lf, text="Update", bg="green", fg='white', font=('bold', 11), border=5, command=update)
update.place(x=110, y=540, width=100, height=30)

delete_buttn = Button(lf, text="Delete", bg="brown", fg='#feffff', font=('bold', 11), border=5, command=delete)
delete_buttn.place(x=330, y=540, width=100, height=30)
root.mainloop()
