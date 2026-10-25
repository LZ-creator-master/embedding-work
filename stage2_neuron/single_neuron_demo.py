"""
single_neuron_demo.py —— 单个神经元点云的降维实验
=================================================
输入：一个SWC文件里的所有采样点（x,y,z坐标）
问题：这些点在原始3D空间里是怎么分布的？
降维后：能不能把不同结构部分（胞体、不同分支）区分开？

运行：右键 Run 'single_neuron_demo'
"""
import os
import numpy as np
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D
from sklearn.decomposition import PCA
from sklearn.manifold import TSNE
import umap


def read_swc(file_path):
    """读取单个SWC文件，返回点数组: [id, type, x, y, z, r, pid]"""
    points = []
    with open(file_path, 'r') as f:
        for line in f:
            line = line.strip()
            if not line or line.startswith('#'):
                continue
            parts = line.split()
            if len(parts) < 7:
                continue
            points.append([float(p) for p in parts[:7]])
    return np.array(points)


def run_single_neuron(swc_path):
    print(f"分析神经元: {os.path.basename(swc_path)}")
    pts = read_swc(swc_path)
    xyz = pts[:, 2:5]   # 所有点的x,y,z坐标
    types = pts[:, 1]   # 点类型（1=胞体, 2=轴突, 3=树突）
    print(f"  总点数: {len(xyz)}")

    # 1. PCA降到2D
    Y_pca2d = PCA(n_components=2, random_state=42).fit_transform(xyz)
    # 2. t-SNE降到2D
    Y_tsne = TSNE(n_components=2, perplexity=30, random_state=42).fit_transform(xyz)
    # 3. UMAP降到2D
    Y_umap = umap.UMAP(n_neighbors=30, random_state=42).fit_transform(xyz)

    # 画图：2行2列
    fig = plt.figure(figsize=(14, 12))

    # 左上：原始3D点云
    ax1 = fig.add_subplot(2, 2, 1, projection='3d')
    ax1.scatter(xyz[:, 0], xyz[:, 1], xyz[:, 2],
                c=types, cmap='Set1', s=2, alpha=0.6)
    ax1.set_title('Original 3D Coordinates', fontsize=13, fontweight='bold')

    # 右上：PCA 2D
    ax2 = fig.add_subplot(2, 2, 2)
    ax2.scatter(Y_pca2d[:, 0], Y_pca2d[:, 1],
                c=types, cmap='Set1', s=2, alpha=0.6)
    ax2.set_title('PCA (2D)', fontsize=13, fontweight='bold')

    # 左下：t-SNE 2D
    ax3 = fig.add_subplot(2, 2, 3)
    ax3.scatter(Y_tsne[:, 0], Y_tsne[:, 1],
                c=types, cmap='Set1', s=2, alpha=0.6)
    ax3.set_title('t-SNE (2D)', fontsize=13, fontweight='bold')

    # 右下：UMAP 2D
    ax4 = fig.add_subplot(2, 2, 4)
    ax4.scatter(Y_umap[:, 0], Y_umap[:, 1],
                c=types, cmap='Set1', s=2, alpha=0.6)
    ax4.set_title('UMAP (2D)', fontsize=13, fontweight='bold')

    plt.suptitle(f'Single Neuron Point Cloud: {os.path.basename(swc_path)}',
                 fontsize=15, y=1.01)
    plt.tight_layout()
    out = 'single_neuron_demo.png'
    plt.savefig(out, dpi=150, bbox_inches='tight')
    print(f"  图已保存: {out}")
    plt.close()


if __name__ == '__main__':
    swc_dir = os.path.join(os.path.dirname(__file__), '..', 'swc_data')
    swc_dir = os.path.abspath(swc_dir)
    files = sorted([f for f in os.listdir(swc_dir) if f.endswith('.swc')])
    run_single_neuron(os.path.join(swc_dir, files[0]))
