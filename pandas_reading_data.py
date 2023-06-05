import pandas as pd


"""Excel"""
data=pd.read_excel("C:/Users/CMR/Downloads/data.xlsx")
df=pd.DataFrame(data)
#print(df)


"""CSV"""
data=pd.read_csv("C:/Users/CMR/Downloads/ekwense/ekwense/scratchs/data/DATA.csv")
df=pd.DataFrame(data)
#print(df)

"""
print(df.head(104) #this will print the top 104 Rows and All Columns
print(df.tail(20)) #this will print the Bottom 20 Rows and All Columns
print(df.describe()) #this will print description of Rows and All Columns
print(df.shape)      #this will print the shape of Rows and Columns
print(df[12:21:2])
print(df['Open'])
print(df[['Open','Close']])
print(df[['Open','Close']][12:23:3])
"""

"""
for rec in df.iterrows():
    print(rec)
"""

"""
loc1=df.loc[12]
#print(loc1)
loc11=df.loc[1:12]
#print(loc11)    #it will includes the last index also
iloc11=df.iloc[1:12]
#print(loc12)    #it will exclude the last index value
loc13=df.loc[1:12,["Open","Low"]]
print(loc13)    #it will select the Open, Low Columns
loc14=df.loc[1:12,"Open":"Volume"]
print(loc14)    #it will select the Open to Volume Columns
"""

"""
iloc12=df.iloc[2,5]
print(iloc12)   #it will print the matrix value 
iloc13=df.iloc[0:10,0:4]
print(iloc13)   #this will print the upto 10 rows and 4 columns
iloc14=df.iloc[0:10,3]
print(iloc14)   #this will print the 10 rows and only 3rd column
iloc15=df.iloc[:,[2,3]] 
print(iloc15)   #This will print the all rows and 2nd and 3rd columns values
"""

"""
data1=df.sort_values("Open")
print(data1)    #this Will sort the values in ascending Order
data2=df.sort_values("Open",ascending=False)
print(data2)    #This will sort the values by desending order
data3=df.sort_values(["Volume","Open"])
print(data3)    #This will sort the values by Volume and open Based values
"""

df["Change"]=((df["Open"]-df["Close"])/df["Close"])*100
data1=df["Change"]
print(data1)

