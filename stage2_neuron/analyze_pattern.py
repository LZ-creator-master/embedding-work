import os
import numpy as np
from sklearn.decomposition import PCA
from sklearn.manifold import TSNE
from sklearn.metrics import silhouette_score
import umap

def read_swc(fp):
    pts = []
    with open(fp) as f:
        for line in f:
            line = line.strip()
            if not line or line.startswith('#'): continue
            p = line.split()
            if len(p) < 7: continue
            pts.append([float(x) for x in p[:7]])
    return np.array(pts)

swc_dir = os.path.join(os.path.dirname(__file__), '..', 'swc_data')
swc_dir = os.path.abspath(swc_dir)
files = sorted([f for f in os.listdir(swc_dir) if f.endswith('.swc')])

print(f"{'神经元文件名':<25} {'总点数':>6} {'胞体数':>5} {'轴突数':>6} {'PCA分':>7} {'tSNE分':>7} {'UMAP分':>7}")
print("-" * 80)

data = []
for f in files:
    pts = read_swc(os.path.join(swc_dir, f))
    xyz = pts[:, 2:5]
    types = pts[:, 1].astype(int)
    n_soma = (types == 1).sum()
    n_axon = (types == 2).sum()

    mask = (types == 1) | (types == 2)
    X = xyz[mask]
    y = types[mask]
    if len(np.unique(y)) < 2:
        continue

    Y_pca = PCA(n_components=2, random_state=42).fit_transform(X)
    s_pca = silhouette_score(Y_pca, y)

    perp = min(30, max(5, len(X)//100))
    Y_tsne = TSNE(n_components=2, perplexity=perp, random_state=42).fit_transform(X)
    s_tsne = silhouette_score(Y_tsne, y)

    n_neighbors = min(30, max(5, len(X)//100))
    Y_umap = umap.UMAP(n_neighbors=n_neighbors, random_state=42).fit_transform(X)
    s_umap = silhouette_score(Y_umap, y)

    data.append([f, len(pts), n_soma, n_axon, s_pca, s_tsne, s_umap])
    print(f"{f:<25} {len(pts):>6} {n_soma:>5} {n_axon:>6} {s_pca:>7.3f} {s_tsne:>7.3f} {s_umap:>7.3f}")

data = np.array(data)
print()
print("=== 规律总结 ===")
# 找t-SNE和UMAP都最差的5个
worst_tsne = sorted(data, key=lambda x: float(x[5]))[:5]
worst_umap = sorted(data, key=lambda x: float(x[6]))[:5]
best_tsne = sorted(data, key=lambda x: float(x[5]), reverse=True)[:5]
best_umap = sorted(data, key=lambda x: float(x[6]), reverse=True)[:5]

print("\n表现最差的5个（t-SNE）:")
for d in worst_tsne:
    print(f"  {d[0]}: 点数={d[1]}, tSNE={float(d[5]):.3f}")

print("\n表现最好的5个（t-SNE）:")
for d in best_tsne:
    print(f"  {d[0]}: 点数={d[1]}, tSNE={float(d[5]):.3f}")
