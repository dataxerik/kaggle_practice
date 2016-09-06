import sys
import os
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

def return_sugars(country):
    return worlds_sugars[worlds_sugars.countries == country].sugars_100g

w_directory = os.getcwd()
print(w_directory)
data_path = "C:\\Users\\dsharp\\PycharmProjects\\kaggle_practice\\data\\world-food-facts\\FoodFacts.csv"
data_path = os.path.join(w_directory, data_path)
data_path = "C:\\Users\\dsharp\\PycharmProjects\\kaggle_practice\\data\\world-food-facts\\FoodFacts.csv"

print(data_path)
world_food_facts = pd.read_csv(data_path)
world_food_facts.countries = world_food_facts.countries.str.lower()

data_directory = os.getcwd()
data_path = 'data\world-food-facts\FoodFacts.csv'
data_path = os.path.join(data_directory, data_path)

if os.path.exists(data_path):
    world_food_facts = pd.read_csv(data_path)
    world_food_facts.countries = world_food_facts.countries.str.lower()
    print("Data loaded. There are {} rows".format(world_food_facts.shape[0]))
else:
    print("Error: source data location: {} does not exist".format(data_path))

worlds_sugars = world_food_facts[world_food_facts.sugars_100g.notnull()]
worlds_sugars = world_food_facts[world_food_facts.countries_tags.notnull()]

world = world_food_facts[pd.notnull(world_food_facts.countries_tags)]

tag_index = world.columns.get_loc('countries_tags')

country = 'france'

country_tags = []
for index, item in world.iterrows():
    if len(item[tag_index].split(",")) > 1:
        for country in (item[tag_index].split(",")):
            if ":" in country and country.split(":")[1] not in country_tags:
                country_tags.append(country.split(":")[1])
    else:
        if ":" in country and country.split(":")[1] not in country_tags:
            country_tags.append(country.split(":")[1])

print(country_tags)

country = 'france'

for index, row in worlds_sugars.head().iterrows():
    if country in row[tag_index]:
        print(row[tag_index])

[row[tag_index] for index, row in worlds_sugars.iterrows() if country in row[tag_index]]
'''
#fr_sugars = return_sugars('france').append(return_sugars('en:fr'))

countries = ['FR']

sugars_1 = [fr_sugars.mean()]
print(sugars_1)
y_pos = np.arange(len(countries))

plt.bar(y_pos, sugars_1, align='center', alpha=0.5)
plt.title('Average total sugar content per 100g')
plt.xticks(y_pos, countries)
plt.ylabel('Sugar/100g')

plt.show()
'''