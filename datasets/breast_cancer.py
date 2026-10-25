"""
Breast Cancer 威斯康星乳腺癌数据集（sklearn内置）
569样本, 30维, 2类（良性/恶性）
"""
import numpy as np

DESCRIPTION = "乳腺癌诊断, 569样本, 30维, 2类"


def load():
    from sklearn.datasets import load_breast_cancer
    data = load_breast_cancer()
    return data.data, data.target
