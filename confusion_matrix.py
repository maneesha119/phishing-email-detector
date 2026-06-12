import pandas as pd
import matplotlib.pyplot as plt

from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.model_selection import train_test_split
from sklearn.ensemble import RandomForestClassifier
from sklearn.metrics import ConfusionMatrixDisplay

df = pd.read_csv("dataset/phishing_email.csv")

X = df["text_combined"]
y = df["label"]

vectorizer = TfidfVectorizer(max_features=5000)
X = vectorizer.fit_transform(X)

X_train, X_test, y_train, y_test = train_test_split(
    X,
    y,
    test_size=0.2,
    random_state=42
)

model = RandomForestClassifier(
    n_estimators=100,
    random_state=42
)

model.fit(X_train, y_train)

ConfusionMatrixDisplay.from_estimator(
    model,
    X_test,
    y_test
)

plt.show()