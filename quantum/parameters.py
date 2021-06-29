import torch
import tensornetwork as tn
from sympy import default_sort_key


class Parameter:

    def __init__(self, circuits):
        self.circuits = circuits
        self.parameters = sorted(
            {s for circ in circuits for s in circ.free_symbols},
            key=default_sort_key)

    def make_pred_fn(self):
        def