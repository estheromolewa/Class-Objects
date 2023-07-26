from typing import Optional, Tuple, Union
import customtkinter as ct

class App(ct.CTk):
    def __init__(self):
        super().__init__()
        self.title("I will overcome you seyyy")
        self.geometry("500x500")
        self.columnconfigure(0, weight=1)
        self.rowconfigure(0,weight=1)


        self.checkbox_frame = ct.CTkFrame(self)
        self.checkbox_frame.grid(row=0, column=0, padx= 10, pady=20, sticky="nsw")
        self.checkbox_1 = ct.CTkCheckBox(self.checkbox_frame, text="Boy")
        self.checkbox_1.grid(row=0, column=0, padx=20, pady=( 20), sticky="w")
        self.checkbox_2 = ct.CTkCheckBox(self.checkbox_frame, text="Girl")
        self.checkbox_2.grid(row=1, column=0, padx=20, pady=( 20), sticky="w")

        self.button = ct.CTkButton( self,text= "no wahala")
        self.button.grid(row=1, column=0,sticky="we")

if __name__=="__main__":
    app1 = App()
    app1.mainloop()