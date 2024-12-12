import tkinter as tk
from tkinter import font
import os

# List of Farsi string variables
s = []
s.append("--------------------نرم افزار تندر---------------")
s.append("تعیین نوبت دفاتر اسناد رسمی جهت بازرسی")
s.append("بهار 1403- نسخه 1.2")
# s.append("نسخه 1.1")
s.append("-------------------------")
s.append("مصطفی جلوه")
s.append("Email: mostafaajelveh@gmail.com")

# Create the main application window
def label_initialization(farsi_texts):
    root = tk.Tk()
    root.title("Farsi Text in Tkinter")

    # Set the geometry of the window
    root.geometry("800x600")
    root.config(bg="black")

    # Create a font that supports Farsi
    farsi_font = font.Font(family="Arial", size=14)

    # Configure grid columns and rows for proper centering
    root.grid_columnconfigure(0, weight=1)  # Center column
    root.grid_columnconfigure(1, weight=1)  # Right column

    # Start placing the first set of labels starting from row 4
    for num, i in enumerate(s):
        if num < 4:
            # Use neon green (#39FF14) for the first 4 items
            label = tk.Label(root, text=i, font=farsi_font, fg="#39FF14", bg="black")
        else:
            # Use white for the rest of the items
            label = tk.Label(root, text=i, font=farsi_font, fg="white", bg="black")
        
        label.grid(row=num + 4, column=0, columnspan=2, sticky='n', padx=10, pady=5)

    # Add '*' pattern starting from row 10
    for i in range(3):  # Create 3 rows of stars
        label = tk.Label(root, text="*" * 50, font=farsi_font, fg="red", bg="black")
        label.grid(row=i + 10, column=0, columnspan=2, sticky='n', padx=10, pady=5)

    # Run the application
    root.mainloop()

label_initialization(s)
