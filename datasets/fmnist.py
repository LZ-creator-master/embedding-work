"""
Fashion-MNIST 服装商品数据集（Zalando）
70000样本, 784维(28x28), 10类
和MNIST同结构但类别更难分，适合对比t-SNE和UMAP在复杂结构上的表现
第一次运行会自动下载约30MB数据
"""
import numpy as np

DESCRIPTION = "Fashion-MNIST服装, 70000样本, 784维, 10类（难分版MNIST）"


def load():
    from sklearn.datasets import fetch_openml
    data = fetch_openml('Fashion-MNIST', version=1, as_frame=False, parser='auto')
    X = data.data.astype(float)
    y = data.target.astype(int)
    return X, y
