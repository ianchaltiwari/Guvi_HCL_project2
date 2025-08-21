# sales.py
import pandas as pd
import matplotlib.pyplot as plt
from sklearn.linear_model import LinearRegression
from sklearn.metrics import r2_score
import os

# ---------------------------
# 1. Load Dataset
# ---------------------------
file_path = "stationery_sales.csv"

if not os.path.exists(file_path):
    raise FileNotFoundError(f"{file_path} not found! Make sure the CSV is in the correct folder.")

df = pd.read_csv(file_path)

print("✅ Original Data Loaded")
print(df.head())

# ---------------------------
# 2. Clean Data & Calculate Revenue
# ---------------------------
# Ensure correct column names
df.columns = df.columns.str.strip()  # remove spaces
expected_cols = ["Date", "Product", "Units", "Price"]
for col in expected_cols:
    if col not in df.columns:
        raise KeyError(f"Missing column: {col}. Found columns: {list(df.columns)}")

# Convert Date to datetime
df["Date"] = pd.to_datetime(df["Date"])

# Calculate Total Revenue
df["Total_Revenue"] = df["Units"] * df["Price"]

print("\n✅ Data after cleaning and revenue calculation")
print(df.head())

# Save cleaned dataset for Tableau
cleaned_file = "stationery_sales_clean.csv"
df.to_csv(cleaned_file, index=False)
print(f"\n💾 Cleaned dataset saved as {cleaned_file}")

# ---------------------------
# 3. Machine Learning: Linear Regression
# ---------------------------
# Convert Date to numerical index for regression
df_sorted = df.sort_values("Date")
df_sorted["Day_Index"] = (df_sorted["Date"] - df_sorted["Date"].min()).dt.days

X = df_sorted[["Day_Index"]]
y = df_sorted["Units"]

# Train Linear Regression
model = LinearRegression()
model.fit(X, y)

# Predictions
y_pred = model.predict(X)

# ---------------------------
# 4. Evaluate Model
# ---------------------------
r2 = r2_score(y, y_pred)
print(f"\n📊 Linear Regression R² Score: {r2:.4f}")
print(f"Equation: Units_Sold = {model.coef_[0]:.2f}*Day_Index + {model.intercept_:.2f}")

# ---------------------------
# 5. Plot for Quick Check
# ---------------------------
plt.figure(figsize=(8, 5))
plt.scatter(X, y, color="blue", label="Actual Sales")
plt.plot(X, y_pred, color="red", label="Regression Line")
plt.xlabel("Day Index (from start)")
plt.ylabel("Units Sold")
plt.title("Sales Trend (Linear Regression)")
plt.legend()
plt.savefig("sales_trend.png")
plt.show()

print("\n📊 ML workflow completed. Files saved: ")
print(f"- {cleaned_file} (Clean data for Tableau)")
print("- sales_trend.png (Trend visualization)")
