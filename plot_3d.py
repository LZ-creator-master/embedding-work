"""
plot_3d.py —— 原始结构 vs 降维结果对比
=======================================
左边: PCA(3D)  数据的原始高维结构（可鼠标旋转）
中间: t-SNE(2D)
右边: UMAP(2D)

用法：右键 Run 'plot_3d'
弹出窗口后，用鼠标拖动左边的3D图旋转，观察数据真实结构；
再对比右边两个2D图，看降维是否忠实保留了3D里的类间关系。
"""

import numpy as np
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D
from sklearn.decomposition import PCA

import config
from data_loader import load_data


def run_3d():
    X, y = load_data()

    # 计算三种结果
    print("[计算] PCA(3D)...")
    Y_pca3d = PCA(n_components=3, random_state=config.TSNE_RANDOM_STATE).fit_transform(X)

    print("[计算] t-SNE(2D)...")
    from sklearn.manifold import TSNE
    Y_tsne = TSNE(n_components=2, perplexity=config.TSNE_PERPLEXITY,
                  max_iter=config.TSNE_MAX_ITER,
                  random_state=config.TSNE_RANDOM_STATE).fit_transform(X)

    print("[计算] UMAP(2D)...")
    import umap
    Y_umap = umap.UMAP(n_components=2, n_neighbors=config.UMAP_N_NEIGHBORS,
                      min_dist=config.UMAP_MIN_DIST,
                      random_state=config.UMAP_RANDOM_STATE).fit_transform(X)

    # 画图：一行三列
    fig = plt.figure(figsize=(18, 6))

    # 左：PCA 3D（原始结构）
    ax1 = fig.add_subplot(1, 3, 1, projection='3d')
    ax1.scatter(Y_pca3d[:, 0], Y_pca3d[:, 1], Y_pca3d[:, 2],
                c=y, cmap=config.CMAP, s=config.POINT_SIZE, alpha=0.85)
    ax1.set_title('Original Structure (PCA 3D)', fontsize=13, fontweight='bold')
    ax1.set_xlabel('PC1')
    ax1.set_ylabel('PC2')
    ax1.set_zlabel('PC3')

    # 中：t-SNE 2D
    ax2 = fig.add_subplot(1, 3, 2)
    ax2.scatter(Y_tsne[:, 0], Y_tsne[:, 1],
                c=y, cmap=config.CMAP, s=config.POINT_SIZE, alpha=0.85)
    ax2.set_title('t-SNE (2D)', fontsize=13, fontweight='bold')
    ax2.set_xticks([])
    ax2.set_yticks([])

    # 右：UMAP 2D
    ax3 = fig.add_subplot(1, 3, 3)
    ax3.scatter(Y_umap[:, 0], Y_umap[:, 1],
                c=y, cmap=config.CMAP, s=config.POINT_SIZE, alpha=0.85)
    ax3.set_title('UMAP (2D)', fontsize=13, fontweight='bold')
    ax3.set_xticks([])
    ax3.set_yticks([])

    plt.suptitle(f'{config.DATASET_LABEL}: Original Structure vs Manifold Embedding',
                 fontsize=15, y=1.02)
    plt.tight_layout()
    plt.savefig('embedding_3d_compare.png', dpi=config.FIG_DPI, bbox_inches='tight')
    print("[图] 静态图已保存: embedding_3d_compare.png")
    print("[提示] 用鼠标拖动左边3D图旋转，从不同角度观察原始结构")
    plt.show()


if __name__ == '__main__':
    run_3d()
