from tkinter import *

def show_selection():
    selected_value = selected_option.get()
    print(f"Selected option: {selected_value}")

# Initialize the main window
root = Tk()
root.title("Radio Button Example")
root.geometry("200x200")  # Adjusted size to make sure everything fits well

# Create a frame to act as a panel for better organization
frame = Frame(root, borderwidth=2, relief="solid")
frame.pack()

# Create a variable to hold the selected option
selected_option = StringVar()
selected_option.set("Option 1")  # Set default option

# Create and place the label in the frame
label = Label(frame, text="Select an option:")
label.pack()  # Padding around the label

# Create and place the radio buttons in the frame
radio1 = Radiobutton(frame, text="Option 1", variable=selected_option, value="Option 1")
radio1.pack()  # Padding inside the frame

radio2 = Radiobutton(frame, text="Ostan", variable=selected_option, value="Option 2")
radio2.pack()  # Padding inside the frame

radio3 = Radiobutton(frame, text="Shahr", variable=selected_option, value="Option 3")
radio3.pack()  # Padding inside the frame
comb1=
# Create and place the button in the frame
button = Button(root, text="Show Selection", command=show_selection)
button.pack()  # Padding around the button

# Run the Tkinter event loop
root.mainloop()
