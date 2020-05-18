
import pandas as pd

df= pd.read_csv('dataset2.csv')
for col in df.columns:
    if "attribute" in col:
        df= df.drop(col, axis=1)          #removal of Unncessary attribute columns
df= df.drop(['scene_id'], axis=1)
i=1
j=5
k=0                                   # splitting the csv into 20 different csv with each row indicating a single person identidification
while(j<=82):
    df1= df[df.columns[0]]
    df2= df[df.columns[i:j]]
    result = pd.concat([df1, df2], axis=1, sort=False)
    result.columns = ['file_name','xmin','ymin','width','height']   #rename all column names
    with open(f"out{k}.csv","w") as fo:
            fo.write(result.to_csv())
    k=k+1
    i = i+4
    j= j+4

i=0
df3 = pd.DataFrame()
print(df3)                                #combining all csv to obtain only one csv
while(i<20):
    with open(f"out{i}.csv","r") as fo:
         df1= pd.read_csv(fo)
    df3 = pd.concat([df3, df1], axis=0, sort=False)
    i = i+1
df3.to_csv('combined.csv')
    

        
        
    
