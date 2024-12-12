import pandas as pd
import os
import openpyxl
from tkinter import ttk
from tkinter import *
import numpy as np



dir_name=os.path.dirname(os.path.abspath(__file__))
os.system('cls' if os.name == 'nt' else 'clear')

df_notary=pd.read_excel(dir_name+"\\"+"notary_address_corrected_FInal_1403_07_23_edited_07_29.xlsx",dtype={1:str})
print(df_notary.head())
notary_list=df_notary[df_notary[df_notary.columns[8]]=="تهران"]["شماره دفترخانه"].unique()
print(notary_list.shape)
print(notary_list)


# print(notary_list[notary_list=="10"].index)
# if "2" in notary_list.values:
#     print("ok")
# else:
#     print("not")
# print(notary_list.isin("2"))
