"""
main.py —— 主入口
=================
运行方式：右键 Run 'main'
流程：加载数据 → t-SNE → UMAP → 画对比图
"""

from data_loader import load_data
from run_tsne import run_tsne
from run_umap import run_umap
from visualizer import plot_compare


def main():
    print("=" * 50)
    print("流形降维对比: t-SNE vs UMAP")
    print("=" * 50)

    # 1. 加载数据（你自己在 data_loader.py 里写好）
    X, y = load_data()

    # 2. 跑两个算法
    Y_tsne = run_tsne(X)
    Y_umap = run_umap(X)

    # 3. 可视化对比
    plot_compare(Y_tsne, Y_umap, y)

    print("\n完成！")


if __name__ == '__main__':
    main()
