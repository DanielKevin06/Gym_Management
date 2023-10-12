from tkinter import *
from tkinter import messagebox
from tkinter import ttk
from PIL import ImageTk
import mysql.connector

signup_window=Tk()
screen_width = signup_window.winfo_screenwidth()
screen_height = signup_window.winfo_screenheight()
signup_window.geometry('1280x720+50+50')
signup_window.resizable(0,0)
bgImage = ImageTk.PhotoImage(file = 'Final.jpg')

bgLabel=Label(signup_window, image=bgImage)
bgLabel.grid()

signup_window.title('Sign Up Page')
signup_window.configure(bg='white')


def login():
    signup_window.destroy()
    import login_page


def sign_up():
    if user_entry.get() == '' or email_entry.get() == '' or password_entry.get() == '' or confirm_entry.get() == '' or number_entry.get() == '' or location_entry.get() == '':
        messagebox.showerror('Error', 'All fields are required.')
    elif password_entry.get() != confirm_entry.get():
        messagebox.showerror('Error', 'Password Mismatched')
    elif check.get() == 0:
        messagebox.showerror('Error', 'Please accept the Terms and Conditions.')  
    elif gender.get()==1:
       gGender = 'Male'
        
    elif gender.get()==2:
       gGender = 'Female'
           
    elif gender.get()== 3:
        gGender = 'Other'
               
    gName = user_entry.get()
    gEmail = email_entry.get()
    gPassword = password_entry.get()
    gNumber = number_entry.get()
    gLocation = location_entry.get()
    
    # db={
    #         "host" : "localhost",
    #         "user" : "root",
    #         "password" : "",
    #         "database" : "gym management"
    #     }
    
        
    try:
        db={
            "host" : "localhost",
            "user" : "root",
            "password" : "",
            "database" : "gym management"
        }
        conn = mysql.connector.connect(**db)
        print("The Database is connected Successfully")
        cursor = conn.cursor()
    except mysql.connector.Error as e :
        print("The Connection is Unsuccessful, Please try again Later")
        messagebox.showerror('Connection Unsuccessful',f"Unable to connect to {e}")
        return    
    query = "SELECT * FROM users WHERE user_name=%s"
    cursor.execute(query,(user_entry.get()))
    row = cursor.fetchone()
    if row != None:
        messagebox.showerror('Error', 'User name already exists')
    else :    
        sql="INSERT INTO users(user_name, user_email, user_password,user_gender, user_number, user_location) VALUES (%s,%s,%s,%s,%s,%s);"
        data = (gName,gEmail,gPassword,gGender, gNumber,gLocation)
        cursor.execute(sql,data)
        messagebox.showinfo('Details Stored',"Your details have been stored successfully.")
        conn.commit()
        conn.close()
        cursor.close()
        user_entry.delete(0, END)
        email_entry.delete(0, END)
        password_entry.delete(0, END)
                #gender.delete(0, END)
        number_entry.delete(0, END)
        location_entry.delete(0, END)
        signup_window.destroy()
        import login_page
            

    
frame=Frame(signup_window, bg='white')
frame.place(x=864,y=93)

heading = Label(frame, text = 'CREATE AN ACCOUNT', font=('Microsoft Yahei UI Light',18,'bold'), bd=0,
                bg='white',activebackground='white', fg= 'tomato3')
heading.grid(row=0, column=0, padx=46, pady=10)

#User Name
user_name = Label(frame, text = 'User Name :',font=('Microsoft Yahei UI Light',10,'bold'), bd=0,
                bg='white',activebackground='white', fg= 'tomato3')
user_name.grid(row=1, column=0, sticky='w', padx=25, pady=(10,0))

user_entry = Entry(frame, width=39, font=('Microsoft Yahei UI Light',10,'bold'), bd=0,
                bg='tomato3',fg= 'white')
user_entry.grid(row=2, column=0, sticky='w', padx=25)

#Email
email = Label(frame, text = 'Email :',font=('Microsoft Yahei UI Light',10,'bold'), bd=0,
                bg='white',activebackground='white', fg= 'tomato3')
email.grid(row=3, column=0, sticky='w', padx=25,pady=(10,0))

email_entry = Entry(frame, width=39, font=('Microsoft Yahei UI Light',10,'bold'), bd=0,
                bg='tomato3',fg= 'white')
email_entry.grid(row=4, column=0, sticky='w', padx=25)

#Password
password = Label(frame, text = 'Password :',font=('Microsoft Yahei UI Light',10,'bold'), bd=0,
                bg='white',activebackground='white', fg= 'tomato3')
