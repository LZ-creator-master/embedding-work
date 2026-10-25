"""
Wine 数据集（UCI id=109）
来源: http://archive.ics.uci.edu/dataset/109/wine
178样本, 13维, 3类（意大利葡萄酒产地）
"""
import numpy as np

DESCRIPTION = "意大利葡萄酒化学分析, 178样本, 13维, 3类"


def load():
    from ucimlrepo import fetch_ucirepo
    wine = fetch_ucirepo(id=109)
    X = np.asarray(wine.data.features.values, dtype=float)
    y = np.asarray(wine.data.targets.values).ravel()
    return X, y
