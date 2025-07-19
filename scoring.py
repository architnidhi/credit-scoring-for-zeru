import pandas as pd
import numpy as np

def normalize(series):
    return 1000 * (series - series.min()) / (series.max() - series.min() + 1e-5)

def score_wallets(df):
    df['score'] = 0

    # Penalize high liquidation ratio
    df['score'] += (1 - df['liquidation_ratio'].clip(0, 1)) * 300

    # Reward repayment-to-borrow ratio
    df['score'] += df['repay_to_borrow_ratio'].clip(0, 1) * 300

    # Reward long duration of activity
    df['score'] += normalize(df['duration_days']) * 0.1 * 1000

    # Reward diversity of transactions
    df['score'] += normalize(df['unique_assets']) * 0.1 * 1000

    # Normalize to 0–1000 range finally
    df['score'] = df['score'].clip(0, 1000)

    return df[['wallet', 'score']]
