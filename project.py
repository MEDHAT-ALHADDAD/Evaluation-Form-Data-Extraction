import cv2
from rotate_img import adjust_img
from ExtractingAnswers import determineAnswers
import tkinter as tk
from tkinter import filedialog, ttk, messagebox
import time
from tkinter import *




class Root(Tk):
    def __init__(self):
        super(Root, self).__init__()
        self.title("Tkinter Progress Bar")
        self.minsize(640, 400)
        self.buttonFrame = ttk.LabelFrame(self, text="extracting eval answers")
        self.buttonFrame.grid(column=0, row=0)
        self.progressBar()
        # make the top right close button minimize (iconify) the main window
        self.protocol("WM_DELETE_WINDOW", self.iconify)
        # make Esc exit the program
        self.bind('<Escape>', lambda e: self.destroy())
    def progressBar(self):
        self.filepaths = ""
        self.button1 = ttk.Button(self.buttonFrame, text = "Start extracting answers", command = self.run_progressbar)
        self.button1.grid(column =0, row = 2)
        self.button2 = ttk.Button(self.buttonFrame, text = "add files", command = self.start_progressbar)
        self.button2.grid(column = 1, row = 2)
        self.button2 = ttk.Button(self.buttonFrame, text = "show enhanced img", command = self.showenhanced)
        self.button2.grid(column = 2, row = 2)
        self.label1 = ttk.Label()
        self.label1.setvar()
        self.progress_bar = ttk.Progressbar(self, orient = 'horizontal', length = 286, mode = 'determinate')
        self.progress_bar.grid(column = 0, row = 4, pady  =2)


    def run_progressbar(self):
        self.progress_bar["maximum"] = 100
        i = 0
        com_ans = "Gender,Semester,Program,1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19\n"
        if (self.file_paths.__sizeof__ != 0):
            for img in self.file_paths:
                image = cv2.imread(img,0)
                
                self.enhanced = adjust_img(image)
                answer,self.enhanced,compined_ans = determineAnswers(self.enhanced)
                com_ans = com_ans + compined_ans
                f= open("./answers/img" + str(i) + ".csv" , "w+")
                f.write(answer)
                f.close()
                i = i + 1
            f= open("./answers/compined_img.csv" , "w+")
            f.write(com_ans)
            f.close()
        for i in range(101):
            time.sleep(0.005)
            self.progress_bar["value"] = i
            self.progress_bar.update()
        self.progress_bar["value"] = 100
        messagebox.showinfo("Extracting Done", "please find answers in answers folder in same dir.")

    def start_progressbar(self):
        root = tk.Tk()
        root.withdraw()
        self.file_paths = filedialog.askopenfilenames()


    def showenhanced(self):
        cv2.imshow("enhanced",self.enhanced)
        cv2.waitKey(0)
        cv2.destroyAllWindows()


root = Root()
root.mainloop()


    



    
