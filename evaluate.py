import argparse
import pandas as pd
from sklearn.metrics import roc_auc_score, accuracy_score, f1_score, precision_score, recall_score

def evaluate(df, threshold=0.5):
    y_true = df['label']
    y_score = df['pred']  # continuous prediction

    # Compute AUC
    auc = roc_auc_score(y_true, y_score)

    # Apply threshold to get binary predictions
    y_pred = (y_score >= threshold).astype(int)

    results = {
        'AUC': auc,
        'Accuracy': accuracy_score(y_true, y_pred),
        'F1': f1_score(y_true, y_pred),
        'Precision': precision_score(y_true, y_pred),
        'Recall': recall_score(y_true, y_pred)
    }

    return results

def main():
    parser = argparse.ArgumentParser()
    parser.add_argument('--input_file', required=True, help='TSV file with columns: pred, label')
    parser.add_argument('--output_file', required=True, help='Path to save evaluation results')
    parser.add_argument('--threshold', type=float, default=0.5, help='Threshold for converting probability to binary')
    args = parser.parse_args()

    df = pd.read_csv(args.input_file, sep='\t')
    results = evaluate(df, threshold=args.threshold)

    with open(args.output_file, 'w') as f:
        for k, v in results.items():
            f.write(f"{k}: {v:.4f}\n")

    print(" Evaluation completed:")
    for k, v in results.items():
        print(f"{k}: {v:.4f}")

if __name__ == '__main__':
    main()
