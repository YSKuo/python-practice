import pandas

data = pandas.read_csv("2018_Central_Park_Squirrel_Census_-_Squirrel_Data.csv")

count = {
    "Gray": 0,
    "Cinnamon": 0,
    "Black": 0
}

list_fur_color = data["Primary Fur Color"].to_list()

for color in list_fur_color:
    try:
        count[color] += 1
    except:
        pass

# print(count)
turn_csv = {
    "Fur Color": [],
    "Count": []
}

for key in count:
    turn_csv["Fur Color"].append(key)
    turn_csv["Count"].append(count[key])


new_data = pandas.DataFrame(turn_csv)
new_data.to_csv("squirrel_count.csv")
