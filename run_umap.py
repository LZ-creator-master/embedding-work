"""
run_umap.py —— UMAP 降维封装
"""

import umap
import config


def run_umap(X):
    """对高维数据 X 做 UMAP，返回 2 维坐标"""
    model = umap.UMAP(
        n_components=2,
        n_neighbors=config.UMAP_N_NEIGHBORS,
        min_dist=config.UMAP_MIN_DIST,
        random_state=config.UMAP_RANDOM_STATE,
    )
    Y = model.fit_transform(X)
    print(f"[UMAP] 完成，输出形状: {Y.shape}")
    return Y
