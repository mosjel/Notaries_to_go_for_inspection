
# import jdatetime
# import pandas as pd
# s="1396/2/30"
# l=s.split("/")
# l=[int(i) for i in l]
# # gregorian_date = jdatetime.date(1396,2,30).togregorian()
# gregorian_date = jdatetime.date(l[0],l[1],l[2]).togregorian()
# print (gregorian_date)

# def persian_to_georgian(persin_date):
#     try:
#         date_list=persin_date.split("/")
#         date_list=[int(i) for i in date_list]
#         gregorian_date=jdatetime.date(date_list[0],date_list[1],date_list[2]).togregorian()
#         return(gregorian_date)
#     except Exception as e:
#         return e
    
        

# print(persian_to_georgian("1403//03/16")


import os

s=os.path.dirname(os.path.abspath(__file__))
s=s+"\\"+"hamed.txt"
print(s)

print(s)
print(u'\u2713')