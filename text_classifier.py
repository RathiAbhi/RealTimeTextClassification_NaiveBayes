"""
Naive-Bayes classifier for text classification
"""

import string
import nltk
import pickle
from nltk.corpus import stopwords
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.naive_bayes import MultinomialNB

nltk.download("stopwords")

class TextClassifier:
    def __init__(self):
        self.vectorizer = TfidfVectorizer(max_features=5000)
        self.model = MultinomialNB()

    def clean_text(self,text):
        text = text.lower().translate(str.maketrans("","",string.punctuation))
        words = [word for word in text.split() if word not in stopwords.words("english")]
        return " ".join(words)

    def train(self,data,labels):
        X = self.vectorizer.fit_transform([self.clean_text(entry["summary"]) for entry in data])
        self.model.fit(X,labels)
        pickle.dump(self.model, open("disc_model.pkl","wb"))

    def predict(self,text):
        text_vectorized = self.vectorizer.transform([self.clean_text(text)])
        return self.model.predict(text_vectorized)[0]