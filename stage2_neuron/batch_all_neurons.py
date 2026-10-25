"""
batch_all_neurons.py —— 批量跑50个神经元，汇总对比
====================================================
遍历swc_data文件夹里所有SWC文件，每个神经元跑PCA/t-SNE/UMAP降维，
计算"胞体与轴突在降维空间的分离程度"（轮廓系数），
最后画一张柱状图对比50个神经元在三种方法下的表现。

运行：右键 Run 'batch_all_neurons'
"""
import os
import numpy as np
import matplotlib.pyplot as plt
from sklearn.decomposition import PCA
from sklearn.manifold import TSNE
from sklearn.metrics import silhouette_score
import umap


def read_swc(file_path):
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


def eval_one_neuron(swc_path):
    """对单个神经元跑三种降维，返回三种方法的轮廓系数"""
    pts = read_swc(swc_path)
    xyz = pts[:, 2:5]
    types = pts[:, 1].astype(int)

    # 只保留胞体(1)和轴突(2)两类来算轮廓系数
    mask = (types == 1) | (types == 2)
    if len(np.unique(types[mask])) < 2:
        return None

    X = xyz[mask]
    y = types[mask]

    # PCA 2D
    Y_pca = PCA(n_components=2, random_state=42).fit_transform(X)
    score_pca = silhouette_score(Y_pca, y)

    # t-SNE 2D
    perp = min(30, max(5, len(X) // 100))
    Y_tsne = TSNE(n_components=2, perplexity=perp, random_state=42).fit_transform(X)
    score_tsne = silhouette_score(Y_tsne, y)

    # UMAP 2D
    n_neighbors = min(30, max(5, len(X) // 100))
    Y_umap = umap.UMAP(n_neighbors=n_neighbors, random_state=42).fit_transform(X)
    score_umap = silhouette_score(Y_umap, y)

    return score_pca, score_tsne, score_umap


def main():
    swc_dir = os.path.join(os.path.dirname(__file__), '..', 'swc_data')
    swc_dir = os.path.abspath(swc_dir)
    files = sorted([f for f in os.listdir(swc_dir) if f.endswith('.swc')])

    print(f"共 {len(files)} 个神经元，开始批量处理...")

    results = []
    names = []
    for i, f in enumerate(files):
        print(f"  [{i+1}/{len(files)}] {f}...", end=" ")
        scores = eval_one_neuron(os.path.join(swc_dir, f))
        if scores is not None:
            results.append(scores)
            names.append(f.replace('.swc', ''))
            print(f"PCA={scores[0]:.3f}, t-SNE={scores[1]:.3f}, UMAP={scores[2]:.3f}")
        else:
            print("跳过(类别不足)")

    results = np.array(results)
    print(f"\n成功处理 {len(results)} 个神经元")

    # 画汇总柱状图
    fig, ax = plt.subplots(figsize=(16, 6))
    x = np.arange(len(names))
    width = 0.25

    ax.bar(x - width, results[:, 0], width, label='PCA', color='#4C72B0')
    ax.bar(x, results[:, 1], width, label='t-SNE', color='#DD8452')
    ax.bar(x + width, results[:, 2], width, label='UMAP', color='#55A868')

    ax.set_xlabel('Neuron ID')
    ax.set_ylabel('Silhouette Score (higher = better separation)')
    ax.set_title('50 Neurons: Somatic vs Axonal Separation after Dimensionality Reduction')
    ax.set_xticks(x)
    ax.set_xticklabels(names, rotation=90, fontsize=7)
    ax.legend()
    ax.axhline(y=0, color='gray', linestyle='--', linewidth=0.5)

    plt.tight_layout()
    out = 'batch_summary.png'
    plt.savefig(out, dpi=150, bbox_inches='tight')
    print(f"汇总图已保存: {out}")

    # 打印平均值
    print(f"\n平均分离程度：")
    print(f"  PCA:    {results[:, 0].mean():.3f}")
    print(f"  t-SNE:  {results[:, 1].mean():.3f}")
    print(f"  UMAP:   {results[:, 2].mean():.3f}")

    plt.close()


if __name__ == '__main__':
    main()
