#importing libraries 
import numpy as np
import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt
df=pd.read_csv("laptop_data.csv")
print(df.head())
print(df.shape)
#check missing values 
print(df.info)
#checking duplicate rows 
print(df.duplicated().sum()) #no duplicated
#checking null data 
print(df.isnull().sum())  #no null data 
#preprocessing 
df.drop(columns=["Unnamed: 0"],inplace=True)
print(df.head())
#delete GB from ram and kg from weight
df['Ram'] = df['Ram'].str.replace('GB','')
df['Weight'] = df['Weight'].str.replace('kg','')
df['Ram'] = df['Ram'].astype('int32')
df['Weight'] = df['Weight'].astype('float32')
print(df.head())
df.info()
sns.histplot(df['Price']) #return histofgram of the prices 
plt.show()
df['Company'].value_counts().plot(kind='bar')
plt.show()

sns.barplot(x=df['Company'],y=df['Price'])
plt.xticks(rotation='vertical')
plt.show()
df['TypeName'].value_counts().plot(kind='bar')
plt.show()
sns.barplot(x=df['TypeName'],y=df['Price'])
plt.xticks(rotation='vertical')
plt.show()
sns.histplot(df['Inches'])
plt.show()
sns.scatterplot(x=df['Inches'],y=df['Price'])
df['ScreenResolution'].value_counts()
df['Touchscreen'] = df['ScreenResolution'].apply(lambda x:1 if 'Touchscreen' in x else 0) 
print(df.sample(20))
df['Touchscreen'].value_counts().plot(kind='bar')
plt.show()

sns.barplot(x=df['Touchscreen'],y=df['Price'])
plt.show()
df['Ips'] = df['ScreenResolution'].apply(lambda x:1 if 'IPS' in x else 0)
df.head()
df['Ips'].value_counts().plot(kind='bar')
sns.barplot(x=df['Ips'],y=df['Price'])
new = df['ScreenResolution'].str.split('x',n=1,expand=True)
df['X_res'] = new[0]
df['Y_res'] = new[1]
print(df.sample(5))
df['X_res'] = df['X_res'].str.replace(',','').str.findall(r'(\d+\.?\d+)').apply(lambda x:x[0]) 
print(df.head())
#from object to integer
df['X_res'] = df['X_res'].astype('int')
df['Y_res'] = df['Y_res'].astype('int')
print(df.info())
print(df.corr()['Price'])
df['ppi'] = (((df['X_res']**2) + (df['Y_res']**2))**0.5/df['Inches']).astype('float') #function to represent pixel per inch new feature
print(df.corr()['Price'])
df.drop(columns=['ScreenResolution'],inplace=True)
print(df.head())
df.drop(columns=['Inches','X_res','Y_res'],inplace=True)
print(df.head())
df['Cpu'].value_counts()
df['Cpu Name'] = df['Cpu'].apply(lambda x:" ".join(x.split()[0:3])) #extract cpu name as new feature
print(df.head())
def fetch_processor(text):
    if text == 'Intel Core i7' or text == 'Intel Core i5' or text == 'Intel Core i3':
        return text
    else:
        if text.split()[0] == 'Intel':
            return 'Other Intel Processor'
        else:
            return 'AMD Processor'
df['Cpu brand'] = df['Cpu Name'].apply(fetch_processor)            
print(df.head())
df['Cpu brand'].value_counts().plot(kind='bar')
sns.barplot(x=df['Cpu brand'],y=df['Price'])
plt.xticks(rotation='vertical')
plt.show()

df.drop(columns=['Cpu','Cpu Name'],inplace=True)
print(df.head())
