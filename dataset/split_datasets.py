import pandas as pd
from consts.paths import Paths

def split(dataset):
    print(f'Original dataset shape: {dataset.shape}')
    train_df = data