import tkinter as tk
from tkinter import font
import os
import time
# List of 10 Farsi string variables
s=[]
s.append("--------------------نرم افزار تندر---------------")
s.append("تعیین نوبت دفاتر اسناد رسمی جهت بازرسی")
s.append("بهار 1403- نسخه 1.2")
# s.append ("نسخه 1.1")
s.append("-------------------------")
s.append("مصطفی جلوه")
s.append("Email: mostafaajelveh@gmail.com")# Create the main application window
def welcome():
    def clear_root(root):
        for widget in root.winfo_children():
            widget.destroy()
        root.config(bg="white")
    
    root = tk.Tk()
    root.title("Farsi Text in Tkinter")

        # Set the geometry of the window
    root.geometry("800x600")
    root.config(bg="black")
        # Create a font that supports Farsi
    farsi_font = font.Font(family="Arial", size=14)
    columns = os.get_terminal_size().columns
    def label_initialization(farsi_texts):
    

        # Configure grid columns and rows for proper centering
        root.grid_columnconfigure(0, weight=1)  # Center column
        root.grid_columnconfigure(1, weight=1)  # Right column

            
        for num,i in enumerate(s):
            
            
            # padding = columns - len(i)
            # div_pd=padding//2
            if num<4:
                label = tk.Label(root, text=i, font=farsi_font,fg="#39FF14",bg="black")
                label.grid(row=num+4, column=0, columnspan=2, sticky='n', padx=10, pady=5)
                # print('\033[1m'+'033[38;5;46m'+'-' * (div_pd)+i+'-' * (div_pd))
            else:
                
                # print('\033[1m'+'\033[38;5;15m'+'-' * (div_pd)+i+'-' * (div_pd))
                label = tk.Label(root, text=i, font=farsi_font,fg="white",bg="black")
                label.grid(row=num+4, column=0, columnspan=2, sticky='n', padx=10, pady=5)
        for i in range(6,9):

            label = tk.Label(root, text="*"*50, font=farsi_font,fg="red",bg="black")
            label.grid(row=i+10, column=0, columnspan=2, sticky='n', padx=10, pady=5)
                
        # for i in range(4):   
        #     print()

        # for i in range(7):
        #     print('\033[1m'+"\033[38;5;196m"+"*"*columns)
        
        # time.sleep(5)
            


        
        
            
            # Create labels for each string and place them in the middle of the form
        # for i, text in enumerate(farsi_texts):
        #     label = tk.Label(root, text=text, font=farsi_font,fg="red",bg="black")
            
                
        #     label.grid(row=i, column=0, columnspan=2, sticky='n', padx=10, pady=5)


        # Run the application
    



    label_initialization(s)
    clear_button = tk.Button(root, text="ادامه", command=lambda: clear_root(root), 
                            font=farsi_font, fg="black", bg="white", width=20)  # Increase button width to 20
    clear_button.grid(row=24, column=0, columnspan=2, sticky='n', padx=10, pady=40)

    root.mainloop()


welcome()