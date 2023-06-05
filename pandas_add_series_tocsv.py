import pandas as pd
from datetime import datetime

data = {'first_name': ['Sigrid', 'Joe', 'Theodoric','Kennedy', 'Beatrix', 'Olimpia', 'Grange', 'Sallee'],
        'last_name': ['Mannock', 'Hinners', 'Rivers', 'Donnell', 'Parlett', 'Guenther', 'Douce', 'Johnstone'],
        'age': [27, 31, 36, 53, 48, 36, 40, 34],
        'amount_1': [7.17, 1.90, 1.11, 1.41, 6.69, 4.62, 1.01, 4.88],
        'amount_2': [8.06,  "?", 5.90,  "?",  "?", 7.48, 4.37,  "?"],
        'date_of_birth':['2009-09-20 1:12:33','1992-09-08 1:12:33',"1996-02-09 1:12:33","1996-02-09 1:12:33",'1996-02-09 1:12:33',"1996-02-09 1:12:33","1996-02-09 1:12:33",'2001-11-21 1:12:33']}
df = pd.DataFrame(data)
print(df)
df['gender']=pd.Series(['Male','Female','Male','Male','Female','Female','Male','Female'])
print(df)

df.to_csv('example.csv')
print('----------------------------------------------------------------------------------------------------------------------')
df1=pd.Series([1,2,3,8,9,10])
df2=pd.Series([3,4,5,9,10])
df3=df2[~df2.isin(df1)]
print(df3)
print('----------------------------------------------------------------------------------------------------------------------')

dateparser= lambda date_val:datetime.strptime(date_val, '%Y-%m-%d %H:%M:%S')
df=pd.read_csv("example.csv", parse_dates=['date_of_birth'], date_parser=dateparser)
print(df)
