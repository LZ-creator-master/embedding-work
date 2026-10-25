# -*- coding: utf-8 -*-
"""
config.py —— SUDE 对比实验全局配置
====================================
所有可调参数都集中在这里，一般只需要改「数据集选择」部分。

使用方法：
    1. 改 DATASET_NAME 选择内置数据集（ucimlrepo 自动下载）
    2. 或者改 CSV_PATH 加载你自己的数据文件（csv/npy/txt）
    3. 运行 run_compare.py 即可出图
"""

# ================= 数据集选择（二选一） =================
# 方案A：使用内置数据集（ucimlrepo 自动下载，无需手动准备文件）
#   可选: 'wine' / 'dermatology' / 'breast_cancer' / 'iris' / 'digits'
#   注意: 首次运行需要联网下载数据
DATASET_NAME = 'wine'

# 方案B：使用你自己的数据文件（CSV格式）
#   把 CSV_PATH 改成你的文件绝对路径，并填上标签列的位置
#   示例: CSV_PATH = r'D:\my_data\mydata.csv'
CSV_PATH = ''          # 留空表示不使用CSV
CSV_LABEL_COL = -1     # 标签列索引: -1表示最后一列, 0表示第一列, 或填列号
CSV_DELIMITER = ','    # 分隔符, 常见 ',' 或 ' ' (空格) 或 '\t' (制表符)

# 图的标题里显示的数据集名称
DATASET_LABEL = 'Wine数据集'

# ================= t-SNE 参数 =================
TSNE_PERPLEXITY = 30       # 困惑度（样本少用5~15，样本多用30~50）
TSNE_MAX_ITER = 1000       # 迭代次数
TSNE_RANDOM_STATE = 42     # 随机种子（保证可复现）

# ================= UMAP 参数 =================
UMAP_N_NEIGHBORS = 20      # 近邻数（小样本5~15，大样本20~50）
UMAP_MIN_DIST = 0.1        # 最小距离（0~1，越小越紧凑）
UMAP_RANDOM_STATE = 42

# ================= SUDE 参数 =================
# n_neighbors 对应论文中的 k1（采样时的近邻数，默认20，小数据集建议10）
# init: 'le'（拉普拉斯特征映射初始化，推荐）/ 'pca' / 'mds'
# max_iter: 迭代轮数（论文默认50，想更稳定可调大）
SUDE_N_NEIGHBORS = 10
SUDE_INIT = 'le'
SUDE_MAX_ITER = 50

# ================= 可视化 =================
# 原始高维数据降维到3D所用的方法（'pca' 线性投影最直观）
ORIG_3D_METHOD = 'pca'
FIGSIZE = (18, 16)         # 整体画布大小（2x2四宫格）
FIG_DPI = 150
CMAP = 'tab10'             # 颜色方案（多类用 tab10/Spectral）
POINT_SIZE = 20            # 散点大小
ALPHA = 0.7                # 散点透明度
OUTPUT_FIG = 'sude_compare.png'   # 输出图片文件名
