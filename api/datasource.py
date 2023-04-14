import pandas as pd

from pathlib import Path

root_dir = Path(__file__).parent.parent


def read_json(path):
    return pd.read_json(path, orient="records", compression="gzip")


df_users = read_json(f"{root_dir}/data/interim/final/users.json.gz")
df_products = read_json(f"{root_dir}/data/interim/final/products.json.gz")
df_reviews = read_json(f"{root_dir}/data/interim/final/reviews.json.gz")
df_processed_reviews = read_json(f"{root_dir}/data/processed/reviews.json.gz")
df_reviews["processed_review_text"] = df_processed_reviews["cleaned_review"]


def get_users():
    return df_users.copy()


def get_products():
    return df_products.copy()


def get_reviews():
    return df_reviews.copy()
