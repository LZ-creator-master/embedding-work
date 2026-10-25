"""
Iris 测试数据集（sklearn内置）
150样本, 4维, 3类
用来跑通流程，不用联网
"""
import numpy as np

DESCRIPTION = "鸢尾花(测试用), 150样本, 4维, 3类"


def load():
    from sklearn.datasets import load_iris
    data = load_iris()
    return data.data, data.target
