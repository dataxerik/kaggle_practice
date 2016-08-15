import sys
import os
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

def return_sugars(country):
    return worlds_sugars[worlds_sugars.countries == country].sugars_100g

w_directory = os.getcwd()
print(w_directory)
data_path = 'world-food-facts\FoodFacts.csv'
data_path = os.path.join(w_directory, data_path)

print(data_path)
world_food_facts = pd.read_csv(data_path)
world_food_facts.countries = world_food_facts.countries.str.lower()

c


fr_sugars = return_sugars('france').append(return_sugars('en:fr'))

countries = ['FR']

sugars_1 = [fr_sugars.mean()]
print(sugars_1)
y_pos = np.arange(len(countries))

plt.bar(y_pos, sugars_1, align='center', alpha=0.5)
plt.title('Average total sugar content per 100g')
plt.xticks(y_pos, countries)
plt.ylabel('Sugar/100g')

plt.show()
