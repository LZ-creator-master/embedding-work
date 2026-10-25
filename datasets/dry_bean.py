"""
Dry Bean 干豆数据集（UCI id=602）
13611样本, 16维, 7类（7种土耳其豆类）
中等规模多类，适合展示多类别下t-SNE的类间粘连问题
"""
import numpy as np

DESCRIPTION = "干豆品种分类, 13611样本, 16维, 7类"


def load():
    from ucimlrepo import fetch_ucirepo
    data = fetch_ucirepo(id=602)
    X = np.asarray(data.data.features.values, dtype=float)
    y = np.asarray(data.data.targets.values).ravel()
    return X, y
