import pandas as pd
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.naive_bayes import MultinomialNB
from sklearn.pipeline import Pipeline
import pickle

data = pd.read_csv("emails.csv")

X = data["text"]
y = data["label"]

model = Pipeline([
    ("tfidf", TfidfVectorizer()),
    ("clf", MultinomialNB())
])

model.fit(X, y)

pickle.dump(model, open("model.pkl", "wb"))

print("Model trained successfully!")