import tkinter as tk
from tkinter import ttk

class MultiCheckboxCombobox(ttk.Combobox):
    def __init__(self, master=None, values=[], **kwargs):
        self.master = master
        self.values = values
        self.selected_values = []
        self.checkbox_vars = []
        
        # Create a variable to store selected values and a readonly combobox
        self.combo_var = tk.StringVar()
        super().__init__(master, textvariable=self.combo_var, state="readonly", **kwargs)
        
        # Add event listener to dropdown opening
        self.bind("<Button-1>", self.show_dropdown)
        self.bind("<KeyRelease>", self.search)

        # Create a dropdown frame that will appear when the combobox is clicked
        self.dropdown_frame = None

    def show_dropdown(self, event):
        """Display the dropdown with checkboxes."""
        if self.dropdown_frame:
            return
        
        # Create a new frame that appears below the combobox
        self.dropdown_frame = tk.Toplevel(self.master)
        self.dropdown_frame.wm_overrideredirect(True)
        
        # Position the dropdown frame directly below the combobox
        x = self.winfo_rootx()
        y = self.winfo_rooty() + self.winfo_height()
        self.dropdown_frame.geometry(f"+{x}+{y}")
        
        # Add a scrollbar to handle large number of items
        canvas = tk.Canvas(self.dropdown_frame)
        scrollbar = ttk.Scrollbar(self.dropdown_frame, orient="vertical", command=canvas.yview)
        scrollable_frame = ttk.Frame(canvas)

        scrollable_frame.bind("<Configure>", lambda e: canvas.configure(scrollregion=canvas.bbox("all")))

        canvas.create_window((0, 0), window=scrollable_frame, anchor="nw")
        canvas.configure(yscrollcommand=scrollbar.set)

        # Populate the frame with checkboxes for each item
        self.checkbox_vars.clear()
        for item in self.values:
            var = tk.BooleanVar(value=item in self.selected_values)
            chk = tk.Checkbutton(scrollable_frame, text=item, variable=var, command=self.update_selected_values)
            chk.pack(anchor="w")
            self.checkbox_vars.append((var, item))
        
        canvas.pack(side="left", fill="both", expand=True)
        scrollbar.pack(side="right", fill="y")
        
        # Bind the combobox and dropdown to close when focus is lost
        self.dropdown_frame.bind("<FocusOut>", self.close_dropdown)
        self.dropdown_frame.focus_set()

    def close_dropdown(self, event=None):
        """Close the dropdown and destroy the frame."""
        if self.dropdown_frame:
            self.dropdown_frame.destroy()
            self.dropdown_frame = None

    def update_selected_values(self):
        """Update the selected values and display them in the combobox."""
        self.selected_values = [item for var, item in self.checkbox_vars if var.get()]
        self.combo_var.set(", ".join(self.selected_values))

    def search(self, event):
        """Search and filter items in the dropdown."""
        search_value = self.get().lower()
        for var, item in self.checkbox_vars:
            # Show or hide checkboxes based on search
            if search_value in item.lower():
                var.get()  # Keep the state of the checkbox if it matches
            else:
                var.set(False)  # Uncheck unchecked items
        # Update the displayed items in the dropdown based on the search
        self.update_dropdown_display(search_value)

    def update_dropdown_display(self, search_value):
        """Update the visibility of checkboxes based on the search value."""
        for var, item in self.checkbox_vars:
            if search_value in item.lower():
                var.set(True)  # Keep checked for matching items
            else:
                var.set(False)  # Uncheck if it doesn't match

# Sample data for the combobox
lst = [f"Option {i}" for i in range(1, 1001)]  # Example of 1000 choices

# Create the main window
root = tk.Tk()
root.title("بازرسی")
root.geometry("800x600")

label1 = tk.Label(root, text=":(1) نوع تخلف را وارد نمایید")
label1.pack()

# Create and display the multi-select combobox
multi_select_combobox = MultiCheckboxCombobox(root, values=lst)
multi_select_combobox.pack(padx=10, pady=20)

# Start the Tkinter event loop
root.mainloop()
