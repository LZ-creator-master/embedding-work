# SUDE 对比实验说明

本文件夹用于 **SUDE 与经典流形算法（t-SNE / UMAP）的对比实验**，与项目其他部分完全隔离。

## 1. 文件夹内容

| 文件 | 作用 |
|---|---|
| `config.py` | 全局配置：数据集选择、算法超参数（只需改这里） |
| `data_loader.py` | 数据加载器：支持 UCI 内置数据集 + 本地 CSV 文件 |
| `run_compare.py` | 主程序：生成 2x2 对比图（3D原始 + t-SNE + UMAP + SUDE） |
| `sude_compare.png` | 输出图片 |

## 2. 运行方法

在 PyCharm 中打开 `run_compare.py`，右键 **Run 'run_compare'**。

输出的图片包含四个子图：
- 左上：原始高维数据的 3D 结构（PCA 降到 3 维，展示数据本来分布）
- 右上：t-SNE 2D
- 左下：UMAP 2D
- 右下：SUDE 2D

## 3. 如何切换数据集

### 方法 A：使用 UCI 内置数据集（推荐，自动下载）

打开 `config.py`，修改 `DATASET_NAME`：

```python
DATASET_NAME = 'wine'           # 可选: 'wine' / 'dermatology' / 'breast_cancer' / 'iris' / 'digits'
```

首次运行会自动联网从 UCI 仓库下载，之后无需再下载。

### 方法 B：使用你自己的数据文件（CSV）

打开 `config.py`，填三行：

```python
CSV_PATH = r'D:\my_data\mydata.csv'   # 你的文件绝对路径
CSV_LABEL_COL = -1                     # 标签列: -1=最后一列, 0=第一列
CSV_DELIMITER = ','                    # 分隔符: ',' 或 ' ' 或 '\t'
```

文件格式要求：每行一个样本，最后一列（或指定列）是类别标签，其余列是特征。

### 常见问题

- **换数据集后出图没变？** 检查 `config.py` 里 `DATASET_NAME` 是否已改，确认后重新 Run。
- **数据太大跑得慢？** `run_compare.py` 默认截取前 3000 个样本做演示。
- **SUDE 参数怎么调？** `SUDE_N_NEIGHBORS`（近邻数，小数据集 10，大数据集 20-50）、`SUDE_INIT`（'le' 推荐）。

## 4. SUDE 算法简介

SUDE（Sampling-based scalable manifold learning for Uniform and Discriminative Embedding）
来自论文：Peng et al., *Nature Machine Intelligence*, 2025.

三阶段流程：
1. **采样（PPS）**：从原始数据中选取均匀的地标点（landmarks）
2. **学习**：用地标点学习低维骨架（全局结构）
3. **纳入（CLLE）**：用约束局部线性嵌入把非地标点纳入低维空间

官方代码仓库：https://github.com/ZPGuiGroupWhu/sude
