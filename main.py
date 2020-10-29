from tkinter import *
from Registrations import Registration


class Full_screen_app(object):
      def __init__(self,master,**kwargs):
            self.master = master
            self._geom= f"{master.winfo_screenwidth() //2}x{master.winfo_screenheight() //2}"
            master.geometry("{0}x{1}".format(master.winfo_screenwidth(),master.winfo_screenheight()))
            master.bind('<Escape>',self.toggle_geom)
      def toggle_geom(self,event):
            geom = self.master.winfo_geometry()
            self.master.geometry(self._geom)
            self._geom= geom

class main_loop():

    def __init__(self):
        btn = Button(main,text = "Click me!",command = self.frame_maker)
        btn.place(x = 40,y = 1)


    def frame_maker(self):

        self.frame = Frame(main,height = main.winfo_screenheight(),width = main.winfo_screenwidth(),bg = "thistle2")
        self.frame.pack()

        Registration(self.frame)
        
        btn1 = Button(self.frame,text = "Back",command = self.frame_destroyer)
        btn1.place(x = 80,y = 300)

    def frame_destroyer(self):
        self.frame.destroy()

main = Tk()
main.title("Customer Records")
main.configure(bg = "thistle2")
Full_screen_app(main)

main_loop()
main.mainloop()
