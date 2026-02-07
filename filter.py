import pandas as pd

first_file=pd.read_csv("data/daily_sales_data_0.csv")
second_file=pd.read_csv("data/daily_sales_data_1.csv")
third_file=pd.read_csv("data/daily_sales_data_2.csv")
combined_file=pd.concat([first_file,second_file,third_file])
filtered_file=combined_file[combined_file["product"]== "pink morsel"].copy()
filtered_file['price']=filtered_file['price'].str.replace("$","",regex=False)
filtered_file['price']=filtered_file['price'].astype(float)
filtered_file['Sales']=filtered_file['price']*filtered_file['quantity']
filtered_file.drop('product',axis=1,inplace=True)
filtered_file.drop('price',axis=1,inplace=True)
filtered_file.drop('quantity',axis=1,inplace=True)
filtered_file["region"] = filtered_file["region"].str.strip().str.title()
filtered_file.rename(columns={'date':'Date','region':'Region'},inplace=True)
filtered_file=filtered_file[['Sales','Date','Region']]
filtered_file.to_csv("filtered_file.csv",index=False)