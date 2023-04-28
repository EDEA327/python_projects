import pandas as pd
#
# # get data in columns
# data = pd.read_csv("weather_data.csv")
# # data_dict = data.to_dict()
# # temp_list = data['temp'].to_list()
# # avg = data["temp"].mean()
# max_value = data["temp"].max()
# # print(temp_list, avg, max_value)
# # print(data_dict)
#
# # get data in rows
# # print(data[data.temp == max_value])
# monday = data[data.day == "Monday"]
# print((monday.temp * 1.8) + 32)

# Create a dataframe from scratch
# data_dict = {
#     "students": ["Jose", "Mar", "Aroldo"],
#     "scores": [76, 89, 99]
# }
# data = pd.DataFrame(data_dict)
# data.to_csv("student_data.csv")

# data = pd.read_csv("2018_Central_Park_Squirrel_Census_-_Squirrel_Data.csv")
# primary_color = data["Primary Fur Color"]
# gray = len(data[primary_color == "Gray"])
# cinnamon = len(data[primary_color == "Cinnamon"])
# black = len(data[primary_color == "Black"])
#
# data_dict = {
#     "Fur Color": ["Gray", "Cinnamon", "Black"],
#     "Count": [gray, cinnamon, black]
# }
#
# df = pd.DataFrame(data_dict)
# df.to_csv("squirrel_count.csv")




