# import rs as r 
# from tkinter import *
# import tkinter as tk
# root = Tk()
# root.geometry('800x600')
# def lo():
#     root.destroy()
#     r.rikit()
# def mm():
#     name = Label (text="Enter number : ")
#     name.place(x=100,y=100)
#     nameinput =Entry()
#     nameinput.place(x=220,y=100)
#     lastname = Label(text="Password :")
#     lastname.place(x=100,y=200)
#     lastinput=Entry()
#     lastinput.place(x=205,y=200)
#     xyname =Label(text=" OTP :")
#     xyname.place(x=100,y=300)
#     xyinput=Entry()
#     xyinput.place(x=205,y=300)
#     blt = Button(text="submit" ,command=lo)
#     blt.place(x=200,y=400)
#     root.mainloop()
# mm()






# def reg():
#     root = Tk()
#     root.geometry('800x600')
#     def data():
#         name=nameinput.get()
#         print("USER id = ", name)
    
#         last_name=lastinput.get()
#         print("last name= ", last_name)
    
    
#         password=xyinput.get()
#         print("password =" ,password)




#     name = Label (text="user id : ")
#     name.place(x=100,y=100)
#     nameinput = Entry()
#     nameinput.place(x=220,y=100)

#     lastname = Label(text="user name:")
#     lastname.place(x=100,y=200)
#     lastinput=Entry()
#     lastinput.place(x=205,y=200)

#     xyname = Label(text=" password :")
#     xyname.place(x=100,y=300)
#     xyinput=Entry()
#     xyinput.place(x=205,y=300)


#     blt = Button(text="submit" ,command=Login)
#     blt.place(x=200,y=400)
#     root.mainloop()

# reg()
# Login()





import pandas as pd 
data = pd.read_csv("Salary_data.csv")
print(data)

# n1=data['Gender'].head[20].values
n2=data['Age'].head[20].values

# print('n1=',n1)
print('n2=',n2)

# if 'Male'in n1:
if'34'in n2:
        print('found')
else:
    print('not found')











