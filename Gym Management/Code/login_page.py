from tkinter import *
from tkinter import messagebox
from tkinter import ttk
from PIL import ImageTk
import mysql.connector

#Login Window
window=Tk()
screen_width = window.winfo_screenwidth()
screen_height = window.winfo_screenheight()
window.geometry('1280x720+50+50')
window.resizable(0,0)
bgImage = ImageTk.PhotoImage(file = 'Final.jpg')

bgLabel=Label(window, image=bgImage, bd = 0,)
bgLabel.place(x=0,y=0)
# bgLabel.pack(side='top', fill='both', expand='yes')

window.title('Login Page')
window.configure(bg='grey')

#To get the User's Data
# def get_data():
#     a = user_entry.get()
#     print(a)
#     b = password_entry.get()
#     print(b)

#Enter Function

def forget():
    window1 = Toplevel()
    window1.title('Change password')
    
    window1.mainloop()
def Login():
    print(user_entry.get())
    print(password_entry.get())
    if user_entry.get()=='' or password_entry.get == '':
        messagebox.showerror('Error', 'All fields are required')
    else:
        try:
            db={
                "host" : "localhost",
                "user" : "root",
                "password" : "",
                "database" : "gym management"
            }
            print("Executing the Try Block...")
            conn = mysql.connector.connect(**db)
            print("The Database is connected Successfully")
            cursor = conn.cursor()
            query = "SELECT * FROM users WHERE user_name=%s AND user_password=%s"
            cursor.execute(query, (user_entry.get(),password_entry.get()))
            row=cursor.fetchone()
            print(row)
            if row==None:
            
                messagebox.showerror('Error', 'Invalid Username or Password')
            else:
                messagebox.showinfo('Welcome', 'Login successful')
        
            window.destroy()
            import Home_Page
#Home Page
            # homepage = Tk()
            # homepage.title('Home Page')
            # Home_screen_width = screen_width
            # Home_screen_height = screen_height
            # homepage.geometry('1280x720+50+50')
            # homepage.resizable(0,0)
            
            # userLabel = Label(homepage, text = f'Welcome {user_entry.get()}',font= ('Times New Roman',24,'bold'), bg='white',bd=0,fg= 'black' )
            # userLabel.pack(pady=10, padx=10)
            # homepage.mainloop()
            
        except mysql.connector.Error as e:
            messagebox.showerror('Error','Connection is not established, try again later')
            return


            
    
def on_enter(event):
    if user_entry.get()=='Username':
        user_entry.delete(0,END)
        
def on_enter1(event):
    if password_entry.get()=='Password':
        password_entry.delete(0,END)
        
def hide():
    open_eye.config(file='closeeye.png')
    password_entry.config(show='*')
    eyeButton.config(command=show)
    
def show():
    open_eye.config(file='openeye.png')
    password_entry.config(show='')
    eyeButton.config(command=hide)
    
def signup():
    window.destroy()
    import Signup_Page
        
#Heading
heading = Label(window, text = 'USER LOGIN', font=('Microsoft Yahei UI Light',23,'bold'), 
                bg='white',activebackground='white', fg= 'tomato3')
heading.place(x=940, y=140)

# #User Name
# user_name = Label(window, text = 'User Name :', font=('Microsoft Yahei UI Light',11,'bold'), bg='white', fg= 'firebrick1')
# user_name.place(x=900,y=180)

# #User Entry Box
user_entry = Entry(window, text = 'User Name :', font=('Microsoft Yahei UI Light',11,'bold'),
                   bd = 0, bg='white', fg= 'tomato3')
user_entry.place(x=910,y=226)
user_entry.insert(0,'Username')
user_entry.bind('<FocusIn>',on_enter)

frame1=Frame(window,width=250,height=2, bg='tomato3')
frame1.place(x=910, y=250)


# #Password
# user_password = Label(window, text = 'Password :')
# user_password.grid(row=1, column=0)

# #Password entry Box
password_entry = Entry(window, text = 'Password :', font=('Microsoft Yahei UI Light',11,'bold'),
                       bd = 0, bg='white', fg= 'tomato3')
password_entry.place(x=910,y=296)
password_entry.insert(0,'Password')
password_entry.bind('<FocusIn>',on_enter1)

frame2=Frame(window,width=250,height=2, bg='tomato3')
frame2.place(x=910, y=320)

#Eye Button
open_eye=PhotoImage(file='openeye.png')
eyeButton = Button(window, image=open_eye,bd=0, bg='white',cursor='hand2', command=hide)
eyeButton.place(x=1140, y=294)

#Forget_password
forgetButton = Button(window, text='Forget Password ?', font=('Microsoft Yahei UI Light', 8,'bold'), 
                      bd=0, bg='white',fg='tomato3',activeforeground='tomato3', cursor='hand2',command = forget)
forgetButton.place(x=1060, y=330)

#Login Button
Login_Button = Button(window, text='LOG IN', font=('Times New Roman',16,'bold'),
                      fg='white', bg='tomato3',activebackground='tomato3',activeforeground='white', cursor='hand2', bd=0, width=21, command=Login)
Login_Button.place(x=912 ,y=370)

#OrLabel
OrLabel=Label(window, text='----------- OR -----------',font=('Microsoft Yahei UI Light',15,'bold'),fg='tomato3',bg='white')
OrLabel.place(x=905, y=430)

#facebook
facebook=PhotoImage(file='facebook.png')
facebookButton=Button(window,image = facebook,bg='white', bd=0)
facebookButton.place(x=950,y=480)

#Google
google=PhotoImage(file='google.png')
googleButton=Button(window,image=google, bg='white', bd=0)
googleButton.place(x= 1030, y=480)

#Twitter
twitter=PhotoImage(file='twitter.png')
twitterButton=Button(window, image=twitter,bd=0,bg='white')
twitterButton.place(x=1110, y=480)

#New User
newUser=Label(window, text='Dont have an account ?',font=('Microsoft Yahei UI Light',10,'bold'),bg='white',bd=0,fg='tomato3')
newUser.place(x=960,y=560)

#Link_Signup
Signup_signup = Button(window,text='Create new Account !',font=('Microsoft Yahei UI Light',8,'bold underline'),
                      bg='white',bd=0,fg='blue',activeforeground='blue',activebackground='white',cursor='hand2', command=signup)
Signup_signup.place(x=980, y=580)

#To Implement the program
window.mainloop()
