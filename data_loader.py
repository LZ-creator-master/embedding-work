"""
data_loader.py —— 数据加载入口
=================================
你一般不用改这个文件。
换数据集：去 config.py 改 DATASET_NAME。
加新数据集：去 datasets/ 文件夹新建一个文件，在 datasets/__init__.py 注册。
"""

import config
from datasets import load as _load, list_datasets


def load_data():
    X, y = _load(config.DATASET_NAME)
    print(f"[数据] 形状: {X.shape[0]} 样本 × {X.shape[1]} 维")
    print(f"[数据] 类别数: {len(set(y))}, 每类样本: {[int(sum(y == c)) for c in sorted(set(y))]}")
    return X, y


if __name__ == '__main__':
    list_datasets()
