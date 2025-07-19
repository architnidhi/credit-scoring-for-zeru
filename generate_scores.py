import argparse
import json
import pandas as pd
from features import build_features
from scoring import score_wallets

def main(input_path, output_path):
    with open(input_path, 'r') as f:
        raw_data = json.load(f)

    df = pd.DataFrame(raw_data)
    features_df = build_features(df)
    scored_df = score_wallets(features_df)
    scored_df.to_csv(output_path, index=False)
    print(f"Wallet scores written to {output_path}")

if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="Generate credit scores for Aave V2 wallets")
    parser.add_argument("--input", required=True, help="Path to input JSON file")
    parser.add_argument("--output", required=True, help="Path to output CSV file")
    args = parser.parse_args()

    main(args.input, args.output)
