## Background, Motivation, and Problem Statement

In the past two decades, the rapid development of the Internet has brought humans to the era of information explosion. The growing amount of information has led to the problem of information overload. People may feel stressed when receiving too much information on the internet. In online shopping, the user experience of customers may be affected negatively due to information overload, which potentially influences their purchase intention. As a result, a recommender system is proposed as a solution to tackle this problem.

Traditional recommender systems can be categorized into content-based filtering and user-based/item-based collaborative filtering. They were used for a long time in the industry but still face some problems, such as the cold start problem and the overspecialization problem. Most importantly, they didn't take the user's implicit feedback, such as user reviews, into consideration.

## Project Objective

This project aims to combine the content-based filtering and the item-to-item collaborative filtering as a hybrid approach to compensate for their drawbacks to each other so that the over-specialization problem and the cold start problem can be eased. Considering the lack of user implicit feedback in the traditional recommender systems, sentiment analysis for user reviews on products will be considered as one of the factors.

## Data Gathering

The [Amazon Review Dataset ](https://nijianmo.github.io/amazon/index.html) will be used for model training. The dataset is a collection of product reviews and metadata, which contains information on millions of products across various categories, including electronics, books, and clothing. In this project, the electronics dataset is selected in which the product with categories cameras, desktops, headphones, laptops, monitors, smartwatches, and tablets will be chosen.

## Built With

- scikit-learn
- surprise
- nltk
- flask
- pandas
- numpy
- matplotlib
- seaborn

## Installion Guide

#### 1. Clone the repository

    git clone https://github.com/imsamleung/personalized-product-recommendation-system.git

#### 2. Install dependencies

    pip install -r requirements.txt

#### 3. Start the server

    python app.py

## API Endpoints

| Method | URL                                                                        | Description                                                              |
| ------ | -------------------------------------------------------------------------- | ------------------------------------------------------------------------ |
| `GET`  | `/login/{user_id}`                                                         | Login to the system.                                                     |
| `GET`  | `/logout`                                                                  | Logout the current user.                                                 |
| `GET`  | `/users?offset=0&limit=100`                                                | Get all users.                                                           |
| `GET`  | `/users/{user_id}`                                                         | Get a specific user.                                                     |
| `GET`  | `/users/{user_id}/reviews?offset=0&limit=100`                              | Get all reviews of a user.                                               |
| `GET`  | `/products?offset=0&limit=100`                                             | Get all products.                                                        |
| `GET`  | `/products/{product_id}`                                                   | Get a specific product.                                                  |
| `GET`  | `/products/{product_id}/reviews?offset=0&limit=100`                        | Get all reviews of a product.                                            |
| `GET`  | `/products/{product_id}/recommend/proposed?n=10`                           | Get top n recommended products using proposed solution.                  |
| `GET`  | `/products/{product_id}/recommend/content-based-filtering?n=10`            | Get top n recommended products using content-based filtering.            |
| `GET`  | `/products/{product_id}/recommend/item-based-collaborative-filtering?n=10` | Get top n recommended products using item-based-collaborative-filtering. |
