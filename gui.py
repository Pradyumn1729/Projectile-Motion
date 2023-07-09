from tkinter import *
from PIL import ImageTk,Image
from tkinter import messagebox
def Run_login():
    email=email_input.get()
    password = Password_input.get()
    if email == 'itspradyumn1729@gmail.com' and password == '1729':
        messagebox.showinfo("cool","welcome Pradyumn")
    else:
        messagebox.showerror("nope",'u r not pradyumn')

root = Tk()
root.title("welcome")
root.geometry('500x500')
img=Image.open('wallpaper nature.jpg')
Resize=img.resize((100,100))
root.configure(background='#a6b697')
img = ImageTk.PhotoImage(Resize)
img_label=Label(root,image=img)
img_label.pack(pady=(15,15))
text_label=Label(root,text='Nature',fg='#88a78e',bg='white')
text_label.pack()
text_label.config(font=('times new roman',15))


email_label = Label(root,text='Enter email',fg='white',bg='#88a78e')
email_label.pack() #to pack image in root variable
email_label.pack(pady=(20,5))
email_label.config(font=('Times new roman',10))

email_input=Entry(root,width=50)
email_input.pack(ipady=4,pady=(1,15)) #for y axis change of box

Password_label = Label(root,text='Enter password',fg='white',bg='#88a78e')
Password_label.pack() #to pack image in root variable
Password_label.pack(pady=(20,5))
Password_label.config(font=('Times new roman',10))

Password_input=Entry(root,width=50)
Password_input.pack(ipady=4) #for y axis change of box
login_button= Button(root,text='Login',bg='white',fg='black',command=Run_login)
login_button.pack(ipadx=10,pady=(10,20))

root.mainloop() # for gui entry

