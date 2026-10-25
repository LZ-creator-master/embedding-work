"""
batch_plot_all.py —— 批量生成50个神经元的降维对比图（黑白+连线版）
====================================================
每个神经元输出一张2x2图：原始3D / PCA 2D / t-SNE 2D / UMAP 2D
特点：
  1. 画上父子节点连线，展示神经元树状结构
  2. 全部黑白配色，简洁清晰

运行：右键 Run 'batch_plot_all'
"""
import os
import numpy as np
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D
from sklearn.decomposition import PCA
from sklearn.manifold import TSNE
import umap


def read_swc(file_path):
    """读取SWC，返回 pts数组 和 edges边列表[(idx_a, idx_b), ...]"""
    raw = {}
    edges = []
    with open(file_path, 'r') as f:
        for line in f:
            line = line.strip()
            if not line or line.startswith('#'):
                continue
            parts = line.split()
            if len(parts) < 7:
                continue
            nid = int(float(parts[0]))
            type_ = int(float(parts[1]))
            x, y, z = float(parts[2]), float(parts[3]), float(parts[4])
            parent = int(float(parts[6]))
            raw[nid] = [type_, x, y, z]
            if parent != -1:
                edges.append((parent, nid))
    ids = sorted(raw.keys())
    pts = np.array([raw[i] for i in ids])
    id_to_idx = {nid: idx for idx, nid in enumerate(ids)}
    edge_idx = [(id_to_idx[a], id_to_idx[b])
                for a, b in edges if a in id_to_idx and b in id_to_idx]
    return pts, edge_idx


def plot_one(swc_path, out_dir):
    name = os.path.basename(swc_path).replace('.swc', '')
    pts, edges = read_swc(swc_path)
    xyz = pts[:, 1:4]   # x,y,z
    types = pts[:, 0].astype(int)

    # 降维
    Y_pca = PCA(n_components=2, random_state=42).fit_transform(xyz)
    perp = min(30, max(5, len(xyz)//100))
    Y_tsne = TSNE(n_components=2, perplexity=perp, random_state=42).fit_transform(xyz)
    n_neighbors = min(30, max(5, len(xyz)//100))
    Y_umap = umap.UMAP(n_neighbors=n_neighbors, random_state=42).fit_transform(xyz)

    fig = plt.figure(figsize=(14, 12))
    soma = types == 1

    # 左上：原始3D
    ax1 = fig.add_subplot(2, 2, 1, projection='3d')
    for a, b in edges:
        ax1.plot([xyz[a,0], xyz[b,0]], [xyz[a,1], xyz[b,1]], [xyz[a,2], xyz[b,2]],
                 color='gray', linewidth=0.5)
    ax1.scatter(xyz[soma,0], xyz[soma,1], xyz[soma,2], c='black', s=30, zorder=10)
    ax1.scatter(xyz[~soma,0], xyz[~soma,1], xyz[~soma,2], c='gray', s=1, alpha=0.5)
    ax1.set_title('Original 3D', fontsize=13, fontweight='bold')

    # 右上：PCA 2D
    ax2 = fig.add_subplot(2, 2, 2)
    for a, b in edges:
        ax2.plot([Y_pca[a,0], Y_pca[b,0]], [Y_pca[a,1], Y_pca[b,1]],
                 color='gray', linewidth=0.5)
    ax2.scatter(Y_pca[soma,0], Y_pca[soma,1], c='black', s=30, zorder=10)
    ax2.scatter(Y_pca[~soma,0], Y_pca[~soma,1], c='gray', s=1, alpha=0.5)
    ax2.set_title('PCA (2D)', fontsize=13, fontweight='bold')

    # 左下：t-SNE 2D
    ax3 = fig.add_subplot(2, 2, 3)
    for a, b in edges:
        ax3.plot([Y_tsne[a,0], Y_tsne[b,0]], [Y_tsne[a,1], Y_tsne[b,1]],
                 color='gray', linewidth=0.5)
    ax3.scatter(Y_tsne[soma,0], Y_tsne[soma,1], c='black', s=30, zorder=10)
    ax3.scatter(Y_tsne[~soma,0], Y_tsne[~soma,1], c='gray', s=1, alpha=0.5)
    ax3.set_title('t-SNE (2D)', fontsize=13, fontweight='bold')

    # 右下：UMAP 2D
    ax4 = fig.add_subplot(2, 2, 4)
    for a, b in edges:
        ax4.plot([Y_umap[a,0], Y_umap[b,0]], [Y_umap[a,1], Y_umap[b,1]],
                 color='gray', linewidth=0.5)
    ax4.scatter(Y_umap[soma,0], Y_umap[soma,1], c='black', s=30, zorder=10)
    ax4.scatter(Y_umap[~soma,0], Y_umap[~soma,1], c='gray', s=1, alpha=0.5)
    ax4.set_title('UMAP (2D)', fontsize=13, fontweight='bold')

    plt.suptitle(f'Neuron: {name}', fontsize=15, y=1.01)
    plt.tight_layout()
    out_path = os.path.join(out_dir, f'{name}.png')
    plt.savefig(out_path, dpi=120, bbox_inches='tight', facecolor='white')
    plt.close()
    print(f"  [完成] {name}.png")


def main():
    swc_dir = os.path.join(os.path.dirname(__file__), '..', 'swc_data')
    swc_dir = os.path.abspath(swc_dir)
    out_dir = os.path.join(os.path.dirname(__file__), 'output_figures')
    os.makedirs(out_dir, exist_ok=True)

    files = sorted([f for f in os.listdir(swc_dir) if f.endswith('.swc')])
    print(f"共 {len(files)} 个神经元，开始批量出图（黑白连线版）...\n")

    for i, f in enumerate(files):
        print(f"[{i+1}/{len(files)}] {f}")
        plot_one(os.path.join(swc_dir, f), out_dir)

    print(f"\n全部完成！图片保存在: {out_dir}")


if __name__ == '__main__':
    main()
