# 流形降维对比实验框架

## 目录结构
```
embedding work/
├── config.py        # 参数配置（改困惑度、近邻数等）
├── data_loader.py   # 【你自己改这里】写数据加载代码
├── run_tsne.py      # t-SNE 封装（不用动）
├── run_umap.py      # UMAP 封装（不用动）
├── visualizer.py    # 可视化（不用动）
└── main.py         # 主入口（右键运行）
```

## 怎么跑
1. 先改 `data_loader.py` 里的 `load_data()`，加载你自己的数据
2. 改 `config.py` 里的 `DATASET_LABEL`，写个数据集名字
3. 右键 `main.py` → Run
4. 看弹出的对比图，同时生成 `embedding_compare.png`

## 怎么导入 Wine 数据集（UCI id=109）
```python
# 先在终端跑：pip install ucimlrepo
from ucimlrepo import fetch_ucirepo
wine = fetch_ucirepo(id=109)
X = wine.data.features.values
y = wine.data.targets.values.ravel()
```

## 怎么导入 Dermatology 数据集（UCI id=33）
```python
# 这个数据集有缺失值（?），要先填一下
from ucimlrepo import fetch_ucirepo
import pandas as pd
import numpy as np
derm = fetch_ucirepo(id=33)
X = pd.DataFrame(derm.data.features.values).replace('?', np.nan).apply(pd.to_numeric).fillna(0).values
y = derm.data.targets.values.ravel()
```

## 调参建议
- **样本少（<200）**：t-SNE 困惑度 5~15，UMAP 近邻数 5~10
- **样本中（200~2000）**：t-SNE 困惑度 20~30，UMAP 近邻数 10~20
- **样本多（>2000）**：t-SNE 困惑度 30~50，UMAP 近邻数 20~50
