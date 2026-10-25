"""
MNIST 手写数字数据集（Yann LeCun）
70000样本, 784维(28x28), 10类
经典大样本高维数据集，t-SNE跑起来很慢，适合展示算法扩展性问题
第一次运行会自动下载约11MB数据
"""
import numpy as np

DESCRIPTION = "MNIST手写数字, 70000样本, 784维, 10类（大样本高维）"


def load():
    from sklearn.datasets import fetch_openml
    data = fetch_openml('mnist_784', version=1, as_frame=False, parser='auto')
    X = data.data.astype(float)
    y = data.target.astype(int)
    return X, y
