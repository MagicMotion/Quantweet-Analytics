import pandas as pd
from consts.paths import Paths

def split(dataset):
    print(f'Original dataset shape: {dataset.shape}')
    train_df = dataset.sample(frac=0.8)
    print(f'Train dataset shape: {train_df.shape}')
    train_df.to_csv(Pat