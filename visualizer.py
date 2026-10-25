"""
visualizer.py —— 可视化：并排对比 t-SNE 和 UMAP 的降维结果
"""

import matplotlib.pyplot as plt
import config


def plot_compare(Y_tsne, Y_umap, labels):
    """画两张并排的散点图，按类别上色"""
    fig, axes = plt.subplots(1, 2, figsize=config.FIGSIZE)

    for ax, Y, title in zip(
        axes,
        [Y_tsne, Y_umap],
        ['t-SNE', 'UMAP'],
    ):
        scatter = ax.scatter(
            Y[:, 0], Y[:, 1],
            c=labels, cmap=config.CMAP,
            s=config.POINT_SIZE, alpha=0.85, edgecolors='none',
        )
        ax.set_title(title, fontsize=14, fontweight='bold')
        ax.set_xlabel('Dimension 1')
        ax.set_ylabel('Dimension 2')
        ax.set_xticks([])
        ax.set_yticks([])

    plt.suptitle(f'{config.DATASET_LABEL}: t-SNE vs UMAP', fontsize=15, y=1.02)
    plt.tight_layout()
    plt.savefig(config.OUTPUT_FIG, dpi=config.FIG_DPI, bbox_inches='tight')
    print(f"[图] 已保存: {config.OUTPUT_FIG}")
    plt.show()
