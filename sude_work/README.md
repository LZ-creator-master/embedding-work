# SUDE 对比实验

[← 返回项目首页](../README.md) · [完整实验指南](../docs/GUIDE.md)

将同一份数据分别转换为 **PCA 3D、t-SNE 2D、UMAP 2D 和 SUDE 2D**，生成四宫格对比图。

## 开始运行

先按[首页](../README.md#quickstart)安装基础依赖，再安装上游 SUDE 包：

```bash
python -m pip install sude
python -c "from sude import SUDE; print(SUDE)"
cd sude_work
python run_compare.py
```

以上从仓库根目录执行。默认选择 Wine，数据加载需要访问 UCI。程序保存 `sude_compare.png` 后关闭图窗，请在工作目录中打开结果图。

安装方法参考 [SUDE Python 上游](https://github.com/ZPGuiGroupWhu/SUDE-pkg)。本仓库的 `sude_official/sude_py/` 只保留上游说明，不等于已安装该 Python 包。

## 文件与输出

| 文件 | 用途 |
| --- | --- |
| [config.py](config.py) | 数据集、CSV 路径、算法参数与绘图配置 |
| [data_loader.py](data_loader.py) | 加载 UCI 或本地数值数据 |
| [run_compare.py](run_compare.py) | 运行四组表示并保存图像 |

| 图的位置 | 表示 |
| --- | --- |
| 左上 | PCA 降到 3 维的投影，不是高维空间的完整原貌 |
| 右上 | t-SNE 2D |
| 左下 | UMAP 2D |
| 右下 | SUDE 2D |

当前入口超过 3000 个样本时会截取前 3000 个。结果图用于探索与对比，不构成统一预处理下的完整算法评测。

## 内置数据

修改本目录的 `config.py`：

```python
DATASET_NAME = 'wine'
CSV_PATH = ''
```

当前注册名称为 `wine`、`dermatology`、`breast_cancer`、`iris`、`digits`。此处加载器通过 UCI 获取数据，与根目录同名加载器的实现不一定相同；不要假定所有数据已缓存或无需联网。

<a id="csv"></a>

## 本地 CSV

准备**无表头、全数值**的二维文件，每行一个样本，最后一列作为数值标签：

```python
CSV_PATH = r'D:\my_data\mydata.csv'
CSV_LABEL_COL = -1
CSV_DELIMITER = ','
```

`CSV_PATH` 非空时优先使用本地文件。请在导入前处理缺失值、字符串标签和非数值列；当前 CSV 读取使用 `numpy.loadtxt`。

TXT 可通过分隔符配置读取。NPY 路径也有实现，但当前非末列标签切片存在限制，建议使用末列标签并核对输出特征数。

## 参数速查

| 参数 | 当前配置 | 作用 |
| --- | --- | --- |
| `TSNE_PERPLEXITY` | 30 | t-SNE 邻域尺度，须小于样本数 |
| `UMAP_N_NEIGHBORS` | 20 | UMAP 邻域规模 |
| `UMAP_MIN_DIST` | 0.1 | UMAP 低维紧密程度 |
| `SUDE_N_NEIGHBORS` | 10 | SUDE 近邻参数 |
| `SUDE_INIT` | `le` | SUDE 初始化方式 |
| `SUDE_MAX_ITER` | 50 | SUDE 迭代次数 |
| `ORIG_3D_METHOD` | `pca` | 左上角展示方式 |

这些是仓库当前设置，不是所有数据集的最优参数。运行前注意缺失值、标签类型、标准化策略，以及图例颜色与散点映射可能不一致的问题，详见[已知限制](../docs/GUIDE.md#limitations)。

## 算法来源

- [SUDE 原始研究代码](https://github.com/ZPGuiGroupWhu/sude)
- [SUDE Python 包](https://github.com/ZPGuiGroupWhu/SUDE-pkg)
- Peng et al., *Sampling-enabled scalable manifold learning unveils the discriminative cluster structure of high-dimensional data*, Nature Machine Intelligence (2025). [论文](https://doi.org/10.1038/s42256-025-01112-9)。

本目录是实验对比入口；SUDE 算法由其上游实现提供。
