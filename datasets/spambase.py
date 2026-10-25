"""
Spambase 垃圾邮件数据集（UCI id=94）
4601样本, 57维, 2类（垃圾/正常邮件）
中规模稀疏特征，适合展示类不平衡下的降维表现
"""
import numpy as np

DESCRIPTION = "垃圾邮件识别, 4601样本, 57维, 2类"


def load():
    from ucimlrepo import fetch_ucirepo
    data = fetch_ucirepo(id=94)
    X = np.asarray(data.data.features.values, dtype=float)
    y = np.asarray(data.data.targets.values).ravel()
    return X, y
