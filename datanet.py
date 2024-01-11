# import requests
# print(requests)

# r=requests.get('http://ankursingh.xyz/api/productshow.php')
# print(type(r))
# print(r)
# l=[]

# for i in r.json().values():
    
#     print(i)




# import pandas as pd 
# df= pd.read_csv('Salary_Data.csv')
# print(df)
# print(df.head (0).values)


# import pandas as pd
# import matplotlib.pyplot as plt

# df = pd.read_csv("Salary_Data.csv")
# def datashow(data):
#   print(data)

# def Graph(data):
#     plt.plot(data)
#     plt.show()

# df = pd.read_csv("Salary_Data.csv")
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





import csv
from ctypes import _NamedFuncPointer

def get_player_details(csv_file, player_name):
    with open(csv_file, 'r') as file:
        reader = csv.DictReader(file)
        for row in reader:
            if row['Player'] == player_name:
                return row

    return None

def main():
    csv_file_path = 'ODI data.csv'  # Replace with your actual file path
    player_name = input("Enter the player name: ")

    player_details = get_player_details(csv_file_path, player_name)

    if player_details:
        print(f"Details for {player_name}:")
        for key, value in player_details.items():
            print(f"{key}: {value}")
    else:
        print(f"Player '{player_name}' not found in the CSV file.")

if __name__== "_main_":
    main()