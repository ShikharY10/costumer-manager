from tkinter import *
from threading import *
from PIL import Image,ImageTk
import time
import datetime
import csv
import os

class Registration():

        def __init__(self,_main = None):
                '''
                This class is responsible for all the registration related entries.(all user details)
                _main : This argument is for taking the frame, the frame on which all tkinter widget show.
                '''
                
                self._main = _main
                self.count = 1
                self.v = IntVar()
                self.radio_btn_val = ""

                Label(self._main,text = "Full Name").place(x = 20,y = 50)
                self.full_name_input = Entry(self._main)
                self.full_name_input.place(
                x = 140,
                y = 50,
                width = 200
                )

                Label(self._main,text = "D.O.B.").place(x = 20,y = 80)
                self.date_of_birth_input = Entry(self._main)
                self.date_of_birth_input.place(x = 140,y = 80,width = 200)

                Label(self._main,text = "Email").place(x= 20,y = 110)
                self.user_email_input = Entry(self._main)
                self.user_email_input.place(x = 140,y = 110,width = 200)

                Label(_main,text = "Gender").place(x = 20,y = 140)
                self.R1 = Radiobutton(_main, text = "Male",bg = "thistle2",variable = self.v,value = 1,command = lambda : self.radio_btn_func("Male"))
                self.R1.place(x = 140,y = 140)
                self.R2 = Radiobutton(_main,text = "Female",bg = "thistle2",variable = self.v,value = 2,command = lambda : self.radio_btn_func("Female"))
                self.R2.place(x = 190, y= 140)
                self.R3 = Radiobutton(_main,text = "Other",bg = "thistle2",variable = self.v,value = 3,command = lambda : self.radio_btn_func("Other"))
                self.R3.place(x = 260, y= 140)

                Label(self._main,text = "Password").place(x = 20,y = 170)
                self.user_password_input = Entry(self._main,show = "*")
                self.user_password_input.place(x = 140,y = 170,width = 200)
                Label(
                        self._main,
                        text = "Minimum 8 Character and should use one ABC,abc,123,!@#",
                        bg = "thistle2",
                        font = (None,8),
                        padx = 0,
                        pady = 0,
                        foreground = "grey"
                        ).place(x = 20,y = 200)

                Label(self._main,text = "Conform Password").place(x = 20,y = 230)
                self.user_conform_password_input = Entry(self._main,show = "*")
                self.user_conform_password_input.place(x = 140,y = 230,width = 200)

                self.pass_quality = Label(self._main,text = "",bg = "thistle2")

                self.file_correct = ImageTk.PhotoImage(Image.open("C:\\Users\\acer\\shikhar\\Projects\\bank_acc_manger\\images\\image_correct.png").resize((20,15)))
                self.file_wrong = ImageTk.PhotoImage(Image.open("C:\\Users\\acer\\shikhar\\Projects\\bank_acc_manger\\images\\images_cross.png").resize((20,15)))

                btn2 = Button(_main,text = "Save",command = self.main_register)
                btn2.place(x = 150,y = 300)
                
                self.start_new_thread()

        def submit_check(self):
                
                while True:
                        
                        time.sleep(1)
                        shikhar = str(self.full_name_input.focus_get())
                          
                        if shikhar == "frame1.!entry":
                                name_first = self.full_name_input.get()
                                if len(name_first)>0 and len(name_first.split()) == 1:
                                        file_wrong_image = Label(self._main,image = self.file_wrong)
                                        file_wrong_image.place(x = 400,y = 50)
                                elif len(name_first.split()) > 1 and len(name_first) > 0:
                                        file_correct_image = Label(self._main,image = self.file_correct)
                                        file_correct_image.place(x = 400,y = 50)

                        elif shikhar == "frame1.!entry2":
                                birth_count = self.date_of_birth_input.get()
                                if len(birth_count) ==2:
                                        self.date_of_birth_input.insert(2,"/")
                                elif len(birth_count) == 5:
                                        self.date_of_birth_input.insert(5,"/")

                        elif shikhar == "frame1.!entry3":
                                email_find = re.findall('\S+@\S+',self.user_email_input.get())
                                if len(email_find) == 0:
                                        email_wrong_image = Label(self._main,image = self.file_wrong)
                                        email_wrong_image.place(x = 400,y = 110)

                                elif len(email_find) == 1:
                                        email_correct_image = Label(self._main,image = self.file_correct)
                                        email_correct_image.place(x = 400,y = 110)

                        elif shikhar == "frame1.!entry4":
                                password_stored = str(self.user_password_input.get())
                                if len(password_stored)>0 and len(password_stored) < 5:
                                        self.pass_quality.config(text = "Too Short!")
                                        self.pass_quality.place(x = 380,y = 170)
                                elif len(password_stored) > 5 and len(password_stored) < 8:
                                        self.pass_quality.place_forget()
                                        self.pass_quality.config(text = "Moderate!")
                                        self.pass_quality.place(x = 380,y = 170)
                                elif len(password_stored) > 8:
                                        self.pass_quality.place_forget()
                                        self.pass_quality.config(text = "Strong!")
                                        self.pass_quality.place(x = 380,y = 170)

                        elif shikhar == "frame1.!entry5":
                                if self.user_conform_password_input.get() == self.user_password_input.get():
                                        conf_pass_correct_image = Label(self._main,image = self.file_correct)
                                        conf_pass_correct_image.place(x = 400,y = 230)
                                else:
                                        file_wrong_image = Label(self._main,image = self.file_wrong)
                                        file_wrong_image.place(x = 400,y = 230)
        
        def start_new_thread(self):
                thread1 = Thread(target = self.submit_check)
                thread1.start()

        def radio_btn_func(self,value):
                self.radio_btn_val = value

        def main_register(self):
                try:
                        A = self.full_name_input.get()
                        B = self.date_of_birth_input.get()
                        C = self.user_conform_password_input.get()

                        lst = os.listdir(str(os.getcwd()+"\Files"))
                        s = str(datetime.date.today()).split("-")
                        p = "-"
                        present_date = p.join([s[2],s[1],s[0]])
                        # file_name = f"File.{self.count}.{d}.csv"
                        print(f"d is: {present_date}")
                        f = lst[-1].split(".")[2]
                        print(f"lst date is: {f}")
                        
                except Exception as e:
                        print(e)

                if len(lst) == 0:
                        try:
                                n = ["Name".center(20),"DOB".center(20),"Pin".center(20),"Gender".center(20),"Date and Time".center(30),]
                                op = open("Files//"+f"File.{self.count}.{present_date}.csv",mode = "w",newline = "\n",encoding = "utf-8")
                                csv_writer = csv.writer(op,delimiter=',')
                                csv_writer.writerow(n)
                                op.close()

                                data = [A.center(20),B.center(20),C.center(20),self.radio_btn_val.center(20),str(datetime.datetime.now()).center(30)]
                                op2 = open("Files//"+f"File.{self.count}.{present_date}.csv",mode = "a",newline = "\n",encoding = "utf-8")
                                csv_writer1 = csv.writer(op2,delimiter=',')
                                csv_writer1.writerow(data)
                                op2.close()

                                Label(self._main,text= "Saved!!").place(x = 150,y = 330)

                        except Exception as e:
                                print(e)

                elif len(lst) > 0 and str(present_date) == str(lst[-1].split(".")[2]):
                        try:
                                data = [A.center(20),B.center(20),C.center(20),self.radio_btn_val.center(20),str(datetime.datetime.now()).center(30)]
                                op2 = open("Files//"+lst[-1],mode = "a",newline = "\n",encoding = "utf-8")
                                print("line 170")
                                csv_writer1 = csv.writer(op2,delimiter=',')
                                csv_writer1.writerow(data)
                                op2.close()
                                Label(self._main,text= "Saved!!").place(x = 150,y = 330)

                        except Exception as e:
                                print(e)
                else:                           
                        try:
                                g = int(lst[-1].split(".")[1]) + 1
                                file_name_2 = "Files//"+f"File.{g}.{present_date}.csv"

                                n = ["Name".center(20),"DOB".center(20),"Pin".center(20),"Gender".center(20),"Date and Time".center(30),]

                                n_file = open(file_name_2,mode = "w",newline = "\n",encoding = "utf-8")
                                csv_writer = csv.writer(n_file,delimiter=',')
                                csv_writer.writerow(n)
                                n_file.close()

                                data = [A.center(20),B.center(20),C.center(20),self.radio_btn_val.center(20),str(datetime.datetime.now()).center(30)]

                                n_file_2 = open(file_name_2,mode = "a",newline = "\n",encoding = "utf-8")
                                csv_writer1 = csv.writer(n_file_2,delimiter=',')
                                csv_writer1.writerow(data)
                                n_file_2.close()

                                Label(self._main,text= "Saved!!").place(x = 150,y = 330)

                        except Exception as e:
                                print(e)
                        

                        




                
