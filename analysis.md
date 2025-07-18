# 📊 Aave V2 Wallet Credit Score Analysis

This report outlines the distribution and behavioral traits of wallets across different credit score ranges (0–1000).

---

### 🎯 Score Distribution
(Sample code to generate visualization below)
```python
import matplotlib.pyplot as plt
import pandas as pd

scores = pd.read_csv("wallet_scores.csv")
scores['score_bucket'] = (scores['score'] // 100) * 100
scores['score_bucket'] = scores['score_bucket'].astype(int)
scores['score_bucket'] = scores['score_bucket'].clip(upper=900)

bucket_counts = scores['score_bucket'].value_counts().sort_index()

plt.figure(figsize=(10,6))
bucket_counts.plot(kind='bar', color='skyblue')
plt.title("Wallet Score Distribution (0-1000)")
plt.xlabel("Score Bucket")
plt.ylabel("Number of Wallets")
plt.xticks(rotation=45)
plt.tight_layout()
plt.savefig("score_distribution.png")
```

---

### 🔴 Low Score Behavior (0–200)
- High liquidation-to-borrow ratio
- Little or no repayments
- Short transaction duration
- Likely exploit attempts or abandoned loans

### 🟡 Mid Score (400–600)
- Mixed behavior: Some repayment, moderate borrowing
- Limited asset usage
- Possibly new or casual users

### 🟢 High Score (800–1000)
- Consistent repayments
- Diversified assets and usage
- No liquidations
- Long, stable interaction with protocol

---

This score can be used to:
- Build user reputation profiles
- Assist in DeFi lending decisions
- Detect bot-like or risky wallet behavior

---

**Author**: Archit Nidhi
