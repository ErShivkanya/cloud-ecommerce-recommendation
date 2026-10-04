import pandas as pd
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.metrics.pairwise import cosine_similarity


# Load product data
products = pd.read_csv("products.csv")


# Combine product information
products["features"] = (
    products["Category"] + " " +
    products["Description"]
)


# Convert text into numerical vectors
vectorizer = TfidfVectorizer(stop_words="english")
feature_matrix = vectorizer.fit_transform(products["features"])


# Calculate similarity between products
similarity_matrix = cosine_similarity(feature_matrix)


def recommend_products(product_name, number_of_recommendations=5):

    # Find selected product
    product_index = products[
        products["Product_Name"] == product_name
    ].index[0]

    # Get similarity scores
    similarity_scores = list(
        enumerate(similarity_matrix[product_index])
    )

    # Sort products by similarity
    similarity_scores = sorted(
        similarity_scores,
        key=lambda x: x[1],
        reverse=True
    )

    # Select top recommendations
    recommended_indices = [
        index
        for index, score in similarity_scores[1:number_of_recommendations + 1]
    ]

    return products.iloc[recommended_indices][
        ["Product_Name", "Category", "Price", "Rating"]
    ]