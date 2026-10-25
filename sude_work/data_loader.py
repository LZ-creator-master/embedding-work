# -*- coding: utf-8 -*-
"""
data_loader.py —— 数据加载器
=============================
负责把数据集加载成 (X, y) 格式：
    X: 样本特征矩阵, 形状 (N, D), N个样本, D维特征
    y: 标签数组, 形状 (N,)

支持两种数据来源：
    1. ucimlrepo 内置数据集（UCI机器学习仓库，自动下载）
    2. 本地 CSV/NPY/TXT 文件（自定义数据）

用法：
    from data_loader import load_data
    X, y, label = load_data()
"""
import os
import numpy as np

# ============ 内置数据集注册表 ============
# key: 数据集名称（对应 config.py 里的 DATASET_NAME）
# value: (ucimlrepo 中的数据集ID, 显示名称)
BUILTIN_DATASETS = {
    'wine':            (109, 'Wine'),
    'dermatology':     (33,  'Dermatology'),
    'breast_cancer':   (17,  'Breast Cancer'),
    'iris':            (53,  'Iris'),
    'digits':          (80,  'Digits'),
}


def _load_from_ucirepo(name):
    """从 UCI ML Repository 加载内置数据集"""
    try:
        from ucimlrepo import fetch_ucirepo
    except ImportError:
        raise ImportError('请先安装 ucimlrepo: pip install ucimlrepo')

    if name not in BUILTIN_DATASETS:
        raise ValueError(
            f'未知数据集 "{name}"，可选: {list(BUILTIN_DATASETS.keys())}'
        )

    repo_id, label = BUILTIN_DATASETS[name]
    print(f'[数据] 正在从UCI仓库下载数据集 "{label}" (ID={repo_id}) ...')
    data = fetch_ucirepo(id=repo_id)

    X = data.data.features
    y = data.data.targets

    # 转成numpy数组
    X = np.array(X, dtype=float)
    y = np.array(y)

    # 如果y是多列则取第一列；如果是字符串标签则编码
    if y.ndim > 1:
        y = y[:, 0]
    if y.dtype.kind in 'US':  # 字符串标签 -> 编码成数字
        from sklearn.preprocessing import LabelEncoder
        y = LabelEncoder().fit_transform(y)

    print(f'[数据] 加载完成: {X.shape[0]}个样本 × {X.shape[1]}维特征, {len(set(y))}个类别')
    return X, y, label


def _load_from_file(csv_path, label_col, delimiter):
    """从本地文件加载数据（支持 csv/txt/npy）"""
    if not os.path.exists(csv_path):
        raise FileNotFoundError(f'找不到数据文件: {csv_path}')

    print(f'[数据] 正在加载本地文件: {csv_path}')

    if csv_path.endswith('.npy'):
        arr = np.load(csv_path)
        X = arr[:, :label_col] if label_col >= 0 else arr[:, :-1]
        y = arr[:, label_col] if label_col >= 0 else arr[:, -1]
    else:
        arr = np.loadtxt(csv_path, delimiter=delimiter)
        if label_col < 0:
            label_col = arr.shape[1] - 1
        X = np.delete(arr, label_col, axis=1)
        y = arr[:, label_col]

    # 标签编码
    if y.dtype.kind in 'US':
        from sklearn.preprocessing import LabelEncoder
        y = LabelEncoder().fit_transform(y.astype(str))

    label = os.path.splitext(os.path.basename(csv_path))[0]
    print(f'[数据] 加载完成: {X.shape[0]}个样本 × {X.shape[1]}维特征, {len(set(y))}个类别')
    return X, y, label


def load_data(cfg):
    """
    加载数据。返回 (X, y, label)
      - cfg: config模块
    """
    if cfg.CSV_PATH:
        return _load_from_file(cfg.CSV_PATH, cfg.CSV_LABEL_COL, cfg.CSV_DELIMITER)
    return _load_from_ucirepo(cfg.DATASET_NAME)


if __name__ == '__main__':
    # 简单测试
    import config
    X, y, label = load_data(config)
    print(f'测试通过: {label}, X={X.shape}, y={y.shape}')
