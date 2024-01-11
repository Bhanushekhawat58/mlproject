# #import pandas as pd
# from pandas import *
# # print(pd)

# data = [2,3,4,5,5]

# df =DataFrame(data)
# print(df)

# data ={
#     "id":[2,3,4],"name":["user1","user2","user3"],"salary":[300,400,500]


# }
# row =["r1","r2","r3"]

# df = pd.DataFrame(data , index=row)
# print(df)
 


# import pandas as pd
# print(pd)


# data={
#     'name':["user1","user2","user3","user4","user5"],
#     'id':[121,131,141,151,161,],
#     'salary':[2500,2500,2500,2500,2500],
#     'mobile num':["******","*******","*******","*****"]
    
    

# }

# print(data.keys())  



    




# # print(data.head(15866))



# data1 = data["Player"].head(10).values 
# print(data1)

# if 'SR Tendulkar (INDIA' in data1:
#     print("found")
# else :
#     print("not found")



# import pandas as pd 

# data=pd.read_csv('ODI data.csv')
# print(data)

# print(data.head(2584))
# print(data['Player'])
# print(data['Player'].values)

# n1=data['Span'].head(20).values
# n2=data['Player'].head(20).values
# print("n1=",n1)
# print("n2=",n2)

# if '2000-2015'in n1:
#     if  'SR Tendulkar (INDIA)' in n2:
#         print('found')

# else:
#     print("not found")




import pandas as pd 
data=pd.read_csv("ODI data.csv")
print(data)

n1=data['Player'].head[20].values
n2=data['Mat'].head[20].values

print('n1=',n1)
print('n2=',n2)


if 'MS Dhoni (Asia/INDIA)'in n1:
    if '463' in n2:
        print('found')
        
else :
    print('not found')


















# import pandas as pd
# data=pd.read_csv('ODI data.csv')
# print(data)

# import pandas as pd

# data=pd.read_csv('ODI data.csv')
# print(data)

# print(data['Player'].values)

# n1=data['Player'].head(10).values
# n2=data['Runs'].head(10).values

# print("n1=",n1)
# print("n2=",n2)

# if 'V Kohli (INDIA)'in n1:
#     if '12650'in n2:
#         print("found")


# import pandas as pd
# data=pd.read_csv('ODI data.csv')
# m=data['Player'][0]
# print(m)
# m1 =(m.split('(')[1].split(')')[0])
# print(m1)





    


# import pandas as pd 
# df=pd.read_csv("ODI data.csv")
# print(df)












