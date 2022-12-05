# Sentimental Analysis

Author:  Alexandra Pfleegor, Charles Mcmanus, Jaleel Cole, Nigel Itchon, Rosie Gianan, Kellimarie Cooper 

Build With: Python, Pandas,  NLP, PySpark, Machine Learning, scikit-learn, jupyter notebook

# Description

Learning is the foundation of humanity. The ability to problem solve and learn from past mistakes has allowed humans to survive for this long. But what if computers could learn and problem solve as well. While society is not quite at the apocalypse at the hands of Skynet nor is Arnold Schwarzenegger telling us come with him if we want to live, there are many examples of machines learning. Through the use of algorithms to build a model or method based on sample data, machine learning is broadly defined as a machine's capability to imitate intelligent human behavior. Speech and text are a result of the evolution of humanity needing to communicate with each other. In addition, emotions add another layer of complexity to human behavior. With this in mind, could a machine be trained to detect sentiment? Natural language processing (NLP) is a branch of artificial intelligence that attempts to give computers the ability to understand human speech and text. In particular, sentimental analysis attempts to extract subjective qualities, such emotion and attitudes, from text. 

The purpose of this project is to create a machine learning model that is able to parse through text and predict a sentimental label. Using a [Twitter dataset](https://www.kaggle.com/datasets/yasserh/twitter-tweets-sentiment-dataset) containing user tweets that have been labeled either positive, negative or neutral, the team experiments with three models: logistic regression, random forests and Naive Bayes. Furthermore the team tries two ensemble methods: adapative boost and extra trees. The models were chosen for their text-related classification. After data preprocessing and term frequency–inverse document frequency (TF-IDF), the team trains and evaulates each model. On the surface, random trees and extra trees returns the best test accuracy score, while Naive Bayes returns the least accurate score. The Naive Bayes algorithm makes more assumptions than the other models, such as independence assumption and relative frequencies, which may be why the model underpeforms compared to the others. Next, the team removes neutral tweets from the dataset and retrains. Each model performs better than the first iteration.

Produce slightly underwhelming results, the team decides to explore other NLP learning techniques. Bidirectional encoder representations from transformers (BERT) is based on transformers, a deep learning model where output elements are connected to input elements and their weights are calculated based on their connection. BERT reads in both directions at once.


## Objective:

Analyze Tweets data using machine learning models. 


## Solution:





