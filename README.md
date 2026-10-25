<div align="center">

# Embedding Work

### 从高维数据到可视化结构

面向流形学习与降维实验的 Python 工作台<br>
**t-SNE · UMAP · SUDE · 神经元形态分析**

<p>
<img alt="Python project" src="https://img.shields.io/badge/Python-3776AB?style=flat-square&amp;logo=python&amp;logoColor=white">
<img alt="Manifold learning" src="https://img.shields.io/badge/Manifold-Learning-0F766E?style=flat-square">
<img alt="Research experiments" src="https://img.shields.io/badge/Research-Experiments-6366F1?style=flat-square">
<a href="https://github.com/LZ-creator-master/embedding-work/stargazers"><img alt="GitHub stars" src="https://img.shields.io/github/stars/LZ-creator-master/embedding-work?style=flat-square&amp;color=0F766E"></a>
</p>

<a href="#overview">项目概览</a> ·
<a href="#quickstart">快速开始</a> ·
<a href="#datasets">数据集</a> ·
<a href="docs/GUIDE.md">实验指南</a> ·
<a href="PROJECT_MAP.md">目录导航</a>

</div>

---

<a id="overview"></a>

## 🧭 一个项目，三条实验路线

在同一份数据上比较低维表示，观察类别分布、局部邻域与形态结构。适合学习算法、调参观察和准备实验汇报。

| 实验路线 | 比较内容 | 从这里开始 |
| :--- | :--- | :--- |
| **01 · 经典降维** | t-SNE 与 UMAP 并排散点图 | [main.py](main.py) · [配置](config.py) |
| **02 · 神经元形态** | 原始 3D、PCA、t-SNE、UMAP；绘制父子节点连线 | [批量绘图](stage2_neuron/batch_plot_all.py) |
| **03 · SUDE 对比** | PCA 3D 投影、t-SNE、UMAP、SUDE 四宫格 | [运行入口](sude_work/run_compare.py) · [指南](sude_work/README.md) |

> [!NOTE]
> 当前仓库以实验源码和文档为主。神经元 SWC 数据、历史结果图、PDF 和压缩包未随仓库提供。PCA 3D 图是高维数据的投影；散点图用于观察，不能单独证明某种算法更优。

<a id="quickstart"></a>

## 🚀 快速开始

**先用 Iris 跑通流程，再换成你的研究数据。** Iris 随 scikit-learn 提供，运行时无需下载数据。

### 1. 获取项目并安装基础依赖

在 PyCharm Terminal 或终端执行：

```bash
git clone https://github.com/LZ-creator-master/embedding-work.git
cd embedding-work
python -m pip install numpy pandas matplotlib "scikit-learn>=1.5" umap-learn ucimlrepo
```

建议使用独立虚拟环境，并确认终端的 Python 与 PyCharm 项目解释器一致。以上为基础实验的依赖起点，尚未提供锁定版本的环境文件。

### 2. 修改根目录的 config.py

```python
DATASET_NAME = 'iris_test'
DATASET_LABEL = 'Iris'
```

仓库原配置选择的是 `pbmc3k`；首次体验请明确改成上面的 Iris 配置。

### 3. 运行

```bash
python main.py
```

程序加载数据，计算 t-SNE 和 UMAP，显示对比图，并在**当前工作目录**保存 `embedding_compare.png`。在 PyCharm 中也可以右键 `main.py` → **Run**。

