import pandas as pd
from pandasgui import show
import tkinter as tk
from tkinter import messagebox

def custom_action():
    # Example custom action: print the DataFrame to console
    print(df)

# Create sample DataFrame
data = {'A': [1, 2, 3], 'B': [4, 5, 6]}
df = pd.DataFrame(data)

# Create tkinter window
root = tk.Tk()
root.title("Custom PandasGUI Interface")

# Add button to tkinter window
button = tk.Button(root, text="Show PandasGUI", command=lambda: show(df))
button.pack(pady=10)

# Add custom action button
custom_button = tk.Button(root, text="Custom Action", command=custom_action)
custom_button.pack(pady=10)

# Start the tkinter main loop
root.mainloop()
