import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt
import geopandas as gpd


st.title("Silver Price Calculator & Silver Sales Analysis")

silver_sales = pd.read_csv("state_wise_silver_purchased_kg.csv")
silver_price = pd.read_csv("historical_silver_price.csv")


st.header("1. Silver Price Calculator")

weight = st.number_input("Enter weight of silver", min_value=0.0)
unit = st.selectbox("Select unit", ["Grams", "Kilograms"])
price_per_gram = st.number_input("Current silver price per gram (INR)", min_value=0.0)


if unit == "Kilograms":
    weight = weight * 1000

total_cost_inr = weight * price_per_gram
st.success(f"Total Cost (INR): ₹ {total_cost_inr:.2f}")


currency = st.selectbox("Convert currency", ["INR", "USD"])
usd_rate = 83  # approx rate

if currency == "USD":
    st.info(f"Total Cost (USD): $ {total_cost_inr / usd_rate:.2f}")


st.subheader("Historical Silver Price Chart")

price_filter = st.selectbox(
    "Filter by price range (INR per kg)",
    ["≤ 20000", "20000 - 30000", "≥ 30000"]
)

if price_filter == "≤ 20000":
    filtered_price = silver_price[silver_price["Silver_Price_INR_per_kg"] <= 20000]
elif price_filter == "20000 - 30000":
    filtered_price = silver_price[
        (silver_price["Silver_Price_INR_per_kg"] > 20000) &
        (silver_price["Silver_Price_INR_per_kg"] < 30000)
    ]
else:
    filtered_price = silver_price[silver_price["Silver_Price_INR_per_kg"] >= 30000]

fig, ax = plt.subplots()
ax.plot(filtered_price["Year"], filtered_price["Silver_Price_INR_per_kg"])
ax.set_xlabel("Year")
ax.set_ylabel("Price (INR per kg)")
ax.set_title("Historical Silver Prices")
st.pyplot(fig)

#Silver Sales Dashboard 
india_states  = gpd.read_file("india.shp")


merged = india_states.merge(
    silver_sales,
    left_on="st_nm",
    right_on="State"
)

fig, ax = plt.subplots(figsize=(10, 10))
merged.plot(
    column="Silver_Purchased_kg",
    cmap="Greys",
    legend=True,
    ax=ax
)
ax.set_title("India State-wise Silver Purchases (kg)")
ax.axis("off")
st.pyplot(fig)


st.subheader("Top 5 States with Highest Silver Purchases")

top5 = silver_sales.sort_values(
    by="Silver_Purchased_kg",
    ascending=False
).head(5)

fig, ax = plt.subplots()
ax.bar(top5["State"], top5["Silver_Purchased_kg"])
ax.set_xlabel("State")
ax.set_ylabel("Silver Purchased (kg)")
ax.set_title("Top 5 Silver Consuming States")
st.pyplot(fig)


st.subheader("January Monthly Silver Sales Analysis")

jan_sales = silver_sales[silver_sales["Month"] == "Jan"]

st.dataframe(jan_sales)

fig, ax = plt.subplots()
ax.plot(jan_sales["State"], jan_sales["Silver_Purchased_kg"], marker='o')
ax.set_xlabel("State")
ax.set_ylabel("Silver Purchased (kg)")
ax.set_title("January Monthly Silver Sales Trend")
plt.xticks(rotation=90)
st.pyplot(fig)

