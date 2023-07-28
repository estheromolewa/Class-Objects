import customtkinter as ct

def button_callback():
    print("button pressed")

def button_callback():
    print("button pressed")


if __name__=="__main__":

    window = ct.CTk()
    window.title("my window")
    window.geometry("400x150")
    window.grid_columnconfigure(0,weight=1)

    button = ct.CTkButton(window, text="my button", command=button_callback, corner_radius=10)
    #button.grid(row=0, column=0, padx=(0,10), columnspan=2, pady=20, sticky="ew")
    button.grid(row=0, column=0, padx=10,  pady=20, sticky="ns")

    
    button = ct.CTkButton(window, text="my butt", command=button_callback, corner_radius=10)
    button.grid(row=0, column=1, padx=10, pady=20, sticky="n")

    button = ct.CTkButton(window, text="my butting", command=button_callback, corner_radius=10)
    button.grid(row=0, column=2, padx=10, pady=20, sticky="n")

    check1 = ct.CTkCheckBox(window, text="girl")
    check1.grid(row=1, column=0, padx=(0,10), pady=20, sticky="w")

    check2 = ct.CTkCheckBox(window, text="boy")
    check2.grid(row=1, column=1, padx=10, pady=20)

    
    
    window.mainloop()