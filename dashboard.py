import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import streamlit as st
import seaborn as sns

# Load datasets
customers_dataset_df = pd.read_csv('customers_dataset.csv')
sellers_dataset_df = pd.read_csv('sellers_dataset.csv')
products_dataset_df = pd.read_csv('products_dataset.csv')
order_items_dataset_df = pd.read_csv('order_items_dataset.csv')

# Streamlit app setup
st.header(' :sparkles: Dicoding Project :sparkles:')
st.subheader('Sayfullah Baruna Prayoga')
st.subheader('This chart shows that most of the product that been ordered multiple times have uploaded more than 5 photos')

# Preprocessing
mean_value = products_dataset_df['product_photos_qty'].mean()
products_dataset_df['product_photos_qty'].fillna(mean_value, inplace=True)
products_dataset_df.product_category_name.fillna(value='Unknown', inplace=True)
selected_columns_df = products_dataset_df[['product_id', 'product_category_name', 'product_photos_qty']]
merged1_df = pd.merge(order_items_dataset_df[['product_id']], selected_columns_df, on='product_id', how='inner')

# Data Analysis
duplicated_products = merged1_df[merged1_df.duplicated(subset=['product_id'], keep=False)]
product_photos_avg = duplicated_products.groupby('product_id')['product_photos_qty'].mean()

# Visualization with Streamlit
st.sidebar.title("Customization (you can see the top 1 - top 50 product)")
top_n = st.sidebar.slider("Select Top N Products", min_value=1, max_value=50, value=20)

# Create Matplotlib figure and axis
fig, ax = plt.subplots(figsize=(10, 6))

top_product_ids = product_photos_avg.nlargest(top_n).index
top_avg_photos_qty = product_photos_avg.nlargest(top_n).values
ax.bar(top_product_ids, top_avg_photos_qty, color='skyblue')
ax.set_xlabel('Product ID')
ax.set_ylabel('Average Product Photos Quantity')
ax.set_title(f'Top {top_n} Product IDs: Avg. Photos Quantity')
ax.tick_params(axis='x', rotation=90)

# Pass the Matplotlib figure explicitly
st.pyplot(fig)

st.subheader('This Chart shows which state has the most customers')

# Customer Distribution by State
total_customers_by_state = customers_dataset_df.groupby('customer_state')['customer_id'].count()

# Create Matplotlib figure and axis
fig_state, ax_state = plt.subplots(figsize=(10, 6))

ax_state.bar(total_customers_by_state.index, total_customers_by_state.values, color='skyblue')
ax_state.set_xlabel('State')
ax_state.set_ylabel('Total Customers')
ax_state.set_title('Distribution of Customers by State')
ax_state.tick_params(axis='x', rotation=45)

# Pass the Matplotlib figure explicitly
st.pyplot(fig_state)

st.subheader('This Chart shows you which city has the most customers')

# Top Cities
st.sidebar.title("Customization (you can see the top 1 - top 50 city)")
total_customers_by_city = customers_dataset_df.groupby('customer_city')['customer_id'].count()
top_n_cities = st.sidebar.slider("Select Top N Cities", min_value=1, max_value=50, value=10)
top_cities = total_customers_by_city.nlargest(top_n_cities)

# Create Matplotlib figure and axis
fig_cities, ax_cities = plt.subplots(figsize=(10, 6))

ax_cities.bar(top_cities.index, top_cities.values, color='salmon')
ax_cities.set_xlabel('City')
ax_cities.set_ylabel('Total Customers')
ax_cities.set_title(f'Top {top_n_cities} Cities with the Most Customers')
ax_cities.tick_params(axis='x', rotation=90)

# Pass the Matplotlib figure explicitly
st.pyplot(fig_cities)

# Additional Streamlit content
st.write("Additional Streamlit content goes here.")
