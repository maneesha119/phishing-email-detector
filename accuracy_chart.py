import matplotlib.pyplot as plt

models = ["Naive Bayes", "Logistic Regression", "Random Forest"]
accuracy = [96.16, 98.18, 98.67]

plt.figure(figsize=(8,5))
plt.bar(models, accuracy)

plt.title("Model Accuracy Comparison")
plt.ylabel("Accuracy (%)")
plt.ylim(95, 100)

plt.savefig("accuracy_chart.png")
plt.show()