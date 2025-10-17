# -----------------------------
# 📦 Import Required Libraries
# -----------------------------
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns

# -----------------------------
# 🧩 Step 1: Generate a Sample Dataset
# -----------------------------
# Setting a random seed for reproducibility
np.random.seed(42)

# Generate random dates, categories, and sales
dates = pd.date_range(start='2023-01-01', end='2023-06-30', freq='D')
categories = ['Electronics', 'Clothing', 'Groceries', 'Home Decor', 'Sports']

# Create synthetic data
data = {
    'Date': np.random.choice(dates, 600),          # Random date for each sale
    'Category': np.random.choice(categories, 600), # Random category
    'Sales': np.random.randint(1000, 15000, 600)   # Random sales amount
}

# Create DataFrame
df = pd.DataFrame(data)

# Display first few rows
print("Sample Data:")
print(df.head())

# -----------------------------
# 🕒 Step 2: Convert Date Column
# -----------------------------
df['Date'] = pd.to_datetime(df['Date'])

# -----------------------------
# 📈 Step 3: Sales Over Time (Line Chart)
# -----------------------------
plt.style.use('seaborn-v0_8')
sns.set_palette("Set2")

sales_over_time = df.groupby('Date')['Sales'].sum().reset_index()

plt.figure(figsize=(10,5))
plt.plot(sales_over_time['Date'], sales_over_time['Sales'], color='teal', linewidth=2)
plt.title('Sales Over Time', fontsize=14)
plt.xlabel('Date')
plt.ylabel('Total Sales')
plt.grid(True, linestyle='--', alpha=0.6)
plt.tight_layout()
plt.savefig('sales_over_time.png')
plt.show()

# -----------------------------
# 🗓️ Step 4: Monthly Aggregation (Bar Chart)
# -----------------------------
df['Month'] = df['Date'].dt.to_period('M')
monthly_sales = df.groupby('Month')['Sales'].sum().reset_index()

plt.figure(figsize=(8,4))
sns.barplot(x=monthly_sales['Month'].astype(str), y=monthly_sales['Sales'], color='skyblue')
plt.title('Monthly Sales', fontsize=14)
plt.xlabel('Month')
plt.ylabel('Sales')
plt.xticks(rotation=45)
plt.tight_layout()
plt.savefig('monthly_sales.png')
plt.show()

# -----------------------------
# 🛍️ Step 5: Category Comparison (Bar Chart)
# -----------------------------
category_sales = df.groupby('Category')['Sales'].sum().sort_values(ascending=False).reset_index()

plt.figure(figsize=(8,4))
sns.barplot(x='Category', y='Sales', data=category_sales)
plt.title('Sales by Category', fontsize=14)
plt.xlabel('Category')
plt.ylabel('Total Sales')
plt.tight_layout()
plt.savefig('category_comparison.png')
plt.show()

# -----------------------------
# 🥧 Step 6: Category Share (Pie Chart)
# -----------------------------
plt.figure(figsize=(6,6))
plt.pie(category_sales['Sales'], labels=category_sales['Category'],
        autopct='%1.1f%%', startangle=90, textprops={'fontsize': 10})
plt.title('Category Sales Share', fontsize=14)
plt.tight_layout()
plt.savefig('category_share.png')
plt.show()

# -----------------------------
# 🧾 Step 7: Summary Report
# -----------------------------
summary = """
Sales Analysis Summary:
------------------------
1. The 'Sales Over Time' line chart shows sales patterns across days, helping identify high-performing periods.
2. The 'Monthly Sales' bar chart reveals how performance varies month to month.
3. The 'Category Comparison' bar chart compares total sales across product categories.
4. The 'Category Share' pie chart highlights which category dominates the market.

Visual formatting choices:
- Titles and axis labels clearly describe each visualization.
- Legends and color schemes improve readability.
- Saved all charts as PNG files for submission.

All files generated:
- sales_over_time.png
- monthly_sales.png
- category_comparison.png
- category_share.png
"""

print(summary)

# Optional: Save the summary as a text file
with open("sales_analysis_summary.txt", "w") as f:
    f.write(summary)

print("\n✅ Task 1 Completed Successfully! Charts and summary saved in your project folder.")
