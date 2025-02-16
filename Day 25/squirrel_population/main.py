import pandas

data = pandas.read_csv("squirrel_data.csv")

gray_squirrel = data[data["Primary Fur Color"] == "Gray"]
cinnamon_squirrel = data[data["Primary Fur Color"] == "Cinnamon"]
black_squirrel = data[data["Primary Fur Color"] == "Black"]


data_dict = {
    "Fur Color" : ["Gray", "Cinnamon", "Black"],
    "Count" : [len(gray_squirrel), len(cinnamon_squirrel), len(black_squirrel)]
}

df = pandas.DataFrame(data_dict)
df.to_csv("squirrel_count.csv")