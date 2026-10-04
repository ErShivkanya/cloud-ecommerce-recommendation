import streamlit as st
import pandas as pd
from recommender import products, recommend_products

st.set_page_config(
    page_title="SmartShop AI",
    page_icon="🛒",
    layout="wide"
)

st.title("🛒 SmartShop AI")
st.subheader("Cloud-Based E-Commerce Recommendation System")

st.write(
    "Discover products recommended especially for your interests!"
)

st.divider()

product_list = products["Product_Name"].tolist()

selected_product = st.selectbox(
    "🔍 Select a product you like:",
    product_list
)

number = st.slider(
    "Number of recommendations",
    min_value=1,
    max_value=5,
    value=3
)

if st.button("🤖 Recommend Products"):
    recommendations = recommend_products(
        selected_product,
        number
    )

    st.success(f"Recommendations for {selected_product}")

    cols = st.columns(len(recommendations))

    for col, (_, product) in zip(
        cols, recommendations.iterrows()
    ):
        with col:
            st.markdown(f"### 🛍️ {product['Product_Name']}")
            st.write(f"Category: {product['Category']}")
            st.write(f"Price: ₹{product['Price']}")
            st.write(f"Rating: ⭐ {product['Rating']}")

st.divider()
st.caption("SmartShop AI | Powered by Machine Learning")