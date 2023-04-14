from sklearn.preprocessing import MinMaxScaler
import pickle
import pandas as pd

from api.repositories import product_repository, review_repository

from pathlib import Path

root_dir = Path(__file__).parent.parent.parent

df_products = product_repository.find_all()
df_reviews = review_repository.find_all()


# Get unrated items for a user
def get_user_unrated_items(user_id, df_products, df_reviews):
    df_user_reviews = df_reviews[df_reviews["user_id"] == user_id]
    return df_products[~df_products["product_id"].isin(df_user_reviews["product_id"])]


CBF_item_similarity_matrix = pickle.load(
    open(
        f"{root_dir}/models/final/content_based_filtering/item_similarity_matrix.pkl",
        "rb",
    )
)


def CBF_find_similar_items(product_id, df_products):
    idx = df_products[df_products["product_id"] == product_id].index[0]
    sorted_scores = pd.Series(CBF_item_similarity_matrix[idx]).sort_values(
        ascending=False
    )
    return df_products.iloc[list(sorted_scores.iloc[1:].index)]


def content_based_filtering(user_id, product_id, n=10):
    df_similar_items = CBF_find_similar_items(product_id, df_products)
    df_user_unrated_items = get_user_unrated_items(
        user_id, df_similar_items, df_reviews
    )

    if n < len(df_user_unrated_items):
        df_user_unrated_items = df_user_unrated_items[:n]

    return df_user_unrated_items


item_based_CF_knn_model = pickle.load(
    open(f"{root_dir}/models/final/item_based_collaborative_filtering/knn.pkl", "rb")
)


# Get all items that have at least 1 rating and sorted by similarity
def item_based_CF_find_similar_items(product_id, df_products):
    neighbors = item_based_CF_knn_model.get_neighbors(
        item_based_CF_knn_model.trainset.to_inner_iid(product_id),
        k=item_based_CF_knn_model.trainset.n_items,
    )
    df_1 = pd.DataFrame(
        {
            "product_id": [
                item_based_CF_knn_model.trainset.to_raw_iid(inner_id)
                for inner_id in neighbors
            ]
        }
    )
    return df_1.merge(df_products, how="inner", on="product_id")


def predict_rating(user_id, product_id):
    return item_based_CF_knn_model.predict(user_id, product_id)


def item_based_collaborative_filtering(user_id, product_id, n=10):
    df_similar_items = item_based_CF_find_similar_items(product_id, df_products)
    df_user_unrated_items = get_user_unrated_items(
        user_id, df_similar_items, df_reviews
    )

    if n < len(df_user_unrated_items):
        df_user_unrated_items = df_user_unrated_items[:n]

    df_user_unrated_items["pre"] = df_user_unrated_items["product_id"].apply(
        lambda id: predict_rating(user_id, id).est
    )
    df_user_unrated_items = df_user_unrated_items.sort_values(
        by=["pre"], ascending=False
    )
    return df_user_unrated_items


sentiment_analysis_model = pickle.load(
    open(
        f"{root_dir}/models/final/sentiment_analysis/logistic_regression_with_tfidf_vectorizer.pkl",
        "rb",
    )
)


def predict_mean_sentiment(product_id: str):
    review_list = df_reviews[df_reviews["product_id"] == product_id][
        "processed_review_text"
    ].tolist()
    if len(review_list) == 0:
        return 0
    sentiment = predict_sentiment(review_list)
    if sentiment is None:
        return 0

    return sentiment.mean()


def predict_sentiment(features: list):
    if len(features) == 0:
        return
    return sentiment_analysis_model.predict(features)


def recommend(user_id, product_id, n=10):
    # Get top n items using item_based_collaborative_filtering
    df_item_based_CF_items = item_based_collaborative_filtering(user_id, product_id, n)

    # Calculate the mean sentiment for each product
    df_item_based_CF_items["sen"] = df_item_based_CF_items["product_id"].apply(
        predict_mean_sentiment
    )

    # Scale the sentiment score to fit the rating [formula: (x - xmin) / (xmax - xmin)] for each product
    scaler = MinMaxScaler(feature_range=(1, 5))
    scaler.fit(df_item_based_CF_items[["sen"]])
    df_item_based_CF_items["sen"] = scaler.transform(df_item_based_CF_items[["sen"]])

    # Calculate the ranking score for each product
    w1 = 1
    w2 = 2
    df_item_based_CF_items["ranking_score"] = (
        w1 * df_item_based_CF_items["pre"] + w2 * df_item_based_CF_items["sen"]
    )

    # filter out low ranking score products
    threshold = (w1 * 5 + w2 * 5) / 2.0
    df_item_based_CF_items = df_item_based_CF_items[
        df_item_based_CF_items["ranking_score"] >= threshold
    ]

    # Sort by ranking score
    df_item_based_CF_items = df_item_based_CF_items.sort_values(
        by=["ranking_score"], ascending=False
    )

    df_final_items = df_item_based_CF_items

    # Handle the cold-start problem
    # Also, complement the filtered products by content_based_filtering
    com = n - len(df_item_based_CF_items)
    if com > 0:
        df_CBF_items = content_based_filtering(user_id, product_id, len(df_products))
        df_CBF_items = df_CBF_items[
            ~df_CBF_items["product_id"].isin(df_item_based_CF_items["product_id"])
        ]
        df_final_items = pd.concat([df_final_items, df_CBF_items[:com]])

    return df_final_items
