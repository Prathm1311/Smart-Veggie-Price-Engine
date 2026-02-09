import random
import pandas as pd

vegetables = ["Tomato", "Onion", "Potato", "Cauliflower", "Carrot"]
seasons = ["Summer", "Winter", "Monsoon"]
demand_levels = ["Low", "Medium", "High"]

def generate_price_change(demand, season):
    if demand == "High":
        base = random.randint(20, 80)
    elif demand == "Medium":
        base = random.randint(-10, 30)
    else:  # Low
        base = random.randint(-50, 10)

    # seasonal adjustment
    if season == "Summer":
        base += random.randint(5, 15)
    elif season == "Winter":
        base -= random.randint(5, 15)
    else:  # Monsoon
        base += random.randint(-20, 20)

    return max(-60, min(90, base))  # clamp values

data = []

for _ in range(1000):
    veg = random.choice(vegetables)
    season = random.choice(seasons)

    # logical demand-season relationship
    if season == "Summer":
        demand = random.choices(demand_levels, weights=[20, 30, 50])[0]
    elif season == "Winter":
        demand = random.choices(demand_levels, weights=[40, 40, 20])[0]
    else:  # Monsoon
        demand = random.choices(demand_levels, weights=[25, 35, 40])[0]

    price_change = generate_price_change(demand, season)

    data.append([veg, season, demand, price_change])

df = pd.DataFrame(data, columns=[
    "vegetable", "season", "demand_level", "price_change_percent"
])

df.to_csv("vegetable_price_training_data.csv", index=False)

print("✅ 1000-row dataset generated successfully!")
