import collections
import psycopg2
from bs4 import BeautifulSoup


# Data set
with open("website.html") as file:
    contents = file.read()

soup = BeautifulSoup(contents, "html.parser")

color_elements = soup.select("td")

colors = [color.get_text().replace('MONDAY', '').replace('TUESDAY', '').replace('WEDNESDAY', '').replace('THURSDAY',
                                                                                                         '').replace(
    'FRIDAY', '').replace(',', '').split() for color in color_elements]

colors_flat = [item.lower() for sublist in colors for item in sublist]

#                       Task 1: Mean color
mean_color = collections.Counter(colors_flat).most_common(1)[0][0]


#                       Task 2: Mode (most common color)
mode_color = collections.Counter(colors_flat).most_common(1)[0][0]


#                       Task 3: Median color
sorted_colors = sorted(colors_flat)
n = len(sorted_colors)
median_color = sorted_colors[n // 2] if n % 2 != 0 else (sorted_colors[(n - 1) // 2] + sorted_colors[(n + 1) // 2]) / 2


#                       Task 4: Variance of colors
counter = collections.Counter(colors_flat)
for color, frequency in counter.items():
    print(f"{color}: {frequency}")


#                       Task 5: Probability of choosing red color at random
probability_red = counter['red'] / len(colors_flat)


#                       Task 6: Save colors and frequencies to PostgreSQL database
db_params = {
    'host': 'localhost',
    'database': 'postgres',
    'user': 'postgres',
    'password': 'Boluwatito'
}

conn = psycopg2.connect(**db_params)
cursor = conn.cursor()

# Create a table to store color frequencies
cursor.execute("CREATE TABLE IF NOT EXISTS color_frequencies (color VARCHAR(50), frequency INT);")

# Calculate frequencies and insert into the database
for color, frequency in counter.items():
    cursor.execute("INSERT INTO color_frequencies (color, frequency) VALUES (%s, %s);", (color, frequency))


cursor.execute("SELECT * FROM color_frequencies;")


rows = cursor.fetchall()

# Print the result
for row in rows:
    print(row)
# Commit the changes and close the connection
conn.commit()
cursor.close()
conn.close()

# Print results
print(f"Mean Color: {mean_color}")
print(f"Most Worn Color: {mode_color}")
print(f"Median Color: {median_color}")
print(f"Probability of Choosing Red Color: {probability_red}")
print("Colors and Frequencies saved to PostgreSQL database.")






