"""
手写数字 Digits 数据集（sklearn内置）
1797样本, 64维(8x8), 10类（0-9）
替代Mfeat：高维多类，适合展示t-SNE在高维下的困惑度敏感问题
不用联网，直接能跑
"""
import numpy as np

DESCRIPTION = "手写数字(替代Mfeat), 1797样本, 64维, 10类"


def load():
    from sklearn.datasets import load_digits
    data = load_digits()
    return data.data.astype(float), data.target
