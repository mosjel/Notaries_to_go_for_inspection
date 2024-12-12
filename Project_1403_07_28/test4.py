import numpy as np
import pandas as pd

# Create dataframes s and s1
s = pd.DataFrame({
    "class": ["1", "2", "5", "2", "4", "2", "1"],
    "number": [10, 20, 30, 40, 50, 60, 10],
    "city": ["tehran", "isfahan", "tabriz", "urumieh", "", "shahsavar", ""]
})
s["number"]=s["number"].astype(str)
s1 = pd.DataFrame({
    "levels": ["1", "2", "100", "", "5","1","5"],"gigili":["10","40","300","400","500","10","isfahan"]
})

def notary_adddress_concat(df1,df_address,base_df_col_num,sec_df_col_num):

    df_address=df_address.drop_duplicates(subset=df_address.columns[sec_df_col_num])
    
# Merge s1 with s based on matching values in s1["levels"] and s["class"]
# Include s index as a new column in s1 called "index_1"
    merged_df = df1.merge(df_address, left_on=[df1.columns[base_df_col_num]], right_on=[df_address.columns[sec_df_col_num]], how="left")
# merged_df = s1.merge(s.reset_index(), left_on="levels", right_on="class", how="left")
    # merged_df = merged_df.rename(columns={"index": "index_1"})
    # merged_df=merged_df.drop_duplicates(subset=merged_df.columns[base_df_col_num])
    return(merged_df)


result=notary_adddress_concat(s1,s,0,0)


print(result)
