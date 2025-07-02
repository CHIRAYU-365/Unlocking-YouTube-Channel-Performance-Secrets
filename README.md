# Unlocking-YouTube-Channel-Performance-Secrets

# 🔹 Project 1: Unlocking YouTube Channel Performance Secrets

## ✏️ Objective:

To predict YouTube video revenue based on performance indicators such as views, engagement, and
subscriber data. The primary aim was to assist content creators in forecasting revenue for videos before
publishing.

## 📈 Dataset Summary:

The dataset included over 350 video entries with the following key features:

```
Engagement Metrics: Views, Likes, Shares, Comments, Subscribers
Revenue Metrics: Estimated Revenue (USD), Revenue per 1000 Views, Ad Impressions
Audience Behavior: Unique Viewers, Returning Viewers, New Subscribers
```
## ⚡️ Key Implementation Steps:

**✉️ Data Preprocessing**

```
Null values were filled with zeros
Irrelevant columns were dropped
Derived column: Engagement Rate
```
```
# Create engagement rate feature
df['Engagement Rate'] = (df['Likes'] + df['Shares'] + df['New Comments']) /
df['Views'] * 100
```
### • • • • • •


**🔧 Model Building (Random Forest)**

```
Features selected: Views, Subscribers, Likes, Shares, Comments, Engagement Rate
Model: RandomForestRegressor
```
```
model= RandomForestRegressor(n_estimators=100, random_state=42)
model.fit(X_train, y_train)
joblib.dump(model,'youtube_revenue_predictor.pkl')
```
**📄 Deployment using Flask**

```
A Flask server was created with endpoints to:
Render HTML form
Accept user input
Predict revenue using the trained model
```
```
@app.route("/predict", methods=["POST"])
defpredict():
input_data = [float(request.form[field])forfield infields]
prediction = model.predict([input_data])[0]
return render_template("index.html", prediction=round(prediction, 2))
```
**🌐 Dashboard Integration (Chart.js)**

A dynamic dashboard was implemented to visually track predictions made by the model over time.

```
constchart =new Chart(ctx, {
type: 'bar',
data: {
labels: [...],
datasets: [
{ label: 'Predicted Revenue ($)', data: [...] },
{ label: 'Views', data: [...]}
]
}
});
```
## 🚀 Outcome:

An interactive web app capable of predicting revenue based on inputs and visualizing past predictions in a
dashboard. Clear thresholds (e.g., \$100) were also implemented for guidance.

### • • • • • •
