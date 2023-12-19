import numpy as np
import pandas as pd


# returns name of samples (ex. country names) as well as x (relevant variable 1), y (relevant var 2) and z (constant var) given path
def data_loader(path):
    samples, x, y, z = [], [], [], []
    df = pd.read_excel(path)
    df = df.to_numpy()
    for a, b, c, d in df:
        samples.append(a)
        x.append(b)
        y.append(c)
        z.append(d)
    return samples, x, y, z


