import pandas as pd

df=pd.read_csv('combined.csv')

df['xmax']= df['xmin']+df['width']
df['ymax']= df['ymin']+df['height']  #calculate xmax and ymax

df= df.drop(df.columns[0], axis=1)    #removal of unncessary fields
df= df.drop(df.columns[0], axis=1)
df= df.drop(df.columns[3], axis=1)
df= df.drop(df.columns[3], axis=1)

df = df.dropna()                               #removal of null rows

df[['del1','del2','file_name']] = df.file_name.str.split("_",n=3,expand=True)     #spliting of filename,removal of the file path name
df= df.drop(df.columns[0], axis=1)                                        #removal of del1 and del2
df= df.drop(df.columns[0], axis=1)

df.to_csv('data2.csv',index = False)
