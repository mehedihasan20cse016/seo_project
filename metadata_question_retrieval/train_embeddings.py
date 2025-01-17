from sklearn.model_selection import train_test_split
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.naive_bayes import MultinomialNB
from sklearn.metrics import classification_report
import pandas as pd
import joblib

def train_category_predictor():
    df = pd.read_csv("data/combined_dataset.csv")

    X = df['question']
    y = df['topic']

    vectorizer = TfidfVectorizer()
    X = vectorizer.fit_transform(X)

    X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)
    model = MultinomialNB()
    model.fit(X_train, y_train)

    y_pred = model.predict(X_test)
    print(classification_report(y_test, y_pred))

    joblib.dump((model, vectorizer), "models/category_model.joblib")
    print("Model saved to models/category_model.joblib")

train_category_predictor()
