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
df_main= pd.read_excel(file_path, engine='openpyxl',sheet_name="Sheet1")

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
def my_click(button_number):
    df=df_main.copy()
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
    
    df=df.rename(columns={"viol1_count":"تخلف شماره 1","viol2_count":"تخلف شماره 2","viol3_count":"تخلف شماره 3"})
    sorted_df=df.sort_values([df.columns[6],df.columns[7],df.columns[8]],ascending=[False,False,False])
    print(sorted_df)
        # print(df[df[df.columns[3]]==True].sort_values(df.columns[6]))
    print(sorted_df)
    print("------------")
    sorted_df_summary=sorted_df[[df.columns[1],df.columns[6],df.columns[7],df.columns[8]]]
    print(sorted_df_summary)
    # sorted_df_summary=sorted_df_summary.rename(columns={"viol1_count":"تخلف شماره 1","viol2_count":"تخلف شماره 2","viol3_count":"تخلف شماره 3"})
    sorted_df_summary=sorted_df_summary.drop_duplicates().reset_index(drop=True)
    sorted_df_summary.insert(0, 'ردیف', range(1, len(sorted_df_summary) + 1))
    sorted_df_summary.index=sorted_df_summary.index + 1
    highest_viol=sorted_df[df.columns[1]].unique()
    print(highest_viol)
    df_freq_1=df[df[df.columns[3]]==True]
    print(df_freq_1)
    print("-----------")
    df_freq_2=df[df[df.columns[4]]==True]
    print(df_freq_2)
    print("!!!!!!!!!!")
    df_freq_3=df[df[df.columns[5]]==True]
    print(df_freq_3)
    print("ooooooooooooooooooooooooooooo")
    df_show =pd.DataFrame()
    for i in highest_viol:
        df_show=pd.concat([df_show,df_freq_1[df_freq_1[df_freq_1.columns[1]]==i],df_freq_2[df_freq_2[df_freq_2.columns[1]]==i],
                            df_freq_3[df_freq_3[df_freq_3.columns[1]]==i]],ignore_index=True)
    df_show_fin=df_show.drop(columns=df_show.columns[3:6])
    if button_number==1:

        show(sorted_df_summary[sorted_df_summary.columns[::-1]])
    if button_number==2:
        show(df_show_fin[df_show_fin.columns[::-1]])      
        
    # print(df)
def myclick1(ss):
    if ss==1:
        print ("jamdsffs")
    else:
        print("2 was pressed")
my_button=Button(root,text="لیست دفترخانه ها", command=lambda: my_click(1))
my_button.pack()
my_button1=Button(root,text="لیست دفترخانه ها همراه با جزئیات",command=lambda: my_click(2))
my_button1.pack()
label = Label(root, text="دفاتر اسناد رسمی")
label.pack()
r1=Radiobutton(root,text="کشور",command=myclick1)
r1.pack()
root.mainloop()
