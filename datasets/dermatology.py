"""
Dermatology 皮肤病数据集（UCI id=33）
来源: http://archive.ics.uci.edu/dataset/33/dermatology
366样本, 34维, 6类（有缺失值，已处理）
"""
import numpy as np
import pandas as pd

DESCRIPTION = "皮肤病诊断, 366样本, 34维, 6类（已处理缺失值）"


def load():
    from ucimlrepo import fetch_ucirepo
    derm = fetch_ucirepo(id=33)
    df = pd.DataFrame(derm.data.features.values)
    df = df.replace('?', np.nan).apply(pd.to_numeric).fillna(0)
    X = df.values.astype(float)
    y = np.asarray(derm.data.targets.values).ravel()
    return X, y
