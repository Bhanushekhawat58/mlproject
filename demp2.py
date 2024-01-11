# from pandas import *
# data = [34,5,6,7,8]
# data1 =["user1","user2","user3","user4","user5"]
# df = DataFrame([data,data1])
# print(df)

# col = ['c1','c2','c3','c4','c5']
# df = DataFrame([data,data1],columns=col)
# print(df)
# row=['r1','r2']
# df = DataFrame([data,data1],columns=col,index=row)
# print(df) 

# data ={
#     "id":[2,3,4],
#     "name":["user1","user2","user3"],
#     "salary":[300,400,500]
# }

# df = DataFrame(data)
# print(df)

# print(df.head(0).values)


import pandas as pd
df=pd.read_csv('ODI data.csv')
print(df)
# print(df.head (0).values)
# col=df.head(1).values
# print(col)

# col1 = df.loc[100:]  
# print(col1)
# col1=df.loc[:200]
# print(col1)

# col1 = df.loc[100:200]
# print(col1)

""" 
col1=df.loc[100:200]
print(col1)
col1=df.loc[100:200,'Player':]
print(col1)
col1=df.loc[100:200,"Run":"HS"]
print(col1) """















































# import pandas as pd 
# import matplotlib.pyplot as plt
# df=pd.read_csv("t20.csv")
# # col1=df.loc[100:]
# # print(col1)
# Mat=df.loc[:20,"Mat"].values
# print(Mat)
# Runs=df.loc[:20,"Runs"].values
# print(Runs)


# # plt.bar(player,Runs)
# # plt.pie(Runs,labels = player)
# plt.plot(Mat,Runs)
# plt.show()


# import pandas as pd
# import matplotlib.pyplot as plt

# df = pd.read_csv("ODI data.csv")
# def datashow(data):
#   print(data)

# def Graph(data):
#     plt.plot(data)
#     plt.show()

# df = pd.read_csv("ODI data.csv")
# print(df.head(0))
# while True:
#     data = df[input("enter col 1")]
#     print(data)
#     num = int(input("enter 1 for data print/n enter 2 for graph"))
#     if (num==1):
#         datashow(data)
#     elif(num==2):
#         Graph(data)
#     else:
#         break


# import pandas as pd 
# import matplotlib.pyplot as plt
# df=pd.read_csv("ODI data.csv")
# def datashow(data):
#     print(data)

# def graph(data):
#     plt.plot(data)
#     plt.show()

# df=pd.read_csv("ODI data.csv")
# print(df.head(0))
# while True:
#     data= df[input("enter col 1")]
#     print(data)
#     num=int(input("enter 1 for data print \n enter2 for graph"))
#     if(num==1):
#         datashow(data)
#     elif(num==2):
#         graph(data)
#     else:
#         break

    