
# Sentiment Analysis and Hawkes Process Analysis

## Overview

This project is divided into two main parts: Sentiment Analysis and Hawkes Process Analysis. Both analyses aim to extract meaningful insights from a dataset containing text data, sentiment labels, timestamps, and retweet counts.

### Sentiment Analysis

The goal of the Sentiment Analysis is to classify the sentiment of the text data into different categories (e.g., positive, negative, neutral). Here's a breakdown of what the process entails:

1. **Data Preprocessing**: 
   - The text data is first cleaned and tokenized to make it suitable for machine learning models.
   - A TF-IDF vectorizer is used to convert the text data into numerical features that can be fed into a machine learning model.

2. **Model Training**:
   - A Naive Bayes classifier is trained on the TF-IDF features extracted from the text data. This model is particularly effective for text classification tasks.

3. **Evaluation**:
   - The trained model is evaluated on a test set, and performance metrics such as precision, recall, F1-score, and a confusion matrix are generated to assess the accuracy of the sentiment predictions.

### Hawkes Process Analysis

The Hawkes Process is a powerful statistical tool used to model events that occur over time. In this project, the Hawkes Process is applied to analyze the retweet activity over time based on the timestamps and retweet counts.

1. **Data Preparation**:
   - The timestamps are first converted into a numerical format that represents the time in seconds since the epoch.
   - The retweet counts are treated as events occurring at the corresponding timestamps.

2. **Modeling with Hawkes Process**:
   - The Hawkes Process is modeled using a Sum of Exponential Kernels (`HawkesSumExpKern`). This approach allows the model to capture complex dynamics where past events can influence future events over multiple timescales.
   - Multiple decay parameters are used in the model, each representing different timescales of influence. For instance, a smaller decay parameter might capture short-term excitement (e.g., a burst of retweets immediately after a tweet is posted), while a larger decay parameter might capture long-term influence (e.g., sustained retweet activity).

3. **Visualization**:
   - The kernels estimated by the model are visualized to show how the retweet activity evolves over time and how past events influence future retweets.
   - The norms of the kernels are also analyzed to understand the overall intensity of the retweet activity.

## Conclusion

By combining Sentiment Analysis with Hawkes Process modeling, this project provides a comprehensive understanding of both the sentiment trends in the text data and the temporal dynamics of retweet activity. The Sentiment Analysis offers insights into how the public feels about certain topics, while the Hawkes Process analysis reveals the temporal patterns and self-exciting nature of the retweet activity.
