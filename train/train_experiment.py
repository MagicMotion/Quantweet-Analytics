import torch
import pandas as pd

from train.train import Train
from consts.paths import Paths
from dataset.dataset import Dataset
from quantum.circuits import Circuit
from quantum.diagrams import Diagram
from quantum.parameters import Parameter
from dataset.preprocess import Preprocess


dataset = pd.read_csv(Paths.train_dataset_path)
dev_dataset = pd.read_csv(Paths.test_dataset_path)

clean_dataset = Pre