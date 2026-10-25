# 源码与验证说明

[← 返回首页](README.md) · [实验指南](docs/GUIDE.md)

## 公开范围

仓库发布了本地 `embedding work` 项目的实验源码、Markdown 文档和 Git 忽略配置。未包含原始数据、历史实验图片、PDF、压缩包、Python 缓存和嵌套 Git 历史。

神经元实验需要自行准备 `swc_data/`；其他实验可能需要联网获取数据或安装额外依赖。

## 验证状态

首次上传时，27 个 Python 文件通过语法解析检查。尚未完成全部实验的端到端验证，也没有发布锁定版本的环境文件。当前文档根据入口代码整理，具体边界见[实验指南](docs/GUIDE.md#limitations)。

本次首页和文档整理未改变算法、数据加载器或本地 PyCharm 项目文件。

## 上游来源

`sude_official/` 来自 [ZPGuiGroupWhu/sude](https://github.com/ZPGuiGroupWhu/sude)。Python 实现的安装来源见 [ZPGuiGroupWhu/SUDE-pkg](https://github.com/ZPGuiGroupWhu/SUDE-pkg)。保留上游作者声明；本仓库没有给第三方代码重新指定许可证。

## 文档设计参考

参考以下项目的公开 README 信息组织，内容按本仓库实际代码重新撰写：

| 项目 | 借鉴方式 |
| --- | --- |
| [PyTorch](https://github.com/pytorch/pytorch) | 清晰的标题区、导航及组件概览 |
| [scikit-learn](https://github.com/scikit-learn/scikit-learn) | 安装、依赖、文档与反馈入口分区 |
| [UMAP](https://github.com/lmcinnes/umap) | 简短用法、参数说明和论文来源 |

未复制其项目标志、测试状态或许可证徽章。首页徽章仅用于标识技术、研究用途以及本仓库真实 Star 数。
