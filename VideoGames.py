import pandas as pd
import matplotlib.pyplot as plt

games = pd.read_csv('vgsales.csv') # Load the CSV file into a DataFrame.

# 1- The total global sales per year
games['Year'] = pd.to_numeric(games['Year'], errors='coerce')
games = games.dropna(subset=['Year'])
games['Year'] = games['Year'].astype(int)
total_global_sales_per_year = games.groupby('Year')['Global_Sales'].sum()

plt.bar(total_global_sales_per_year.index,total_global_sales_per_year.values)
plt.title('Total Global Sales Per Year')
plt.xlabel('Year')
plt.ylabel('Total global sales'.capitalize())
plt.grid(True, linestyle='--', alpha=0.5)
plt.show(block = False)

# 2-Showing how the number of games released has changed year by year.
number_of_games_released = games.groupby('Year')['Name'].count()
max_year = number_of_games_released.idxmax()
max_value = number_of_games_released.max()

plt.figure(figsize=(8, 8))
plt.plot(number_of_games_released.index,number_of_games_released.values)
plt.title('number of games released has changed year by year'.capitalize())
plt.xlabel('Year')
plt.ylabel('Number of games')
plt.grid(True)  
plt.annotate(f'Peak: {max_value}', xy=(max_year, max_value), xytext=(max_year, max_value + 50),arrowprops=dict(facecolor='black', arrowstyle='->'), fontsize=9)
plt.xticks(rotation=45)  
plt.tight_layout()  
plt.show(block = False)

# 3-Pie chart of top 10 platforms by total global sales.
top_platforms = games.groupby('Platform')['Global_Sales'].sum().sort_values(ascending=False).head(10)

plt.figure(figsize=(5, 5))
plt.pie(top_platforms.values,labels=top_platforms.index,autopct='%1.1f%%')
plt.title('top 10 platforms by total global sales\n\n'.capitalize())
plt.axis('equal')
plt.tight_layout()  
plt.show(block = False)

# 4- Which genre has the highest average global sales
genre_avg_sales = games.groupby('Genre')['Global_Sales'].mean()

# highlight max global sales 
highlight_color = ['skyblue'] * len(genre_avg_sales)
max_index = genre_avg_sales.idxmax()
highlight_color[list(genre_avg_sales.index).index(max_index)] = 'steelblue'

plt.figure(figsize=(6, 6))
plt.bar(genre_avg_sales.index, genre_avg_sales.values, color=highlight_color)
plt.title('Average Global Sales by Genre')
plt.xlabel('Genre')
plt.ylabel('Average Global Sales (millions)')
plt.xticks(rotation=45)
plt.tight_layout()
plt.show(block = False)

# 5-Compare top 5 sales in NA, EU, and JP by platform 
sales_compare = games.groupby('Platform')[['NA_Sales','EU_Sales','JP_Sales']].sum().sort_values(by=['NA_Sales','EU_Sales','JP_Sales'],ascending=False).head(5)

sales_compare.plot(kind='bar', figsize=(10, 6))
plt.title('Regional Sales by Platform')
plt.xlabel('Platform')
plt.ylabel('Sales (millions)')
plt.xticks(rotation=0)
plt.legend(title='Region')
plt.tight_layout()
plt.show()