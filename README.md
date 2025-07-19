# Project: Aave V2 Wallet Credit Scoring

This project assigns a **credit score (0–1000)** to wallets based on their transaction history on the Aave V2 protocol. The goal is to reward responsible behavior and flag risky or exploitative usage.

---

### 🔍 Data
- Input: Raw JSON of transaction-level records
- Each record contains: `wallet`, `timestamp`, `action`, `amount`, `asset`

---

### ⚙️ Features Engineered
- `total_txns`, `unique_assets`
- `deposit_amt`, `borrow_amt`, `repay_amt`, `liquidation_amt`
- Ratios: `deposit_to_borrow`, `repay_to_borrow`, `liquidation_ratio`
- `duration_days` — span of wallet activity

---

### 🧠 Scoring Logic
Score is composed of:
- ✅ Low liquidation ratio → +300
- ✅ High repay-to-borrow ratio → +300
- ✅ Long active duration → +100
- ✅ Diversity in assets → +100
- ➕ All scores normalized and clipped between 0–1000

---

### ▶️ Usage
```bash
python generate_scores.py --input user-transactions.json --output wallet_scores.csv
```

---

### 📦 Requirements
```
pandas
numpy
```
Install with:
```bash
pip install -r requirements.txt
```

---

### 📁 File Structure
```
.
├── generate_scores.py
├── features.py
├── scoring.py
├── README.md
└── analysis.md
```

---

### 📌 Author
Built by Archit Nidhi – for DeFi creditworthiness insights using only on-chain behavior.
