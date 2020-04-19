import pandas as pd


#=============================Slicing====================================================
XYZ_web = {
    'Day':[1, 2, 3, 4, 5, 6],
    'visitors':[1000, 700, 6000, 1000, 400, 350],
    'Bounce_rate': [20, 20, 23, 15, 10, 34]
}

df = pd.DataFrame(XYZ_web)
print(df)

print(df.head(3))#print the first 3 row of the column
print(df.tail(2))#print the last 2 row of the column



#====================================Merging and joining===============================
df1 = pd.DataFrame({'HPI':[80, 90, 70, 60], 'Int_Rate':[2, 1, 2, 3], 'IND_GDP':[50, 45, 45, 67]}, index=[2001, 2002, 2003, 2004])

df2 = pd.DataFrame({'HPI':[80, 90, 70, 60], 'Int_Rate':[2, 1, 2, 3], 'IND_GDP':[50, 45, 45, 67]}, index=[2005, 2006, 2007, 2008])

merged = pd.merge(df1, df2, on='HPI')
print(merged)#merge function is adding new rows


df1 = pd.DataFrame({'Int_Rate':[2, 1, 2, 3], 'IND_GDP':[50, 45, 45, 67]}, index=[2001, 2002, 2003, 2004])
df2 = pd.DataFrame({'Low_tier':[50, 45, 45, 67], 'Unemployment':[1,  3, 5, 6]}, index=[2001, 2003, 2004, 2004])

joined = df1.join(df2)#column is adding new columns
print(joined)

#concactenation

df3 = pd.DataFrame({'HPI':[80, 90, 70, 60], 'Int_Rate':[2, 1, 2, 3], 'IND_GDP':[50, 45, 45, 67]}, index=[2001, 2002, 2003, 2004])

df4 = pd.DataFrame({'HPI':[80, 90, 70, 60], 'Int_Rate':[2, 1, 2, 3], 'IND_GDP':[50, 45, 45, 67]}, index=[2005, 2006, 2007, 2008])
concat = pd.concat([df3, df4])
concat2 = pd.concat([df3, df4], axis=1)
print(concat)
print(concat2)


#==========================================================changing the index=======================================================
XYZ_web = {
    'Day':[1, 2, 3, 4, 5, 6],
    'visitors':[1000, 700, 6000, 1000, 400, 350],
    'Bounce_rate': [20, 20, 23, 15, 10, 34]
}

df = pd.DataFrame(XYZ_web)
df.set_index('Day', inplace=True)
print(df)

#changing a column
df = df.rename(columns={'visitors':'Users'})
print(df)

#================================================Data Munging or convertion===========================================
EUR_USD = pd.read_csv('EUR_USD_15mn.csv')
EUR_USD.to_html('educ.html')

