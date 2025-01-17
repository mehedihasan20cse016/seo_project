import pandas as pd

def combine_datasets():
    # Paths
    stackoverflow_path = "data/stackoverflow_data.csv"
    kaggle_path = "data/kaggle_dataset.csv"
    combined_path = "data/combined_dataset.csv"

    # Read datasets
    stackoverflow_data = pd.read_csv(stackoverflow_path)
    kaggle_data = pd.read_csv(kaggle_path)

    # Combine datasets
    combined_data = pd.concat([stackoverflow_data, kaggle_data]).drop_duplicates(subset="question").reset_index(drop=True)

    # Save combined dataset
    combined_data.to_csv(combined_path, index=False)
    print(f"Combined dataset saved to {combined_path}")

if __name__ == "__main__":
    combine_datasets()
