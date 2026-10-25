"""
run_tsne.py —— t-SNE 降维封装
"""

from sklearn.manifold import TSNE
import config


def run_tsne(X):
    """对高维数据 X 做 t-SNE，返回 2 维坐标"""
    model = TSNE(
        n_components=2,
        perplexity=config.TSNE_PERPLEXITY,
        max_iter=config.TSNE_MAX_ITER,
        random_state=config.TSNE_RANDOM_STATE,
    )
    Y = model.fit_transform(X)
    print(f"[t-SNE] 完成，输出形状: {Y.shape}")
    return Y
