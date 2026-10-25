"""
config.py —— 全局配置
====================
所有可调参数都在这里，一般只需要改这个文件
"""

# ========== 数据集选择 ==========
# 可选: 'wine' / 'dermatology' / 'iris_test'
# 想加新数据集? 去 datasets/ 文件夹新建一个 .py 文件, 在 datasets/__init__.py 注册
DATASET_NAME = 'pbmc3k'
DATASET_LABEL = 'PBMC3k单细胞(导师推荐)'   # 图标题里显示的名字

# ========== t-SNE 参数 ==========
TSNE_PERPLEXITY = 30       # 困惑度（样本少用5~15，样本多用30~50）
TSNE_MAX_ITER = 1000       # 迭代次数
TSNE_RANDOM_STATE = 42     # 随机种子（保证可复现）

# ========== UMAP 参数 ==========
UMAP_N_NEIGHBORS = 20      # 近邻数（小样本5~15，大样本20~50）
UMAP_MIN_DIST = 0.1        # 最小距离（0~1，越小团越紧）
UMAP_RANDOM_STATE = 42

# ========== 可视化 ==========
FIGSIZE = (14, 6)          # 两张子图的整体大小
FIG_DPI = 150
CMAP = 'tab10'             # 颜色方案（多类用 tab10/Spectral）
POINT_SIZE = 25            # 散点大小
OUTPUT_FIG = 'embedding_compare.png'  # 输出图文件名
