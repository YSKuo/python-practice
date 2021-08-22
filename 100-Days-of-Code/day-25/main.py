# with open("weather_data.csv") as file:
#   data = file.readlines()

# import csv

# with open("weather_data.csv") as file:
#   data = csv.reader(file)
#   temperature = []
#   for row in data:
#     try:
#       temperature.append(int(row[1]))
#     except:
#       pass

# print(temperature)

import pandas
# import statistics

data = pandas.read_csv("weather_data.csv")

# print(data["temp"])

data_dict = data.to_dict()
# print(data_dict)

temp_list = data["temp"].to_list()
# print(temp_list)

# temp_average_statistics = statistics.mean(temp_list)
# print(temp_average_statistics)
# temp_average_sum = sum(temp_list) / len(temp_list)
# print(temp_average_sum)

# print(data["temp"].mean())
# print(data["temp"].max())

# # Get Data in Col
# print(data["condition"])
# print(data.condition)

# Get Data in Row
# print(data[data.day == "Monday"])
# print(data[data.temp == data.temp.max()])

# def convertCtoF(C):
#   return C * 9 / 5 + 32

# monday = data[data.day == "Monday"]
# monday_temp = int(monday.temp)
# print(convertCtoF(monday_temp))

# Create a dataframe from scratch
data_dict = {
    "students": ["Amy", "Ben", "Ciri"],
    "score": [76, 15, 82]
}
new_data = pandas.DataFrame(data_dict)
new_data.to_csv("new_data.csv")
