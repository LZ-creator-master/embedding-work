# 项目地图

[← 返回首页](README.md) · [实验指南](docs/GUIDE.md)

## 按任务找入口

| 想做什么 | 运行入口 | 配置或数据位置 |
| --- | --- | --- |
| 比较 t-SNE / UMAP | [main.py](main.py) | [config.py](config.py) |
| 列出基础实验数据集 | [data_loader.py](data_loader.py) | [数据注册表](datasets/__init__.py) |
| 批量绘制神经元结构 | [batch_plot_all.py](stage2_neuron/batch_plot_all.py) | 自行准备根目录 `swc_data/` |
| 比较 SUDE / t-SNE / UMAP | [run_compare.py](sude_work/run_compare.py) | [sude_work/config.py](sude_work/config.py) |
| 汇总多个数据集 | [summary_table.py](summary_table.py) | 脚本内 `DATASETS_TO_RUN` |

## 目录职责

| 路径 | 内容 | 说明 |
| --- | --- | --- |
| [datasets/](datasets/) | 数据加载器与注册表 | 10 个注册入口，实际数据来源见首页 |
| [stage2_neuron/](stage2_neuron/) | 神经元演示、批量绘图和分析 | 需要单独准备 SWC 数据 |
| [sude_work/](sude_work/) | SUDE 四宫格对比实验 | 独立配置；支持本地 CSV |
| [sude_official/](sude_official/) | 上游参考源码和说明 | MATLAB、R 等参考实现；保留来源声明 |
| [sude_official/sude_py/](sude_official/sude_py/) | Python 包的上游说明 | 本目录不是完整的可安装 Python 包 |
| [docs/](docs/) | 实验使用指南 | 安装、数据、限制与反馈 |

## 根目录文件

| 文件 | 职责 |
| --- | --- |
| [config.py](config.py) | 基础实验的数据集、算法参数和绘图设置 |
| [data_loader.py](data_loader.py) | 按注册名称加载数据 |
| [run_tsne.py](run_tsne.py) / [run_umap.py](run_umap.py) | 算法封装函数，由入口调用；单独执行不会启动完整实验 |
| [visualizer.py](visualizer.py) | 并排绘图及保存 |
| [plot_3d.py](plot_3d.py) | 3D 可视化辅助脚本 |
| [summary_table.py](summary_table.py) | 多数据集对比图 |
| [generate_report_pdf.py](generate_report_pdf.py) | 报告生成脚本，包含需调整的本机路径 |
| [SOURCE_UPLOAD.md](SOURCE_UPLOAD.md) | 公开范围与验证说明 |

## 数据与输出文件

以下为运行时路径或本地资料，**不是仓库已附带的内容**：

| 路径或文件 | 用途 |
| --- | --- |
| `swc_data/` | 用户准备的神经元原始数据 |
| `data/` | 部分数据下载缓存，实际位置取决于加载器 |
| `embedding_compare.png` | 基础实验输出，相对于运行工作目录 |
| `sude_compare.png` | SUDE 实验输出，相对于运行工作目录 |
| `stage2_neuron/output_figures/` | 神经元批量结果 |
| PDF、ZIP 和历史实验图片 | 本地历史资料，未随源码发布 |

**配置不要混用：** 基础实验修改根目录 `config.py`；SUDE 实验修改 `sude_work/config.py`。自定义 CSV 入口仅在后者提供。
