import pandas as pd 
import numpy as np 
import seaborn as sb
import matplotlib.pyplot as plt

data = pd.read_csv("/Users/umayyentur/Downloads/netflix_titles.csv")
data.info()
data.head()

data['date_added'] = data['date_added'].str.strip()
data['date_added'] = pd.to_datetime(data['date_added'], format='%B %d, %Y')


TV_show = []
movies = []
for i in range(1, 13):
    monthly_data = data[data["date_added"].dt.month == i]
    a = monthly_data[monthly_data["type"] == "Movie"].shape[0]
    b = monthly_data[monthly_data["type"] == "TV Show"].shape[0]

    movies.append(a)
    TV_show.append(b)


plt.rcParams['axes.facecolor'] = 'white'
plt.rcParams['grid.color'] = 'gray'
plt.rcParams['grid.linestyle'] = ':'
plt.plot(range(1,13),TV_show, color = "red")
plt.plot(range(1,13),movies, color = "gray")
plt.title('Distribution of movies and TV shows by month', fontname='Arial', fontsize=15, fontweight='bold')
plt.xlabel("Month")
plt.ylabel("Count")
plt.show()


us = data.country.value_counts()["United States"]
others = data.country.value_counts()[1:]
a = data.country.value_counts().head(10)

fig, ((ax1, ax2), (ax3, ax4)) = plt.subplots(2, 2, figsize=(12, 10))

labels = ['United States', 'Others']
sizes = [us, others.sum()]
text = f'Total countries: {len(data.country.unique())}'

# Pie chart - Distribution of Countries
ax1.pie(sizes, labels=labels, autopct='%1.1f%%', explode=(0, 0.1), colors=["red", "darkblue"], startangle=90, textprops={'color': 'white', 'fontsize': 12, 'fontweight': 'bold'})
ax1.set_title('Distribution of Countries', fontsize=16, fontweight='bold')

# Bar chart - Number of Titles by Country
ax2.barh(a.index, a.values, color="red")
ax2.set_title('Number of Titles by Country', fontsize=15, fontweight='bold')

# The top 10 countries with the most liked shows
top_countries = data.country.value_counts().index[:10]

listed_in_counts = []
for country in top_countries:
    temp = data["listed_in"][data.country == country].value_counts()
    listed_in_counts.append(temp)

top_list_in = [temp.index[0] for temp in listed_in_counts]

# Bar chart - Top Categories by Country
ax3.barh(top_list_in, [temp.values[0] for temp in listed_in_counts], color="red")
ax3.set_title('Top Categories by Country', fontsize=15, fontweight='bold')

# Pie chart - Distribution of Titles
labels = ["Movies", "TV Show"]
sizes = data["type"].value_counts()

ax4.pie(sizes, labels=labels, colors=["darkblue", "red"], autopct="%1.1f%%", startangle=90, textprops={'color': 'white', 'fontsize': 12, 'fontweight': 'bold'},explode=(0, 0.1))
ax4.set_title('Distribution of Titles', fontsize=15, fontweight='bold')

plt.tight_layout()
plt.show()


#Most film directors 

c = data.director.value_counts().head(10)

plt.barh(c.index, c.values, color="#A1CCD1")
plt.title("Directors who made the most films", fontsize=15, fontweight="bold")
plt.xlabel("Film Count")
plt.ylabel("Director")
plt.xticks([10, 12, 14,16,18,19])
plt.show()



