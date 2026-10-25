"""
summary_table.py —— 多数据集对比总结表
=========================================
自动跑多个数据集，生成一张大图：
  行 = 数据集（从上到下：从简单到难）
  列 = Original(PCA 3D) / t-SNE(2D) / UMAP(2D)

运行后保存为 summary_comparison.png，直接可以放PPT
"""

import numpy as np
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D
from sklearn.decomposition import PCA
from sklearn.manifold import TSNE
import umap
import config
from datasets import REGISTRY

# 要对比的数据集（按难度从易到难排序）
DATASETS_TO_RUN = [
    'iris_test',
    'wine',
    'breast_cancer',
    'dermatology',
    'mfeat',       # 目前是digits替代
    'pbmc3k',      # 导师推荐：单细胞数据
]


def run_all():
    n_rows = len(DATASETS_TO_RUN)
    n_cols = 3  # Original 3D, t-SNE, UMAP

    fig = plt.figure(figsize=(15, 5 * n_rows))

    for row_idx, ds_name in enumerate(DATASETS_TO_RUN):
        print(f"\n[运行] {ds_name}...")
        mod = REGISTRY[ds_name]
        X, y = mod.load()
        print(f"  数据形状: {X.shape}")

        # 1. PCA 3D 原始结构
        Y_pca3d = PCA(n_components=3, random_state=42).fit_transform(X)
        ax1 = fig.add_subplot(n_rows, n_cols, row_idx * n_cols + 1, projection='3d')
        ax1.scatter(Y_pca3d[:, 0], Y_pca3d[:, 1], Y_pca3d[:, 2],
                    c=y, cmap=config.CMAP, s=8, alpha=0.7)
        ax1.set_xticks([])
        ax1.set_yticks([])
        ax1.set_zticks([])
        if row_idx == 0:
            ax1.set_title('Original (PCA 3D)', fontsize=14, fontweight='bold')

        # 2. t-SNE 2D
        # 小数据集用小困惑度，大数据集用大一点
        perp = min(30, max(5, X.shape[0] // 20))
        Y_tsne = TSNE(n_components=2, perplexity=perp,
                      max_iter=config.TSNE_MAX_ITER,
                      random_state=42).fit_transform(X)
        ax2 = fig.add_subplot(n_rows, n_cols, row_idx * n_cols + 2)
        ax2.scatter(Y_tsne[:, 0], Y_tsne[:, 1],
                    c=y, cmap=config.CMAP, s=8, alpha=0.7)
        ax2.set_xticks([])
        ax2.set_yticks([])
        if row_idx == 0:
            ax2.set_title('t-SNE', fontsize=14, fontweight='bold')

        # 3. UMAP 2D
        n_neighbors = min(20, max(5, X.shape[0] // 50))
        Y_umap = umap.UMAP(n_neighbors=n_neighbors, min_dist=0.1,
                           random_state=42).fit_transform(X)
        ax3 = fig.add_subplot(n_rows, n_cols, row_idx * n_cols + 3)
        ax3.scatter(Y_umap[:, 0], Y_umap[:, 1],
                    c=y, cmap=config.CMAP, s=8, alpha=0.7)
        ax3.set_xticks([])
        ax3.set_yticks([])
        if row_idx == 0:
            ax3.set_title('UMAP', fontsize=14, fontweight='bold')

        # 行标签（数据集名字）
        ax1.set_ylabel(f'{ds_name}\n{X.shape[0]}×{X.shape[1]}',
                       fontsize=11, fontweight='bold', labelpad=15)

    plt.suptitle('Manifold Learning Comparison: Original vs t-SNE vs UMAP',
                 fontsize=16, y=1.01)
    plt.tight_layout()
    plt.savefig('summary_comparison.png', dpi=150, bbox_inches='tight')
    print(f"\n[完成] 已保存: summary_comparison.png")
    plt.close()


if __name__ == '__main__':
    run_all()
