# import tkinter as tk

# def on_new_file():
#     print("New file menu option clicked.")

# def on_open_file():
#     print("Open file menu option clicked.")

# def on_save_file():
#     print("Save file menu option clicked.")

# def on_exit():
#     root.quit()

# if __name__ == "__main__":
#     root = tk.Tk()
#     root.title("Tkinter Menu Example")

#     # Create the main menu
#     menu_bar = tk.Menu(root)
#     root.config(menu=menu_bar)

#     # Create the "File" menu
#     file_menu = tk.Menu(menu_bar, tearoff=0)
#     menu_bar.add_cascade(label="File", menu=file_menu)

#     file_menu.add_command(label="New", command=on_new_file)
#     file_menu.add_command(label="Open", command=on_open_file)
#     file_menu.add_command(label="Save", command=on_save_file)
#     file_menu.add_separator()
#     file_menu.add_command(label="Exit", command=on_exit)

#     # Create the "Edit" menu (optional, you can add more menus)
#     edit_menu = tk.Menu(menu_bar, tearoff=0)
#     menu_bar.add_cascade(label="Edit", menu=edit_menu)

#     # Add options to the "Edit" menu (you can add more options)
#     edit_menu.add_command(label="Cut")
#     edit_menu.add_command(label="Copy")
#     edit_menu.add_command(label="Paste")

#     root.mainloop()
#     root.mainloop()

from tkinter import *

homepage = Tk()
homepage.geometry('1280x20+50+50')
homepage.title('Home Page')

myframe=Frame(homepage)
myframe.pack()

YScrollbar=Scrollbar(myframe,orient=VERTICAL)

arnold = ImageTk.PhotoImage(file = 'arnold new.png')

arnoldLabel=Label(homeframe1, image=arnold)
arnoldLabel.pack(pady=10, padx=10)

quote1 = Label(homeframe1, text ='''
               “The last three or four reps is what makes the muscle grow. 
               This area of pain divides the champion from someone 
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
               “I hated every minute of training, but I said, don’t quit. 
               Suffer now and live the rest of your life as a champion.”

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
                “Success isn’t overnight. It’s when everyday you get 
                a little better than the day before. It all adds up.”

                                                                  –DWAYNE JOHNSON
''', font=('Times New Roman',16,'bold'))
quote3.pack()

homepage.mainloop()





