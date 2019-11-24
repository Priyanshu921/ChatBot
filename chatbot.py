from tkinter import *
import datetime
import time
class Window(Tk):
    def __init__(self):
        super().__init__()
    def Window(self):
        self.geometry("420x480")
        self.minsize(420,480)
        self.maxsize(420,480)
        self.title("ChatBot")
        self.wm_iconbitmap("chtbot.ico") 
    
    def GetMessage():
        time1=datetime.datetime.now()
        repl={"hey":"hey there",
              "Hey":"Hey There",
              "Hi":"Hey There",
              "How are you":"I am Fine,What about you?",
              "how are you":"I am Fine,What about you?",
              "What is the time now?":f'The time now is {time1.strftime("%X")}',
              "What is the time now":f'The time now is {time1.strftime("%X")}',
              "what is the time now":f'The time now is {time1.strftime("%X")}',
              "Which is your favourite movie?":'My Most faviourite movie is "Source Code"',
              "Who is Your Favourite actor?":"",
              "bye":"Byee..Have a Nice day ",
              "What is your name":"My Name is Talko Talko",
              "What Do you Do":"I Chat with everyone",
              "Which fields are you intrested in?":"I am intrested in Various topics such as mobile phones,Study,Space,etc",
              "Which Branch Should I take in Engineering":"As I am a Computer Science Product I would highly recommend Computer Science+",
              "Which mobile phone you would prefer me to buy":"It depends on your budget",
              "Should I buy an Iphone":"I would say no to an iPhone",
              "Who created you":"I was sololey created by Priyanshu Patidar",
              "why should I take computer science":"because it has good scope in the coming future"

        }
        msg=UserMSG.get()
        msg1=f"{UserMSG.get()}"
        textar.insert(END,'you:- '+msg+'\n')
        rep=f"{repl[msg]}"
        time.sleep(1)
        textar.insert(END,'Robo:- '+rep+'\n')

        

    def textarea(self):
        global UserMSG,textar
        UserMSG=StringVar()
        """photo=PhotoImage(file="bgimage.png")
        bg=Label(self,image=photo)
        bg.place(x=0,y=0,relwidth=1,relheight=1)"""
        scroll=Scrollbar(self)
        scroll.grid(row=1,column=1,sticky=NS)
        textar=Text(self,width=50,height=25,yscrollcommand = scroll.set )
        textar.grid(row=1,column=0,sticky=NSEW)
        textar.insert(END,'Hello This is just a simple Chatbot \nMade By Priyanshu Patidar \nusing Tkinter and a simle Dictionary and he hopes that \nyou will Like the Program he created\n')
        msg=Entry(self,width=60,textvariable=UserMSG)
        msg.grid(row=2,column=0,pady=10,sticky=SW)
        send=Button(text="SEND",command=Window.GetMessage)
        send.grid(row=3,column=0)
        scroll.config(command=textar.yview)
if __name__ == "__main__":
    win1=Window()
    win1.Window()
    #win1.title()
    win1.textarea()
    win1.mainloop()
