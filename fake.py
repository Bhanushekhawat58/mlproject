# # import csv

# # def get_player_details(csv_file, player_name):
# #     with open(csv_file, 'r') as file:
# #         reader = csv.DictReader(file)
# #         for row in reader:
# #             if row['Player'] == player_name:
# #                 return row

# #     return None

# # def main():
# #     csv_file_path = 'ODI data.csv'  # Replace with your actual file path
# #     player_name = input("Enter the player name: ")

# #     player_details = get_player_details(csv_file_path, player_name)

# #     if player_details:
# #         print(f"Details for {player_name}:")
# #         for key, value in player_details.items():
# #             print(f"{key}: {value}")
# #     else:
# #         print(f"Player '{player_name}' not found in the CSV file.")

# # if __name__ == "_main_":
# #     main()
    
    
    
    
    
    
# # import pandas as pd
# # df = pd.read_csv('ODI data.csv')
# # v=df['Player'][0]
# # print(v.split('(')[1].split(')')[0])


# # import pandas as pd
# # data = pd.read_csv("ODI data.csv")
# # print(data)

# # n1=data['player'].head[20].values
# # n2=data['Mat'].head[20].values

# # print('n1=',n1)
# # print('n2=',n2)


# # if 'RT Ponting (AUS/ICC)' in n1:
# #     if '445' in n2:
# #         print('found')
        
# # else:
# #     print('not found')

    
    

# import pandas as pd 
# import matplotlib.pyplot as plt
# df=pd.read_csv("Salary_Data.csv")
# print(df)
# Age=df.loc[:20,"Age"].values
# print(Age)
# Salary=df.loc[:20,"Salary"].values
# print(Salary)

# plt.bar(Age,Salary)
# # plt.plot(Age,Salary)
# plt.show()





# Import the necessary modules
# import numpy as np
# import matplotlib.pyplot as plt
# from sklearn.linear_model import LinearRegression

# # Generate some random data
# rng = np.random.default_rng()
# x = rng.random(10) # Independent variable
# y = 1.6*x + rng.random(10) # Dependent variable

# # Create and fit a linear regression model
# model = LinearRegression()
# model.fit(x.reshape(-1, 1), y)

# # Print the model coefficients
# print("Intercept:", model.intercept_)
# print("Slope:", model.coef_)

# # Plot the data and the regression line
# plt.scatter(x, y, label="Data")
# plt.plot(x, model.predict(x.reshape(-1, 1)), color="red", label="Regression line")
# plt.xlabel("x")
# plt.ylabel("y")
# plt.legend()
# plt.show()