password.grid(row=5, column=0, sticky='w', padx=25,pady=(10,0))

password_entry = Entry(frame, width=39, font=('Microsoft Yahei UI Light',10,'bold'), bd=0,
                bg='tomato3',fg= 'white')
password_entry.grid(row=6, column=0, sticky='w', padx=25)

confirm = Label(frame, text = 'Confirm Password :',font=('Microsoft Yahei UI Light',10,'bold'), bd=0,
                bg='white',activebackground='white', fg= 'tomato3')
confirm.grid(row=7, column=0, sticky='w', padx=25,pady=(10,0))

confirm_entry = Entry(frame, width=39, font=('Microsoft Yahei UI Light',10,'bold'), bd=0,
                bg='tomato3',fg= 'white')
confirm_entry.grid(row=8, column=0, sticky='w', padx=25)

#Gender
# gender=ttk.Combobox(frame, values=["Male", "Female", "Other"])
# gender=ttk.Combobox(font=('Microsoft Yahei UI Light',10,'bold'), bd=0,
#                 bg='white',activebackground='white', fg= 'tomato3')
# gender.set("Gender")
# gender.grid(row=9, column=0, sticky='w', padx=25, pady=(10,0))
gender = IntVar()
gender_m = Radiobutton(frame, text = 'Male', variable = gender, value = 1, font=('Microsoft Yahei UI Light',10,'bold'), bd=0,
                bg='white',fg= 'tomato3',activeforeground='tomato3' )
gender_m.grid(row=9, column=0, sticky='w', padx=25, pady=(10,0))

gender_f = Radiobutton(frame, text = 'Female', variable = gender, value = 2, font=('Microsoft Yahei UI Light',10,'bold'), bd=0,
                bg='white',fg= 'tomato3',activeforeground='tomato3')
gender_f.grid(row=9, column=0, pady=(10,0))

gender_o = Radiobutton(frame, text = 'Other', variable = gender, value = 3, font=('Microsoft Yahei UI Light',10,'bold'), bd=0,
                bg='white',fg= 'tomato3',activeforeground='tomato3')
gender_o.grid(row=9, column=0,padx=(246,0), pady=(10,0))

#Contact Number
number = Label(frame, text = 'Contact Number :',font=('Microsoft Yahei UI Light',10,'bold'), bd=0,
                bg='white',activebackground='white', fg= 'tomato3')
number.grid(row=10, column=0, sticky='w', padx=25,pady=(10,0))

number_entry = Entry(frame, width=39, font=('Microsoft Yahei UI Light',10,'bold'), bd=0,
                bg='tomato3',fg= 'white')
number_entry.grid(row=11, column=0, sticky='w', padx=25)

#Location
location = Label(frame, text = 'Location :',font=('Microsoft Yahei UI Light',10,'bold'), bd=0,
                bg='white',activebackground='white', fg= 'tomato3')
location.grid(row=12, column=0, sticky='w', padx=25,pady=(10,0))

location_entry = Entry(frame, width=39, font=('Microsoft Yahei UI Light',10,'bold'), bd=0,
                bg='tomato3',fg= 'white')
location_entry.grid(row=13, column=0, sticky='w', padx=25)

#terms
check = IntVar()
termsandconditions= Checkbutton(frame,text = 'I agree to the Terms and Conditions',font=('Microsoft Yahei UI Light',10,'bold'),
                bg='white',activebackground='white', fg= 'tomato3',activeforeground='tomato3', cursor='hand2', variable = check)
termsandconditions.grid(row=14, column=0, sticky='w', padx=25)

# signup
signup_btn = Button(frame, text='SIGNUP', font=('Times New Roman',16,'bold'),
                      fg='white', bg='tomato3',activebackground='tomato3',activeforeground='white', cursor='hand2', bd=0, width=26, command = sign_up)
signup_btn.grid(row=15, column=0, sticky='w', padx=25)

#Have an account
Have_acc = Label(frame,text = 'Already have an account ?',font=('Microsoft Yahei UI Light',10,'bold'), bd=0,
                bg='white',fg= 'tomato3')
Have_acc.grid(row=16, column=0, sticky='w', padx=25, pady=(10,0))

#link
login_btn = Button(frame, text='Log in',font=('Microsoft Yahei UI Light',10,'bold underline'), bd=0,
                bg='white',fg= 'blue', cursor='hand2', activebackground='white',activeforeground='blue', command= login)
login_btn.grid(row=16, column=0,padx=(100,0), pady=(10,0))

signup_window.mainloop()