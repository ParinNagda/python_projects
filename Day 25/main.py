import pandas
data = pandas.read_csv("weather_data.csv")
data_dict = data.to_dict()
temp_list = data["temp"].mean()
# print(data_dict)
# print(data[data.temp == data.temp.max()])

monday = data[data.day=="Monday"]
monday_temp = monday.temp[0]
# print(monday_temp * 9/5 + 32)

new_dict = {
    "students" : ["Amy", "Bruce", "James"],
    "scores" : [42,99,55]
}

data = pandas.DataFrame(new_dict)
print(data)
data.to_csv("mark.csv")



# with open("weather_data.csv") as datafile:
#     data = datafile.readlines()
#     print(data)

# import csv
# with open("weather_data.csv") as datafile:
#     data = csv.reader(datafile)
#     temperatures = []
#     for row in data:
#         if row[1] !="temp":
#             temperatures.append(row[1])
#
#     print(temperatures)
