# Sentimental Analysis

Author:  Alexandra Pfleegor, Charles Mcmanus, Jaleel Cole, Nigel Itchon, Rosie Gianan, Kellimarie Cooper

# Description

Learning is the foundation of humanity. The ability to problem solve and learn from past mistakes has allowed humans to survive for this long. But what if computers could learn and problem solve as well. While society is not quite at the apocalypse at the hands of Skynet nor is Arnold Schwarzenegger telling us come with him if we want to live, there are many examples of machines learning. Through the use of algorithms to build a model or method based on sample data, machine learning is broadly defined as a machine's capability to imitate intelligent human behavior. Speech and text are a result of the evolution of humanity needing to communicate with each other. In addition, emotions add another layer of complexity to human behavior. With this in mind, could a machine be trained to detect sentiment? Natural language processing (NLP) is a branch of artificial intelligence that attempts to give computers the ability to understand human speech and text. In particular, sentimental analysis attempts to extract subjective qualities, such emotion and attitudes, from text. 

The purpose of this project is to create a machine learning model that is able to parse through text and predict a sentimental label. Using a [Twitter dataset](https://www.kaggle.com/datasets/yasserh/twitter-tweets-sentiment-dataset) containing user tweets that have been labeled either positive, negative or neutral, the team experiments with three models: logistic regression, random forests and Naive Bayes. Furthermore the team tries two ensemble methods: adapative boost and extra trees. The models were chosen for their text-related classification. After data preprocessing and term frequency–inverse document frequency (TF-IDF), the team trains and evaulates each model. On the surface, random trees and extra trees returns the best test accuracy score, while Naive Bayes returns the least accurate score. The Naive Bayes algorithm makes more assumptions than the other models, such as independence assumption and relative frequencies, which may be why the model underpeforms compared to the others. Next, the team removes neutral tweets from the dataset and retrains. Each model performs better than the first iteration.

Produce slightly underwhelming results, the team decides to explore other NLP learning techniques. Bidirectional encoder representations from transformers (BERT) is based on transformers, a deep learning model where output elements are connected to input elements and their weights are calculated based on their connection. BERT reads in both directions at once providing a deeper sense of language context and flow as opposed to the single-direction language models. TF-IDF does not take into account the semantic meaning or context of the words. When trained on the Twitter dataset, BERT returned accuracy scores of 80% and 93%, with and without neutral labels respectively. 

Feeling more confident in BERT, the team trains BERT on a separate [emotions dataset](https://www.kaggle.com/datasets/praveengovi/emotions-dataset-for-nlp), which contains sentences that are pre-labeled with the following emotions: anger, fear, joy, love, sadness and surprise. BERT achieved an accuracy score of 93%. With this model, the team develops a Flask app that asks for a user input to predict their current emotion.

# Repository Description

In this repository, there are three folders entitled: BERT, Notebooks, and Resources and two Jupyter notebooks in the main directory. The Resources folder contains the Twitter dataset. The Notebooks folder contains the teams individual explorations of each model. The Sentimental_Analysis notebook contains a consolidated version of all the models. The second notebook, Sentimental_Analysis_Colab, mirrors the first notebook, but trains a second Naive Bayes model using PySpark and was run with Google Colab. The BERT folder contains all the BERT training, Flask app and the requisite HTML and CSS files. 

# Tools/Modules Used
- Python
- Pandas
- scikit-learn
- Matplotlib
- nltk
- Spark
- Flask
- Pickle
- simpletransformers
- Tableau
- CSV

# Conclusions
Machines and computers lack context. When given context, they require more resources. While accurate, BERT took two hours to train using simpletransformers. TF-IDF is useful in objective classification, but may fail to identify context needed for accurate subjective multiclass classification. Ensemble methods are techniques that create multiple models and then combine them to produce improved results. Ensemble methods usually produces more accurate solutions than a single model would.

# Usage and Project Status
The repository and code can be used and adapted for any text classification problems. The Flask app also provides a simple template for creating a website using an exported machine learning model. While project week is over, the project is far from complete. In the future, the Flask app would be deployed to a hosting service and the model be saved in an S3 bucket for retrieval as opposed to being saved locally. Currently a major downside of the Flask app running locally is that the app cannot handle simultaneous multiprocessing and only provides outputs in debugger mode. Also, we believe having another input feature of the website where the user indicates whether the emotion predicted/returned is accurate. In addition, we would like the model trained on more nuanced emotions. We would also like to revisit the BERT and Naive Bayes model using different libraries, specifically with Spark.


<p align="center">
  <img src="https://user-images.githubusercontent.com/107419765/205708159-5cb5bb5e-d714-4027-907f-0d16925feaca.png" alt="Sublime's custom image"/>
</p>






