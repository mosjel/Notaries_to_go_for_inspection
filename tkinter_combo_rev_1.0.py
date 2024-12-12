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
file_path = dir_name+"\\"+"takhalof.xlsx"
# df = pd.read_excel(file_path, engine='openpyxl',usecols=
                #    list(range(0,7)),sheet_name="Sheet1",dtype=column_dtype)
df = pd.read_excel(file_path, engine='openpyxl',sheet_name="Sheet1")

def search(event,combo_box):
    global value,lst
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
combo_box1.bind("<KeyRelease>",lambda event: search(event, combo_box1))

label2=Label(root,text=":(2)نوع تخلف را وارد نمایید")
label2.pack()
combo_box2=ttk.Combobox(root,value=lst)
combo_box2.set("Search")
combo_box2.pack()
combo_box2.bind("<KeyRelease>",lambda event: search(event, combo_box2))

label3=Label(root,text=":(3)نوع تخلف را وارد نمایید")
label3.pack()
combo_box3=ttk.Combobox(root,value=lst)
combo_box3.set("Search")
combo_box3.pack()
combo_box3.bind("<KeyRelease>",lambda event: search(event, combo_box3))
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
    sorted_df_summary=sorted_df[[df.columns[1],df.columns[6],df.columns[7],df.columns[8]]]

    sorted_df_summary=sorted_df_summary.rename(columns={"viol1_count":"تخلف شماره 1","viol2_count":"تخلف شماره 2","viol3_count":"تخلف شماره 3"})
    sorted_df_summary=sorted_df_summary.drop_duplicates().reset_index(drop=True)
    sorted_df_summary.insert(0, 'ردیف', range(1, len(sorted_df_summary) + 1))
    sorted_df_summary.index=sorted_df_summary.index + 1
    show(sorted_df_summary[sorted_df_summary.columns[::-1]])
    highest_viol=sorted_df[df.columns[1]].unique()
    # print(df)
def myclick1():
    print ("jamdsffs")
my_button=Button(root,text="لیست دفترخانه ها",command=myclick)
my_button.pack()
my_button1=Button(root,text="لیست دفترخانه ها همراه با جزئیات",command=myclick1)
my_button1.pack()
root.mainloop()
