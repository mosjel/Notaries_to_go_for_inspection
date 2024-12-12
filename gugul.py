import pandas as pd
technologies = {
    'Courses':["Spark","PySpark","Hadoop","Python","PySpark","Spark","Spark"],
    'Fee' :[20000,25000,26000,22000,25000,20000,35000],
    'Duration':['30day','40days','35days','40days','60days','60days','70days'],
    'Discount':[1000,2300,1200,2500,2000,2000,3000]
              }

df = pd.DataFrame(technologies)
df.set_index(['Courses','Fee'], inplace=True)
print("Create DataFrame:\n", df)
print(df[df.columns[0]])
print(df.shape)