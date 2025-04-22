import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns

# Simulate Superstore data
data = {
    "Order Date": pd.date_range(start="2022-01-01", periods=100, freq='D'),
    "Region": ["East", "West", "Central", "South"] * 25,
    "Category": ["Furniture", "Office Supplies", "Technology"] * 33 + ["Furniture"],
    "Sub-Category": ["Chairs", "Storage", "Phones", "Binders", "Accessories"] * 20,
    "Sales": np.random.uniform(50, 1000, 100),
    "Profit": np.random.uniform(-100, 300, 100),
    "State": ["California", "Texas", "New York", "Florida"] * 25
}

df = pd.DataFrame(data)
df["Month"] = df["Order Date"].dt.to_period("M").astype(str)

# Set up the plotting style
sns.set(style="whitegrid")
plt.figure(figsize=(18, 20))

# Plot 1: Monthly Sales Trend
plt.subplot(3, 2, 1)
monthly_sales = df.groupby("Month")["Sales"].sum().reset_index()
sns.lineplot(data=monthly_sales, x="Month", y="Sales", marker='o')
plt.title("Monthly Sales Trend")
plt.xticks(rotation=45)

# Plot 2: Sales and Profit by Region
plt.subplot(3, 2, 2)
region_metrics = df.groupby("Region")[["Sales", "Profit"]].sum().reset_index()
region_metrics = pd.melt(region_metrics, id_vars="Region", value_vars=["Sales", "Profit"])
sns.barplot(data=region_metrics, x="Region", y="value", hue="variable")
plt.title("Sales and Profit by Region")

# Plot 3: Sales by Category
plt.subplot(3, 2, 3)
category_sales = df.groupby("Category")["Sales"].sum().reset_index()
sns.barplot(data=category_sales, x="Category", y="Sales", palette="Set2")
plt.title("Total Sales by Category")

# Plot 4: Profitability by Sub-Category
plt.subplot(3, 2, 4)
subcat_profit = df.groupby("Sub-Category")["Profit"].sum().reset_index().sort_values(by="Profit", ascending=False)
sns.barplot(data=subcat_profit, x="Profit", y="Sub-Category", palette="coolwarm")
plt.title("Profit by Sub-Category")

# Plot 5: Sales by State
plt.subplot(3, 2, 5)
state_sales = df.groupby("State")["Sales"].sum().reset_index().sort_values(by="Sales", ascending=False)
sns.barplot(data=state_sales, x="Sales", y="State", palette="Blues_d")
plt.title("Sales by State")

# Save dashboard
plt.tight_layout()
plt.savefig("superstore_dashboard.png")
