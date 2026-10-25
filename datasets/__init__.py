"""
datasets/ —— 数据集注册表
=========================
想加新数据集？在这个文件夹里新建一个 .py 文件，然后在下面的 REGISTRY 里加一行就行。
其他代码完全不用动。
"""

from datasets import (
    wine, dermatology, iris_test,
    breast_cancer, mfeat, spambase, dry_bean,
    mnist, fmnist, pbmc3k,
)

# 注册表：名字 -> 模块
REGISTRY = {
    # 小规模测试
    'iris_test': iris_test,
    'wine': wine,
    'breast_cancer': breast_cancer,
    'dermatology': dermatology,
    # 中规模
    'mfeat': mfeat,
    'spambase': spambase,
    'dry_bean': dry_bean,
    # 大规模高维
    'mnist': mnist,
    'fmnist': fmnist,
    # 导师推荐方向：单细胞数据
    'pbmc3k': pbmc3k,
}


def list_datasets():
    """列出所有可用数据集"""
    print("可用数据集：")
    for name, mod in REGISTRY.items():
        print(f"  - {name:15s}  {mod.DESCRIPTION}")


def load(name):
    """按名字加载数据集，返回 (X, y)"""
    if name not in REGISTRY:
        raise ValueError(f"没有数据集 '{name}'，可用: {list(REGISTRY.keys())}")
    mod = REGISTRY[name]
    X, y = mod.load()
    print(f"[数据集] {name}: {X.shape[0]}样本 × {X.shape[1]}维, {len(set(y))}类")
    return X, y
