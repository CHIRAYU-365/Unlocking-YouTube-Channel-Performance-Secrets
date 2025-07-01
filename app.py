from flask import Flask, render_template, request, redirect, url_for
import numpy as np
import joblib

app = Flask(__name__)
model = joblib.load("youtube_revenue_predictor.pkl")

# In-memory prediction history for dashboard
history = []

@app.route("/", methods=["GET"])
def index():
    return render_template("index.html")

@app.route("/clear", methods=["POST"])
def clear_predictions():
    global history
    history = []
    return redirect(url_for("dashboard"))

@app.route("/predict", methods=["POST"])
def predict():
    try:
        views = float(request.form["views"])
        subscribers = float(request.form["subscribers"])
        likes = float(request.form["likes"])
        shares = float(request.form["shares"])
        comments = float(request.form["comments"])
        engagement_rate = float(request.form["engagement_rate"])

        features = np.array([[views, subscribers, likes, shares, comments, engagement_rate]])
        prediction = round(model.predict(features)[0], 2)

        # Add to history
        history.append({
            "views": views,
            "subscribers": subscribers,
            "prediction": prediction
        })

        return render_template("index.html", prediction=prediction)
    except Exception as e:
        return f"Error: {e}"

@app.route("/dashboard")
def dashboard():
    labels = list(range(1, len(history) + 1))
    predictions = [entry["prediction"] for entry in history]
    views = [entry["views"] for entry in history]

    return render_template("dashboard.html", labels=labels, predictions=predictions, views=views)

if __name__ == "__main__":
    app.run(debug=True, host='0.0.0.0')
