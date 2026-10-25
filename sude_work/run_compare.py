# -*- coding: utf-8 -*-
"""
run_compare.py —— SUDE 与经典流形算法对比实验（主程序）
========================================================
输出一张 2x2 四宫格对比图：
    左上：原始高维数据的3D结构（PCA降维到3D展示，最能反映原始分布）
    右上：t-SNE 2D
    左下：UMAP 2D
    右下：SUDE 2D

运行方法：
    1. 在 PyCharm 里打开本文件，右键 -> Run 'run_compare'
    2. 或者终端执行: python run_compare.py

切换数据集：
    打开 config.py，修改 DATASET_NAME 或 CSV_PATH（详见config.py注释）
"""
import time
import numpy as np
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D
from sklearn.decomposition import PCA
from sklearn.manifold import TSNE

import config
from data_loader import load_data


def run_tsne(X, cfg):
    """t-SNE 降维到2D"""
    print('  [t-SNE] 运行中...')
    t0 = time.time()
    Y = TSNE(n_components=2,
             perplexity=cfg.TSNE_PERPLEXITY,
             max_iter=cfg.TSNE_MAX_ITER,
             random_state=cfg.TSNE_RANDOM_STATE).fit_transform(X)
    print(f'  [t-SNE] 完成, 耗时 {time.time()-t0:.1f}s')
    return Y


def run_umap(X, cfg):
    """UMAP 降维到2D"""
    print('  [UMAP] 运行中...')
    import umap
    t0 = time.time()
    Y = umap.UMAP(n_neighbors=cfg.UMAP_N_NEIGHBORS,
                  min_dist=cfg.UMAP_MIN_DIST,
                  random_state=cfg.UMAP_RANDOM_STATE).fit_transform(X)
    print(f'  [UMAP] 完成, 耗时 {time.time()-t0:.1f}s')
    return Y


def run_sude(X, cfg):
    """SUDE 降维到2D（官方实现）"""
    print('  [SUDE] 运行中...')
    from sude import SUDE
    t0 = time.time()
    model = SUDE(n_components=2,
                 n_neighbors=cfg.SUDE_N_NEIGHBORS,
                 init=cfg.SUDE_INIT,
                 max_iter=cfg.SUDE_MAX_ITER)
    Y = model.fit_transform(X)
    print(f'  [SUDE] 完成, 耗时 {time.time()-t0:.1f}s')
    return Y


def run_orig_3d(X, cfg):
    """原始数据投影到3D用于展示"""
    print(f'  [原始3D] 用{cfg.ORIG_3D_METHOD.upper()}降到3D展示...')
    if cfg.ORIG_3D_METHOD == 'pca':
        Y = PCA(n_components=3, random_state=42).fit_transform(X)
    else:
        # 高维数据先PCA到50维再t-SNE到3D（数据过大时的替代方案）
        from sklearn.manifold import TSNE
        Y = TSNE(n_components=3, random_state=42).fit_transform(X)
    return Y


def plot_compare(Y3d, Y_tsne, Y_umap, Y_sude, y, label, cfg, X=None):
    """绘制2x2四宫格对比图"""
    fig = plt.figure(figsize=cfg.FIGSIZE)

    # ---- 左上: 原始3D结构 ----
    ax1 = fig.add_subplot(2, 2, 1, projection='3d')
    sc = ax1.scatter(Y3d[:, 0], Y3d[:, 1], Y3d[:, 2],
                     c=y, cmap=cfg.CMAP, s=cfg.POINT_SIZE, alpha=cfg.ALPHA)
    ax1.set_title(f'Original 3D Structure\n({cfg.ORIG_3D_METHOD.upper()})',
                  fontsize=14, fontweight='bold')
    ax1.set_xlabel('Dim1')
    ax1.set_ylabel('Dim2')
    ax1.set_zlabel('Dim3')

    # ---- 右上: t-SNE ----
    ax2 = fig.add_subplot(2, 2, 2)
    ax2.scatter(Y_tsne[:, 0], Y_tsne[:, 1],
                c=y, cmap=cfg.CMAP, s=cfg.POINT_SIZE, alpha=cfg.ALPHA)
    ax2.set_title('t-SNE (2D)', fontsize=14, fontweight='bold')
    ax2.set_xlabel('Dim1')
    ax2.set_ylabel('Dim2')

    # ---- 左下: UMAP ----
    ax3 = fig.add_subplot(2, 2, 3)
    ax3.scatter(Y_umap[:, 0], Y_umap[:, 1],
                c=y, cmap=cfg.CMAP, s=cfg.POINT_SIZE, alpha=cfg.ALPHA)
    ax3.set_title('UMAP (2D)', fontsize=14, fontweight='bold')
    ax3.set_xlabel('Dim1')
    ax3.set_ylabel('Dim2')

    # ---- 右下: SUDE ----
    ax4 = fig.add_subplot(2, 2, 4)
    ax4.scatter(Y_sude[:, 0], Y_sude[:, 1],
                c=y, cmap=cfg.CMAP, s=cfg.POINT_SIZE, alpha=cfg.ALPHA)
    ax4.set_title('SUDE (2D)', fontsize=14, fontweight='bold')
    ax4.set_xlabel('Dim1')
    ax4.set_ylabel('Dim2')

    # 图例（取每个类别一个代表点）
    cmap_obj = plt.get_cmap(cfg.CMAP)
    handles = []
    seen = set()
    for i, lab in enumerate(y):
        if lab not in seen:
            seen.add(lab)
            handles.append(plt.Line2D([0], [0], marker='o', color='w',
                                      markerfacecolor=cmap_obj(lab % 10),
                                      markersize=8, label=f'Class {lab}'))
    fig.legend(handles=handles, loc='lower center', ncol=min(len(handles), 8),
               fontsize=10, frameon=False)

    plt.suptitle(f'Manifold Learning Comparison on {label} '
                 f'({len(y)} samples, {X.shape[1] if X is not None else "?"} dims)',
                 fontsize=16, fontweight='bold', y=0.98)
    plt.tight_layout(rect=[0, 0.05, 1, 0.95])
    plt.savefig(cfg.OUTPUT_FIG, dpi=cfg.FIG_DPI, bbox_inches='tight')
    print(f'[图] 已保存: {cfg.OUTPUT_FIG}')
    plt.close()


def main():
    # 1. 加载数据
    X, y, label = load_data(config)
    # 只保留前2000个样本（SUDE对小数据集用10近邻，避免过慢/过拟合）
    if len(X) > 3000:
        print(f'[数据] 样本数 {len(X)} 较大，为演示效果截取前3000个样本')
        X, y = X[:3000], y[:3000]

    # 2. 四种降维
    print('=' * 50)
    print(f'数据集: {label}  样本: {X.shape[0]}  维度: {X.shape[1]}  类别: {len(set(y))}')
    print('=' * 50)

    Y3d = run_orig_3d(X, config)
    Y_tsne = run_tsne(X, config)
    Y_umap = run_umap(X, config)
    Y_sude = run_sude(X, config)

    # 3. 绘图
    plot_compare(Y3d, Y_tsne, Y_umap, Y_sude, y, label, config, X=X)
    print('\n[完成] 对比图已生成，打开 sude_compare.png 查看结果')


if __name__ == '__main__':
    main()
