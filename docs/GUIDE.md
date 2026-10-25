# 实验指南

[← 返回首页](../README.md) · [项目地图](../PROJECT_MAP.md) · [SUDE 指南](../sude_work/README.md)

## 环境与安装

在 PyCharm 中创建项目虚拟环境，使用该环境的 Terminal 安装依赖。也可用 `python -m venv .venv` 建立环境，再在 PyCharm 中选择对应解释器。

```bash
python -m pip install numpy pandas matplotlib "scikit-learn>=1.5" umap-learn ucimlrepo
```

此列表按现有导入和调用整理，并非经过完整验证的锁定环境。源码使用 `TSNE(max_iter=...)`，较旧的 scikit-learn 可能不接受这个参数。请保留自己的环境版本记录。

| 实验 | 额外安装 | 说明 |
| --- | --- | --- |
| PBMC3k | `python -m pip install scanpy` | 数据下载及稀疏矩阵转稠密可能占用较多内存 |
| SUDE | `python -m pip install sude` | 安装后核对 `from sude import SUDE` 是否可用 |
| PDF 报告 | `python -m pip install reportlab` | 脚本还包含本机 Windows 字体和输出路径，需要调整 |

## 基础实验：换数据、再调参

在仓库根目录的 `config.py` 中选择数据集，例如：

```python
DATASET_NAME = 'wine'
DATASET_LABEL = 'Wine'
TSNE_PERPLEXITY = 30
UMAP_N_NEIGHBORS = 20
UMAP_MIN_DIST = 0.1
```

在仓库根目录运行：

```bash
python data_loader.py
python main.py
```

第一条命令列出可选数据集；第二条运行对比实验。只更换内置数据集时，不需要改写 `data_loader.py`。

| 参数 | 作用 | 使用要点 |
| --- | --- | --- |
| `TSNE_PERPLEXITY` | 控制 t-SNE 邻域尺度 | 必须小于样本数；比较不同设置时记录取值 |
| `TSNE_MAX_ITER` | t-SNE 优化迭代次数 | 增加迭代可能增加耗时 |
| `UMAP_N_NEIGHBORS` | UMAP 邻域规模 | 结合样本规模设置，比较局部与较大尺度结构 |
| `UMAP_MIN_DIST` | 控制低维点的紧密程度 | 簇更紧不等于分类效果更好 |
| 随机种子 | 控制随机过程 | 固定种子便于比较；环境变化仍可能影响结果 |

<a id="custom-data"></a>

## 自定义数据

### 基础模块：注册加载器

1. 在 `datasets/` 下新建 Python 文件，实现 `load()`，返回 `X, y`。
2. `X` 为二维数值数组，形状为 `(样本数, 特征数)`；`y` 为一维标签数组。
3. 在 `datasets/__init__.py` 中导入模块，并加入 `REGISTRY`。
4. 将根目录 `config.py` 的 `DATASET_NAME` 改为注册名称。

基础绘图直接把 `y` 传给 Matplotlib 的颜色参数，字符串类别应先编码为整数。请自行处理缺失值，并根据研究目的决定是否标准化。

### SUDE 模块：使用 CSV

详见 [SUDE 指南](../sude_work/README.md#csv)。这里的 `CSV_PATH` 配置只属于 `sude_work/config.py`；根目录配置没有这个选项。

<a id="neuron"></a>

## 神经元形态实验

先在仓库根目录创建 `swc_data/`，放入你自己的 `.swc` 文件，再执行：

```bash
python stage2_neuron/batch_plot_all.py
```

脚本读取 SWC 的坐标、节点类型和父节点关系，分别绘制原始 3D、PCA 2D、t-SNE 2D、UMAP 2D，并在每个视图中保留父子节点连线。

结果保存到 `stage2_neuron/output_figures/`。脚本处理目录内所有扩展名为 `.swc` 的文件，数量并不固定为 50。仓库未附带原始 SWC 数据。

## 汇总图与报告

| 脚本 | 用途 | 运行前检查 |
| --- | --- | --- |
| `plot_3d.py` | 补充 3D 可视化 | 数据与绘图配置 |
| `summary_table.py` | 多数据集对比大图 | 脚本中的 `DATASETS_TO_RUN`；其中可能包含需要额外依赖的数据 |
| `generate_report_pdf.py` | 生成实验报告 | 本地字体、绝对路径、静态报告内容与当前实验是否一致 |

这些辅助脚本保留了原实验环境的设置，使用前应阅读脚本，而不是假定下载后均可直接运行。

<a id="limitations"></a>

## 当前实现需要留意的地方

- **验证范围：** 首次上传时通过了 27 个 Python 文件的语法检查；未完成所有依赖组合和数据集的端到端验证。
- **数据预处理：** 基础入口没有统一标准化或抽样层。根目录 Dermatology 加载器会填补缺失值，SUDE 加载器没有同样的统一处理。
- **数据命名：** `mfeat` 实际调用 scikit-learn 的 Digits；不要把结果标成原始 Mfeat。
- **PBMC3k：** 标签由 K-means 生成；不是细胞类型真值。当前稠密矩阵分支仍调用 `toarray()`，遇到稠密输入时可能报错。
- **字符串标签：** 部分加载器可能返回字符串或 object 类型，当前绘图和编码逻辑没有覆盖所有情况，需要检查。
- **样本上限：** SUDE 入口仅取前 3000 个样本；基础入口没有这一限制。顺序截取也可能改变类别比例。
- **SUDE 本地 NPY：** 非末列标签时，当前实现只保留标签列之前的特征；使用末列标签或自行核对切片。
- **SUDE 图例：** 当前图例颜色与散点颜色的映射方式不同，可能不一致；正式汇报前需核对。
- **图像解释：** PCA 3D 是投影；二维分簇、簇间距离和簇大小不应直接当作算法质量结论。

这些条目描述现有代码的边界。本次文档整理不改变算法或数据加载行为。

## 反馈一个可复现的问题

在 [Issues](https://github.com/LZ-creator-master/embedding-work/issues) 中提供运行脚本、数据集名称、关键参数、Python/依赖版本、完整报错，以及是否使用了自定义预处理。
