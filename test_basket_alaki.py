import numpy as np
import pandas as pd
import math
notary_list=list(range(1,6))
notary_list.append("")
print(notary_list)
notary_list=np.array(notary_list).astype("str")

print(notary_list)
print(notary_list.shape)
list1=([1,10,100,3])

list1=[str(i) for i in list1]
list1.append(math.nan)
list1=np.array(list1)

notary_list_not_exist=np.invert(np.isin(notary_list,list1))
list1_not_exist=np.invert(np.isin(list1,notary_list))
print(notary_list)
print(list1)
print(notary_list[notary_list_not_exist])
print(list1[list1_not_exist])

















# df_rule_cont=df_merged[df_merged[df.columns[5]] != "تخلف ندارد"]

# df_rule_cont[df_rule_cont.columns[2]]=df_rule_cont[df_rule_cont.columns[2]].fillna("")


# df_rule_cont["georgian"]=df_rule_cont[df_rule_cont.columns[2]].apply (lambda x:persian_to_georgian(x))
# print(df_rule_cont)



# df_error=df_rule_cont[df_rule_cont[df_rule_cont.columns[8]]=="Error"]
# df_na=df_rule_cont[df_rule_cont[df_rule_cont.columns[8]].isnull()]

# df_rule_cont[df_rule_cont.columns[8]]=pd.to_datetime(df_rule_cont[df_rule_cont.columns[8]],errors="coerce").dt.date
# print(df)
# df_rule_cont.dropna(subset=[df_rule_cont.columns[8]], inplace=True)


# df_dates=df_rule_cont[df_rule_cont.groupby(df_rule_cont.columns[4],dropna=False)[df_rule_cont.columns[8]].transform("max")==df_rule_cont[df_rule_cont.columns[8]]]
# df_dates=df_dates.sort_values(df_dates.columns[8],ascending=True)

# df_org=pd.concat([df_error,df_na,df_dates])



# output_file_path=r"C:\Users\VAIO\Desktop\test\Book2.xlsx"
# df_org.to_excel(output_file_path,index=False)

# # with pd.ExcelWriter(file_path, engine='openpyxl', mode='a', if_sheet_exists='replace') as writer:
# #     # Write the new data to "Sheet2"
# #     new_data.to_excel(writer, sheet_name='Sheet2', index=False)
# print("!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!")
# workbook = openpyxl.load_workbook(output_file_path)
# sheet = workbook.active

# # Set the sheet to RTL mode
# from openpyxl.styles import Alignment

# sheet.sheet_view.rightToLeft = True
# for row in sheet.iter_rows():
#     for cell in row:
#         # Set text direction to right-to-left by setting reading order
#         cell.alignment = Alignment(wrap_text=True,readingOrder=2,vertical="center",horizontal="center")

# # Save the changes to the workbook

# # Save the workbook with the RTL modification
# workbook.save(output_file_path)


