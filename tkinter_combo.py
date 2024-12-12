from tkinter import *
from tkinter import ttk
import os
import openpyxl
import pandas as pd
lst=["داشتن دستگاه پوز نامناسب", "کشیدن مبلغ اضافی","تاخیر در انجام کار","بسته بودن دفترخانه"]
dir_name=os.path.dirname(os.path.abspath(__file__))
os.system('cls' if os.name == 'nt' else 'clear')
file_path = dir_name+"\\"+"takhalof.xlsx"
# df = pd.read_excel(file_path, engine='openpyxl',usecols=
                #    list(range(0,7)),sheet_name="Sheet1",dtype=column_dtype)
df = pd.read_excel(file_path, engine='openpyxl',sheet_name="Sheet1")

def search(event):
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

root=Tk()
root.title("بازرسی")
root.geometry("800x600")
label1=Label(root,text=":(1)نوع تخلف را وارد نمایید")
label1.pack()
combo_box1=ttk.Combobox(root,value=lst)
combo_box1.set("Search")
combo_box1.pack()
combo_box1.bind("<KeyRelease>",search)

label2=Label(root,text=":(2)نوع تخلف را وارد نمایید")
label2.pack()
combo_box2=ttk.Combobox(root,value=lst)
combo_box2.set("Search")
combo_box2.pack()
combo_box2.bind("<KeyRelease>",search)

label3=Label(root,text=":(3)نوع تخلف را وارد نمایید")
label3.pack()
combo_box3=ttk.Combobox(root,value=lst)
combo_box3.set("Search")
combo_box3.pack()
combo_box3.bind("<KeyRelease>",search)
def myclick():
    choosen1=combo_box1.get()
    choosen2=combo_box2.get()
    choosen3=combo_box3.get()
    df["viol1"]=""
    df["viol2"]=""
    df["viol3"]=""

    for i,takh in enumerate(df[df.columns[2]]):
        if choosen1 in takh:
            df.at[i,"viol1"]=True
        else:
            df.at[i,"viol1"]=False
            
        if choosen2 in takh:
            df.at[i,"viol2"]=True
        else:
            df.at[i,"viol2"]=False
        if choosen3 in takh:
            df.at[i,"viol3"]=True
        else:
            df.at[i,"viol3"]=False
    df["viol1_count"]=""
    df["viol2_count"]=""
    df["viol3_count"]=""
    df["viol1_count"]=df.groupby(df.columns[1])[df.columns[3]].transform(lambda x:(x==True).sum())
    df["viol2_count"]=df.groupby(df.columns[1])[df.columns[4]].transform(lambda x:(x==True).sum())
    df["viol3_count"]=df.groupby(df.columns[1])[df.columns[5]].transform(lambda x:(x==True).sum())
    print("gigili")
    print(df)
    sorted_df=df.sort_values([df.columns[6],df.columns[7],df.columns[8]],ascending=[False,False,False])

    # print(df[df[df.columns[3]]==True].sort_values(df.columns[6]))
    print(sorted_df)
    print("------------")
    print(sorted_df[df.columns[1]])
    
    # print(df)

my_button=Button(root,text="Click me",command=myclick)
my_button.pack()
root.mainloop()
