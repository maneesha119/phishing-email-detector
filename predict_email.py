import pandas as pd

from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.ensemble import RandomForestClassifier

# Load Dataset
df = pd.read_csv("dataset/phishing_email.csv")

X = df["text_combined"]
y = df["label"]

# Convert text to numbers
vectorizer = TfidfVectorizer(max_features=5000)
X_tfidf = vectorizer.fit_transform(X)

# Train model
model = RandomForestClassifier(
    n_estimators=100,
    random_state=42
)

model.fit(X_tfidf, y)

# User input
email = input("Enter Email Text: ")

email_vector = vectorizer.transform([email])

prediction = model.predict(email_vector)

if prediction[0] == 1:
    print("⚠️ Phishing Email")
else:
    print("✅ Legitimate Email")