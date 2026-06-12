from flask import Flask, render_template, request
import joblib

app = Flask(__name__)

# Load Model & Vectorizer
model = joblib.load("model.pkl")
vectorizer = joblib.load("vectorizer.pkl")


@app.route("/", methods=["GET", "POST"])
def home():

    result = ""
    result_class = ""
    probability = 0

    if request.method == "POST":

        email_text = request.form["email"]

        vector = vectorizer.transform([email_text])

        prediction = model.predict(vector)[0]

        probs = model.predict_proba(vector)[0]

        if prediction == 1:

            probability = round(probs[1] * 100, 2)

            result = "⚠️ Phishing Email Detected"
            result_class = "phishing"

        else:

            probability = round(probs[0] * 100, 2)

            result = "✅ Legitimate Email"
            result_class = "safe"

    return render_template(
        "index.html",
        result=result,
        result_class=result_class,
        probability=probability
    )


if __name__ == "__main__":
    app.run(debug=True)