import numpy as np
import pandas as pd
from PIL import ImageTk,Image
from sklearn.preprocessing import StandardScaler
from sklearn.model_selection import train_test_split
from sklearn import svm
from sklearn.metrics import accuracy_score
import pyttsx3

engine = pyttsx3.init()
#ai
import pandas as pd2
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import StandardScaler
from sklearn import svm

df = pd.read_csv('C:\\Users\\Srinath\\OneDrive\\Others\\Desktop\\bit\\heart.csv')
X = df.drop(columns='output', axis=1)
Y = df['output']

# the features extraction0
scaler = StandardScaler()
X_standardized = scaler.fit_transform(X)

# Split the data into training and testing sets
X_train, X_test, Y_train, Y_test = train_test_split(X_standardized, Y, test_size=0.2, stratify=Y, random_state=2)

# Create and train the SVM classifier
classifier = svm.SVC(kernel='linear')
classifier.fit(X_train, Y_train)

# Now you can use the trained classifier for predictions or other tasks


#ui
from tkinter import *

root = Tk()
root.geometry("800x510")
title = root.title('HEART-ATTACK PREDICTOR')
root.resizable(0,0)
bg = ImageTk.PhotoImage(file="C:\\Users\\Srinath\\OneDrive\\Others\\Desktop\\bit\\bg hd.png")
canvas = Canvas(root, width=800, height=510)
canvas.pack(fill="both", expand=True)
canvas.create_image(0, 0, image=bg, anchor="nw")
def submit_command():
    a = int(field1.get())
    b = int(field2.get())
    c = int(field3.get())
    d = int(field4.get())
    e = int(field5.get())
    f = float(field6.get())
    g = float(field7.get())
    h = int(field8.get())
    i = int(field9.get())
    j = float(field10.get())
    k = int(field11.get())
    l = int(field12.get())
    m = int(field13.get())
    input_data = (a,b,c,d,e,f,g,h,i,j,k,l,m)
    input_data_as_numpy_array = np.asarray(input_data)
    input_data_reshaped = input_data_as_numpy_array.reshape(1,-1)
    std_data = scaler.transform(input_data_reshaped)
    prediction = classifier.predict(std_data)
    if (prediction[0] == 0):
        engine = pyttsx3.init()
        engine.say("YOU ARE HEALTHY")
        engine.runAndWait()
        predict_label.config(text="YOU ARE HEALTHY",fg='green')
    else:
        engine = pyttsx3.init()
        engine.say("YOU HAVE RISK OF HEART ATTACK")
        engine.runAndWait()
        predict_label.config(text="YOU HAVE RISK OF HEART ATTACK",fg='red')

def clear_command():
    field1.delete(0, END)
    field2.delete(0, END)
    field3.delete(0, END)
    field4.delete(0, END)
    field5.delete(0, END)
    field6.delete(0, END)
    field7.delete(0, END)
    field8.delete(0, END)
    field9.delete(0, END)
    field10.delete(0, END)
    field11.delete(0, END)
    field12.delete(0, END)
    field13.delete(0, END)
    predict_label.config(text="ENTER THE ABOVE DETAILS",fg='gray')
    field1.focus_set()

label1 = Label(root, text = "AGE",fg = 'grey', bg = 'black',font=('helvetica',8,"bold"))
label1.place(x=35,y=45)
field1 = Entry(root)
field1.place(x=200,y=45)
label2 = Label(root, text = "SEX",fg = 'grey', bg = 'black',font=('helvetica',8,"bold"))
label2.place(x=35,y=70)
field2 = Entry(root)
field2.place(x=200,y=70)
label3 = Label(root, text = "CP",fg = 'grey', bg = 'black',font=('helvetica',8,"bold"))
label3.place(x=35,y=95)
field3 = Entry(root)
field3.place(x=200,y=95)
label4 = Label(root, text = "TRTBPS",fg = 'grey', bg = 'black',font=('helvetica',8,"bold"))
label4.place(x=35,y=120)
field4 = Entry(root)
field4.place(x=200,y=120)
label5 = Label(root, text = "CHOLESTRAL",fg = 'grey', bg = 'black',font=('helvetica',8,"bold"))
label5.place(x=35,y=145)
field5 = Entry(root)
field5.place(x=200,y=145)
label6 = Label(root, text = "FBS",fg = 'grey', bg = 'black',font=('helvetica',8,"bold"))
label6.place(x=35,y=170)
field6 = Entry(root)
field6.place(x=200,y=170)
label7 = Label(root, text = "RESTCEG",fg = 'grey', bg = 'black',font=('helvetica',8,"bold"))
label7.place(x=35,y=195)
field7 = Entry(root)
field7.place(x=200,y=195)
label8 = Label(root, text = "THALACHH",fg = 'grey', bg = 'black',font=('helvetica',8,"bold"))
label8.place(x=35,y=220)
field8 = Entry(root)
field8.place(x=200, y=220)
label9 = Label(root, text = "EXNG",fg = 'grey', bg = 'black',font=('helvetica',8,"bold"))
label9.place(x=35,y=245)
field9 = Entry(root)
field9.place(x=200, y=245)
label10 = Label(root, text = "OLDPEAK",fg = 'grey', bg = 'black',font=('helvetica',8,"bold"))
label10.place(x=35,y=270)
field10 = Entry(root)
field10.place(x=200, y=270)
label11 = Label(root, text = "SLP",fg = 'grey', bg = 'black',font=('helvetica',8,"bold"))
label11.place(x=35,y=295)
field11 = Entry(root)
field11.place(x=200, y=295)
label12 = Label(root, text = "CAA",fg = 'grey', bg = 'black',font=('helvetica',8,"bold"))
label12.place(x=35,y=320)
field12 = Entry(root)
field12.place(x=200, y=320)
label13 = Label(root, text = "THALL",fg = 'grey', bg = 'black',font=('helvetica',8,"bold"))
label13.place(x=35,y=345)
field13 = Entry(root)
field13.place(x=200, y=345)

button1 = Button(root, text = "PREDICT", bg = "gray25",fg = "white",font=('helvetica',8,"bold"),borderwidth=0, command = submit_command)
button1.place(x=165,y=380)
button2 = Button(root, text = "CLEAR", bg = "gray25",fg = "white",font=('helvetica',8,"bold"),borderwidth=0, command = clear_command)
button2.place(x=250,y=380)

predict_label = Label(root, text="ENTER THE ABOVE DETAILS",fg = 'gray', bg = 'black',font='helvetica 10 bold')
predict_label.place(x=148, y=430)
root.mainloop()
