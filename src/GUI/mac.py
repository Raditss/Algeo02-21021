from tkinter import *
from PIL import Image
from PIL import ImageTk
from tkinter import filedialog
from tkinter.filedialog import askopenfile
from tkinter import ttk
import sv_ttk




root = Tk()
root.title("Face Recognition") 
root.geometry("992x558")
bgimg= ImageTk.PhotoImage(file = "src/GUI/Components/vw.jpg")
limg= Label(root, i=bgimg)
limg.pack()




nofile1=Label(text="No File Chosen", font='Helvatica 12',bg="peachpuff3")
nofile1.place(x=150, y=170)

nofile2=Label(text="No File Chosen", font='Helvatica 12',bg="peachpuff3")
nofile2.place(x=150, y=250)


result=Label(text="None", font='century 18',fg="green4",bg="peachpuff3")
result.place(x=73, y=350)





def upload_file1():
    global img1,f1
    foldername = filedialog.askdirectory(initialdir="test")
    img1 = Image.open(foldername)
    img1 = img1.resize((256,256), Image.ANTIALIAS)
    img1 = ImageTk.PhotoImage(img1)
    f1=foldername


button1 = ttk.Button(text="Upload file", command=upload_file1)
button1.pack()
button1.place(x=73, y=170)


img2 = Image.open("src/GUI/Components/noimage.jpg")
img2 = img2.resize((256,256), Image.ANTIALIAS)
img2 = ImageTk.PhotoImage(img2)
label = Label( image = img2)
label.place(x=387, y=162)

def upload_file2():
    global img2,t1
    f_types = [('Jpg Files', '*.jpg')]
    filename = filedialog.askopenfilename(filetypes=f_types)
    img2 = Image.open(filename)
    img2 = img2.resize((256,256), Image.ANTIALIAS)
    img2 = ImageTk.PhotoImage(img2)
    label = Label(image = img2)
    label.place(x=387, y=161)
    shortfilename = filename.split('/')[len(filename.split('/'))-1]
    nofile2["text"] = shortfilename
    nofile2["font"] = "century 10"
    t1=filename


button2 = ttk.Button(text="upload file", command=upload_file2)
button2.pack()
button2.place(x=73, y=250)



img3 = Image.open("src/GUI/Components/noimage.jpg")
img3 = img3.resize((256,256), Image.ANTIALIAS)
img3 = ImageTk.PhotoImage(img3)
label = Label(image = img3)
label.place(x=672, y=162)




time=Label(text="00:00", font='century 24', fg="green4", bg="peachpuff3")
time.place(x=515, y=468)

sv_ttk.set_theme("light")



root.mainloop()