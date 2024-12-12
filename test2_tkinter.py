import tkinter as tk
from tkinter import font

# Create the main application window
root = tk.Tk()
root.title("Farsi Text in Tkinter")

# Set the geometry of the window (adjust as needed)
root.geometry("400x300")

# Create a font that supports Farsi
farsi_font = font.Font(family="Arial", size=14)

# Configure grid columns and rows
root.grid_columnconfigure(0, weight=1)
root.grid_columnconfigure(1, weight=0)

# Create a label with Farsi text
farsi_text = tk.Label(root, text="سلام دنیا", font=farsi_font)

# Place the label in the top right corner using grid with sticky
farsi_text.grid(row=0, column=1, sticky='ne', padx=(0, 10), pady=(10, 0))

# Run the application
root.mainloop()