**下一步：** [换数据集与调参](docs/GUIDE.md) · [运行 SUDE](sude_work/README.md) · [准备神经元数据](docs/GUIDE.md#neuron)

<a id="datasets"></a>

## 🗂️ 数据集入口

根目录通过 `config.py` 的 `DATASET_NAME` 选择数据，注册表在 [datasets/__init__.py](datasets/__init__.py)。

| 配置名称 | 当前实际加载的数据 | 获取方式 |
| :--- | :--- | :--- |
| `iris_test` | Iris | scikit-learn 内置 |
| `breast_cancer` | Breast Cancer | scikit-learn 内置 |
| `mfeat` | **Digits 替代数据**，并非原始 Mfeat | scikit-learn 内置 |
| `wine` / `dermatology` | Wine / Dermatology | UCI，需网络 |
| `spambase` / `dry_bean` | Spambase / Dry Bean | UCI，需网络 |
| `mnist` / `fmnist` | MNIST / Fashion-MNIST | OpenML，需下载或已有缓存 |
| `pbmc3k` | PBMC3k 单细胞数据 | Scanpy，需额外依赖和数据 |

**PBMC 标签说明：** 当前代码用 K-means 生成 8 个演示簇，不是已验证的细胞类型注释。样本数和特征数以实际加载结果为准。

**自定义数据：** SUDE 模块提供本地 CSV 入口；基础模块需要新增并注册数据加载器。[查看操作方法 →](docs/GUIDE.md#custom-data)

## 🎛️ 常用配置

| 目标 | 修改位置 | 参数 |
| :--- | :--- | :--- |
| 切换基础实验数据 | 根目录 `config.py` | `DATASET_NAME`、`DATASET_LABEL` |
| 调整 t-SNE | 对应实验的 `config.py` | `TSNE_PERPLEXITY`、`TSNE_MAX_ITER` |
| 调整 UMAP | 对应实验的 `config.py` | `UMAP_N_NEIGHBORS`、`UMAP_MIN_DIST` |
| 调整 SUDE | `sude_work/config.py` | `SUDE_N_NEIGHBORS`、`SUDE_INIT`、`SUDE_MAX_ITER` |
| 导入 CSV | `sude_work/config.py` | `CSV_PATH`、`CSV_LABEL_COL` |

比较算法时，请记录数据预处理、参数、随机种子和环境版本。当前基础入口没有统一标准化或自动抽样步骤；SUDE 对比入口会截取前 3000 个样本。

## 📚 文档导航

| 文档 | 你可以找到什么 |
| :--- | :--- |
| [实验指南](docs/GUIDE.md) | 环境、数据导入、神经元实验、调参与已知限制 |
| [项目地图](PROJECT_MAP.md) | 每个目录和主要脚本的用途 |
| [SUDE 对比指南](sude_work/README.md) | 安装、四宫格输出与 CSV 输入要求 |
| [源码与验证说明](SOURCE_UPLOAD.md) | 发布范围、验证状态和上游来源 |

## 💬 常见问题

<details>
<summary><b>为什么提示找不到 umap 或 sude？</b></summary>

UMAP 的安装包名是 `umap-learn`，导入名是 `umap`。SUDE 需要额外安装；参见 [SUDE 指南](sude_work/README.md)。安装命令应在运行项目的同一 Python 环境中执行。

</details>

<details>
<summary><b>为什么切换数据后标题没变，或者找不到生成的图？</b></summary>

基础实验需同时更新 `DATASET_NAME` 与 `DATASET_LABEL`。输出路径相对于当前工作目录；在 PyCharm 的运行配置中检查 Working directory。

</details>

<details>
<summary><b>为什么大数据集运行很慢？</b></summary>

基础 `main.py` 不会自动截取样本。先用 Iris 验证流程，再明确安排抽样、预处理和实验规模。UMAP 首次运行还可能包含 JIT 编译开销。

</details>

<details>
<summary><b>这些脚本是否已经全部验证可运行？</b></summary>

首次上传时 27 个 Python 文件通过语法解析检查，但尚未完成全部数据集、依赖版本和实验流程的端到端验证。具体限制见 [实验指南](docs/GUIDE.md#limitations)。

</details>

## 🤝 反馈与参考

欢迎通过 [Issues](https://github.com/LZ-creator-master/embedding-work/issues) 反馈问题，请附上运行入口、数据集、参数、依赖版本和完整错误信息。

- [scikit-learn](https://github.com/scikit-learn/scikit-learn) — PCA、t-SNE 等基础实现。
- [UMAP](https://github.com/lmcinnes/umap) — UMAP 实现与文档。
- [SUDE 原始仓库](https://github.com/ZPGuiGroupWhu/sude) · [SUDE Python 包](https://github.com/ZPGuiGroupWhu/SUDE-pkg) — 上游实现。
- Peng et al., *Sampling-enabled scalable manifold learning unveils the discriminative cluster structure of high-dimensional data*. [论文](https://doi.org/10.1038/s42256-025-01112-9)。

本仓库尚未声明统一开源许可证；第三方代码保留其原始作者声明。引用算法或复用上游实现时，请查看对应项目的引用与许可说明。

---

<p align="center"><sub>Embedding Work · Explore structure, compare embeddings.</sub></p>
