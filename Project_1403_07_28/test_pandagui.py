import warnings
warnings.filterwarnings("ignore", category=FutureWarning)
warnings.simplefilter(action='ignore', category=FutureWarning)
from tkinter import *
from tkinter import ttk
import os
import openpyxl
import pandas as pd
from pandasgui import show



lst=["داشتن دستگاه پوز نامناسب", "کشیدن مبلغ اضافی","تاخیر در انجام کار","بسته بودن دفترخانه"]
dir_name=os.path.dirname(os.path.abspath(__file__))
os.system('cls' if os.name == 'nt' else 'clear')
file_path = dir_name+"\\"+"notaries_togo.xlsx"
# df = pd.read_excel(file_path, engine='openpyxl',usecols=
                #    list(range(0,7)),sheet_name="Sheet1",dtype=column_dtype)
df_main= pd.read_excel(file_path, engine='openpyxl',sheet_name="Sheet1")





root=Tk()
root.title("بازرسی")
root.geometry("800x600")


def my_click():
    show(df_main[df_main.columns[::-1]])
my_button=Button(root,text="نمایش", command=lambda: my_click())
my_button.pack()
root.mainloop()
