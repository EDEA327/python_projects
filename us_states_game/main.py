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
data_dict = {
    "students": ["Jose", "Mar", "Aroldo"],
    "scores": [76, 89, 99]
}
data = pd.DataFrame(data_dict)
data.to_csv("student_data.csv")

