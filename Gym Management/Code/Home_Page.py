from tkinter import *
from tkinter import messagebox
from PIL import Image, ImageTk
from tkinter import ttk


homepage = Tk()
screen_width = homepage.winfo_screenwidth()
screen_height = homepage.winfo_screenheight()
homepage.geometry(f'{screen_width}x{screen_height}')
homepage.resizable(0,0)
homepage.title('Home Page')

homeframe=Frame(homepage)
homeframe.pack(fill= BOTH, expand=1)

#Canvas
my_canvas = Canvas(homeframe)
my_canvas.pack(side=LEFT, fill= BOTH, expand=1)

#Scroll bar

Yscroll = ttk.Scrollbar(homeframe,orient=VERTICAL, command=my_canvas.yview)
Yscroll.pack(side=RIGHT,fill=Y)

my_canvas.configure(yscrollcommand=Yscroll.set)
my_canvas.bind('<Configure>', lambda e: my_canvas.configure(scrollregion= my_canvas.bbox("all")))

#Additional Frame
homeframe1 = Frame(my_canvas, bg= 'white')
homeframe1.pack(fill='both', expand=TRUE)

my_canvas.create_window((0,0), window= homeframe1, anchor='nw')
my_canvas.pack(fill='both', expand=TRUE)

userLabel = Label(homeframe1, text = 'Welcome',font= ('Arial Rounded MT Bold',24,'bold'), bg='white',bd=0,fg= 'black' )
userLabel.place(x=600, y=10)

#Arnold
# arnoldpic= Image.open('arnold.png')
# resized1= arnoldpic.resize((350,250), Image.ANTIALIAS)
# arnold=ImageTk.PhotoImage(resized1)

# arnoldlabel=Label(homeframe1, image=arnold)
# arnoldlabel.pack(pady=10, padx=10)
arnold = ImageTk.PhotoImage(file = 'arnold new.png')

arnoldLabel=Label(homeframe1, image=arnold)
arnoldLabel.pack(pady=10, padx=10)

quote1 = Label(homeframe1, text ='''
               “The last three or four reps is what makes the muscle grow. This area of pain divides the champion from someone 
               who is not a champion.”
               
                                                                  -ARNOLD SCHWARZENEGGER
''', font=('Times New Roman',16,'bold'))
quote1.pack()

#Ali
# new_image= Image.open("muhammad_ali.jpg")
# resized2= new_image.resize((300,300), Image.ANTIALIAS)
# Ali = ImageTk.PhotoImage(resized2)
# AliLabel=Label(homeframe1,image=Ali)
# AliLabel.pack(pady=10, padx=10)
ali = ImageTk.PhotoImage(file = 'ali new.jpg')

aliLabel=Label(homeframe1, image=ali)
aliLabel.pack(pady=10, padx=10)


quote2 = Label(homeframe1, text ='''
               “I hated every minute of training, but I said, don’t quit. Suffer now and live the rest of your 
               life as a champion.”

                                                                  -MUHAMMAD ALI
''', font=('Times New Roman',16,'bold'))
quote2.pack()

#Rock
# rockpic= Image.open('rock new.jpg')
# resized3= rockpic.resize((300,400), Image.ANTIALIAS)
# rock=ImageTk.PhotoImage(resized3)
# rocklabel=Label(homeframe1, image=rock)
# rocklabel.pack(pady=10, padx=10)

rock = ImageTk.PhotoImage(file = 'rock new.jpg')

rockLabel=Label(homeframe1, image=rock)
rockLabel.pack(pady=10, padx=10)

quote3 = Label(homeframe1, text ='''
                “Success isn’t overnight. It’s when everyday you get a little better than the day before. 
                It all adds up.”

                                                                  –DWAYNE JOHNSON
''', font=('Times New Roman',16,'bold'))
quote3.pack()

homepage.mainloop()