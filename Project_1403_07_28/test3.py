import numpy as np
import pandas as pd


s=pd.DataFrame({"class":["1","2","5","3","4","6","1"],
                "number":[10,20,30,40,50,60,10],"city":["tehran","isfahan","tabriz","urumieh","","shahsavar",""]})


print(s)
s1=pd.DataFrame({"levels":["1","2","100","","3"]})
print(s1)

# ou1=s[s[s.columns[0]].isin(member_list)]
# ou2=ou1[ou1[ou1.columns[2]].isin(["tehran","urumieh"])]

# total_list=np.array(s[s.columns[0]])
# member_list=np.array(ou2[ou2.columns[0]])
# print(member_list,"grtgrtrttr")
# final_list=np.isin(total_list,member_list)

# print(ou2)
# print(final_list)
