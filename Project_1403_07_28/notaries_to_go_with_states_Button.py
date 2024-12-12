import pandas as pd
import os
import openpyxl
from tkinter import ttk
from tkinter import *
import numpy as np
from collections import Counter
def search(event,combo_box,lst):
    global value
    value=event.widget.get()
    if value=="":
        combo_box["value"]=lst
    else:
        data=[]
        for item in lst:
            if value.lower() in item.lower():
                data.append(item)
        combo_box["value"]=data
def my_click():
    
    choosen1=combo_box1.get()
    print(choosen1)
    df_notary=pd.read_excel(dir_name+"\\"+"notary_address_corrected_FInal_1403_07_23_edited_07_29.xlsx",dtype={1:str})
    notary_list=np.array((df_notary[df_notary["شهر"]==choosen1])["شماره دفترخانه"])
    np.set_printoptions(threshold=np.inf) 
    print((notary_list.shape))
    notary_list=np.unique(notary_list)
df_h=({"hamed":[1,2,3,1],"asghar":[5,6,7,8]})
df_h=pd.DataFrame(df_h)
print(df_h.iloc[:,0].unique())
dir_name=os.path.dirname(os.path.abspath(__file__))
os.system('cls' if os.name == 'nt' else 'clear')
df_notary=pd.read_excel(dir_name+"\\"+"notary_address_corrected_FInal_1403_07_23_edited_07_29.xlsx")
df_new=df_notary.iloc[:,8].unique()
df_new=list(df_new)
print(df_new)

# def_new=pd.DataFrame(df_new)
# print(def_new)
# print(type(def_new))
# output_file_path=dir_name+"\\"+"test_new1.xlsx"
# with pd.ExcelWriter(output_file_path, engine='openpyxl', mode='w') as writer:
#     def_new.to_excel(writer, index=False)
root=Tk()
root.title("بازرسی")
root.geometry("800x600")
label1=Label(root,text="شهر")
label1.pack()
combo_box1=ttk.Combobox(root,value=df_new)
combo_box1.set("Search")
combo_box1.pack()
combo_box1.bind("<KeyRelease>",lambda event: search(event, combo_box1,df_new))

my_button=Button(root,text="لیست دفترخانه ها", command=lambda: my_click())
my_button.pack()
root.mainloop()

