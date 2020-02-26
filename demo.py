from tkinter import *
from tkinter import ttk
import time



class Root(Tk):
    def __init__(self):
        super(Root, self).__init__()
        self.title("Tkinter Progress Bar")
        self.minsize(640, 400)

        self.buttonFrame = ttk.LabelFrame(self, text="extracting eval answers")
        self.buttonFrame.grid(column=0, row=0)
        self.progressBar()



    def progressBar(self):



        self.button1 = ttk.Button(self.buttonFrame, text = "Start extracting answers", command = self.run_progressbar)
        self.button1.grid(column =0, row = 2)


        self.button2 = ttk.Button(self.buttonFrame, text = "add files", command = self.start_progressbar)
        self.button2.grid(column = 3, row = 2)
        self.label1 = ttk.Label()
        self.label1.setvar()

        self.progress_bar = ttk.Progressbar(self, orient = 'horizontal', length = 286, mode = 'determinate')
        self.progress_bar.grid(column = 1, row = 2, pady  =2)


    def run_progressbar(self):
        self.progress_bar["maximum"] = 100

        for i in range(101):
            time.sleep(0.05)
            self.progress_bar["value"] = i
            self.progress_bar.update()

        self.progress_bar["value"] = 0



    def start_progressbar(self):
        self.progress_bar.start()



    def stop_progressbar(self):
        self.progress_bar.stop()





root = Root()
root.mainloop()