from tkinter import *
import smtplib
import sys
import datetime

root = Tk()
#width x height
root.title("Mail Sender")
root.geometry("500x500+0+0")

ftop = Frame(root,width=500,height=300,bd=8,relief="raise")
flow = Frame(root,width=500,height=200,bd=8,relief="raise")
ftop.pack(side=TOP)
flow.pack(side=BOTTOM)

textfield = Text(flow)
textfield.pack()



sender = "test@gmail.com"    #put your email here
password = "test123"         #put your password here
reciever = StringVar()
subject = StringVar()
body = StringVar()
message = f'Subject: {subject} \n\n {body}'

label1 = Label(ftop , font=("Times",15,"bold"),text="Reciver's  Email : " , fg="blue" ).grid(row=1,column=2)
entry1 = Entry(ftop ,textvariable=reciever ,font=("arial",13,"bold"), width = 35,fg="brown").grid(row=1,column=3)

label2 = Label(ftop , font=("Times",15,"bold"),text="Subject : " , fg="blue" ).grid(row=2,column=2)
entry2 = Entry(ftop ,textvariable=subject ,font=("arial",13,"bold"), width = 35,fg="brown").grid(row=2,column=3)

label3 = Label(ftop , font=("Times",15,"bold"),text="Body : " , fg="blue" ).grid(row=3,column=2)
entry3 = Entry(ftop ,textvariable=body ,font=("arial",13,"bold"), width = 35,fg="brown").grid(row=3,column=3)

buttonsend = Button(ftop , text = "SEND" ,font=("arial",13,"bold"),padx=20,pady=8 ,bd = 5,fg="green",command = lambda :Send_Mail(sender,password,reciever.get(),subject.get(),body.get()) ).grid(row=4,column=3)

def Send_Mail(sender,password,reciever,subject,body):
    ################### HISTORY ###################
    obj = open("history.txt","a")
    now = str(datetime.datetime.now())
    obj.write(reciever)
    obj.write("                 ")
    obj.write(subject)
    obj.write("                 ")
    obj.write(body)
    obj.write("                 ")
    obj.write(now)
    obj.write("\n")
    obj.close()
    ################################################
    
    textfield.insert(INSERT,"************************** STATUS **************************\n")
    check = list(reciever)
    if('@' not in check):
        textfield.insert(INSERT,"--> Enter Valid Mail :( !!\n")
        sys.exit()
    if('.' not in check):
        textfield.insert(INSERT,"--> Enter Valid Mail :( !!\n")
        sys.exit()
    
    
        
    try:
        s = smtplib.SMTP('smtp.gmail.com', 587) 
        s.ehlo()
        s.starttls() 
        s.login(sender,password)
        message = f'Subject: {subject} \n\n {body}'
        s.sendmail(sender, reciever, message)
    except smtplib.SMTPException:
        textfield.insert(INSERT,"--> ERROR :( !!\n")
    else:
        textfield.insert(INSERT,"--> Mail Sent :) !!\n")
    s.close() 


root.mainloop()
