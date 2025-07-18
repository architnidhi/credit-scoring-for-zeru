import pandas as pd
import numpy as np

def build_features(df):
    df['timestamp'] = pd.to_datetime(df['timestamp'], unit='s')
    grouped = df.groupby('wallet')

    feature_list = []
    for wallet, txns in grouped:
        actions = txns['action'].value_counts().to_dict()
        total_txns = len(txns)
        n_assets = txns['asset'].nunique()

        deposits = txns[txns['action'] == 'deposit']['amount'].sum()
        borrows = txns[txns['action'] == 'borrow']['amount'].sum()
        repayments = txns[txns['action'] == 'repay']['amount'].sum()
        liquidations = txns[txns['action'] == 'liquidationcall']['amount'].sum()

        duration = (txns['timestamp'].max() - txns['timestamp'].min()).days
        duration = duration if duration > 0 else 1

        features = {
            'wallet': wallet,
            'total_txns': total_txns,
            'unique_assets': n_assets,
            'deposit_amt': deposits,
            'borrow_amt': borrows,
            'repay_amt': repayments,
            'liquidation_amt': liquidations,
            'duration_days': duration,
            'deposit_to_borrow_ratio': deposits / (borrows + 1),
            'repay_to_borrow_ratio': repayments / (borrows + 1),
            'liquidation_ratio': liquidations / (borrows + 1),
        }
        feature_list.append(features)

    return pd.DataFrame(feature_list)
