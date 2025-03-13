# with open("weather_data.csv") as data_file:
#     data = data_file.readline()

# import csv
#
# with open("weather_data.csv") as data_file:
#     data = csv.reader(data_file)
#     temperatures = []
#     for row in data:
#         if row[1] != "temp":
#           temperatures.append(int(row[1]))
#     print(temperatures)

import pandas
#
#data = pandas.read_csv("weather_data.csv")
# data_dict = data.to_dict()
# print(data_dict)
#
# temp_list = data["temp"].to_list()
# average = sum(temp_list) / len(temp_list)
# print(average)
#
# print(data["temp"].max())
# print(data["condition"])
#
# conditions = data.condition
# print(conditions)

# print(data[data.day == "Monday"])
# print(data[data.temp == data.temp.max()])
#monday = data[data.day == "Monday"]
# print(monday.condition)

# monday_temp = monday.temp[0]
# monday_temp_F = monday_temp * 9/5 + 32
# print(monday_temp_F)
#
#
# data_dict = {
#     "students" : ["Amy", "James", "Angela"],
#     "scores" : [76, 56, 65]
# }
# data = pandas.DataFrame(data_dict)
# print(data)
# data.to_csv("new_data.csv")

data = pandas.read_csv("2018_Central_Park_Squirrel_Census_-_Squirrel_Data.csv")
# grey_squirrels = len(data[data["Primary Fur Color"] == "Gray"])
# cinnamon_squirrels= len(data[data["Primary Fur Color"] == "Cinnamon"])
# black_squirrels = len(data[data["Primary Fur Color"] == "Black"])



# print(grey_squirrels)
# print(cinnamon_squirrels)
# print(black_squirrels)

#
# data_dict = {
#     "Fur Color" : ["Gray", "Cinnamon", "Black"],
#     "Count" : [grey_squirrels, cinnamon_squirrels, black_squirrels]
#
# }
#
# df = pandas.DataFrame(data_dict)
#df.to_csv("squirrel_count.csv")
