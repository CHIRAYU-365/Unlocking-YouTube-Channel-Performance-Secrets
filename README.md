# Unlocking-YouTube-Channel-Performance-Secrets

# Project 1: Unlocking YouTube Channel Performance Secrets

## ✏️ Objective

To predict YouTube video revenue based on performance indicators such as views, engagement, and subscriber data. The primary aim was to assist content creators in forecasting revenue for videos before publishing.

## 📈 Dataset Summary

The dataset included over 350 video entries with the following key features:

- Engagement Metrics: `Views`, `Likes`, `Shares`, `Comments`, `Subscribers`
- Revenue Metrics: `Estimated Revenue (USD)`, `Revenue per 1000 Views`, `Ad Impressions`
- Audience Behavior: `Unique Viewers`, `Returning Viewers`, `New Subscribers`

## ⚡️ Key Implementation Steps

### ✉️ Data Preprocessing

- Null values were filled with zeros
- Irrelevant columns were dropped
- Derived column: `Engagement Rate`

```python
# Create engagement rate feature
df['Engagement Rate'] = (df['Likes'] + df['Shares'] + df['New Comments']) / df['Views'] * 100
