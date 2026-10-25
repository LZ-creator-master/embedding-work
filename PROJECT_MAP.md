# 项目地图（PROJECT MAP）
# ============================================================
# 本文件说明每个文件夹/文件的作用，方便快速找到对应代码
# 代码运行不需要本文件，只是导览用
# ============================================================

embedding work/
│
├── 📁 data/                  [数据缓存] 自动下载的数据集缓存（pbmc3k等）
│
├── 📁 datasets/              [阶段一：数据集注册]
│   ├── __init__.py           数据集注册表（告诉config有哪些数据集可选）
│   ├── wine.py               UCI Wine数据集（3类，13维，178样本）
│   ├── dermatology.py        UCI 皮肤病数据集（6类，34维）
│   ├── breast_cancer.py       UCI 乳腺癌数据集（2类）
│   ├── mfeat.py              UCI 多特征数据集（10类）
│   ├── spambase.py           UCI 垃圾邮件数据集（2类，57维）
│   ├── dry_bean.py           UCI 干豆数据集（大样本）
│   ├── mnist.py              MNIST手写数字（10类，784维）
│   ├── fmnist.py             Fashion-MNIST服饰（10类，784维）
│   ├── pbmc3k.py             PBMC3k单细胞数据
│   └── iris_test.py          Iris鸢尾花（测试用小数据集）
│
├── 📁 stage2_neuron/          [阶段二：神经元形态学实验]
│   ├── single_neuron_demo.py  单个神经元点云降维demo
│   ├── batch_plot_all.py      批量跑50个神经元，出黑白连线版图
│   ├── analyze_pattern.py     分析神经元形态与降维效果的关系
│   ├── output_figures/         50张神经元输出图
│   └── 神经元降维对比图_50张.zip  打包好的结果（已交付）
│
├── 📁 sude_work/              [阶段三：SUDE新算法对比实验]
│   ├── run_compare.py          主程序：2x2四宫格对比图（3D+t-SNE+UMAP+SUDE）
│   ├── config.py              配置：切换数据集、调SUDE参数
│   ├── data_loader.py          数据加载（UCI自动下载+本地CSV）
│   ├── README.md               使用说明
│   └── sude_compare.png        Wine测试结果图
│
├── 📁 sude_official/          [参考：SUDE官方源码（不用改）]
│   ├── sude_py/               Python版官方代码
│   ├── sude_mat/              MATLAB版官方代码
│   ├── ECG/                   心电图应用示例
│   └── scRNA-seq/             单细胞应用示例
│
├── 📁 swc_data/               [原始数据] 50个.swc神经元文件
│
├── 📄 main.py                [阶段一入口] 选一个数据集，跑t-SNE+UMAP对比
├── 📄 config.py               [阶段一配置] 改这里切换数据集、调参数
├── 📄 data_loader.py           [阶段一] 数据加载器
├── 📄 run_tsne.py             [阶段一] 单独跑t-SNE
├── 📄 run_umap.py             [阶段一] 单独跑UMAP
├── 📄 visualizer.py            [阶段一] 画图工具函数
├── 📄 plot_3d.py              [阶段一] 画3D原始结构图
├── 📄 summary_table.py         [阶段一] 生成多数据集汇总对比表
├── 📄 generate_report_pdf.py   [阶段一] 生成汇报PDF
├── 📄 README.md               项目总说明
└── 📄 流形学习实验汇报.pdf     [交付物] 最终汇报文档


# ============================================================
# 快速入口：想跑哪个实验？
# ============================================================
# 1. 经典流形算法对比（t-SNE vs UMAP）
#    → 打开 main.py，改 config.py 里的 DATASET_NAME
#
# 2. 神经元形态降维实验
#    → 打开 stage2_neuron/batch_plot_all.py
#
# 3. SUDE新算法对比（3D+t-SNE+UMAP+SUDE四宫格）
#    → 打开 sude_work/run_compare.py
#
# 切换数据集只需改对应文件夹里的 config.py
# ============================================================


# ============================================================
# 具体操作：怎么切换数据集？（一项一项跟着做）
# ============================================================
#
# ▶ 情况一：阶段一（经典t-SNE/UMAP对比）换数据集
# ------------------------------------------------------------
# 1. 打开根目录的 config.py
# 2. 找到这一行: DATASET_NAME = 'wine'
# 3. 把引号里的名字改成你想用的数据集，可选:
#      'wine' / 'dermatology' / 'breast_cancer' / 'mfeat'
#      'spambase' / 'dry_bean' / 'mnist' / 'fmnist'
# 4. 保存（Ctrl+S）
# 5. 右键 main.py → Run 'main'
#
#
# ▶ 情况二：阶段三（SUDE对比实验）换数据集
# ------------------------------------------------------------
# 1. 打开 sude_work/config.py
# 2. 找到这一行: DATASET_NAME = 'wine'
# 3. 改成: 'wine' / 'dermatology' / 'breast_cancer' / 'iris' / 'digits'
# 4. 保存
# 5. 右键 sude_work/run_compare.py → Run
#
#
# ▶ 情况三：用自己的数据（不是内置数据集）
# ------------------------------------------------------------
# 1. 把你的数据保存成CSV文件：每行一个样本，最后一列是类别标签
# 2. 打开对应文件夹的 config.py（阶段一改根目录的，SUDE改sude_work的）
# 3. 找到 CSV_PATH = '' 这一行，把你的文件绝对路径填进去:
#      例: CSV_PATH = r'C:\Users\ASUS\Desktop\my_data.csv'
# 4. 找到 CSV_LABEL_COL = -1（默认最后一列是标签，不用改）
# 5. 保存，右键运行主程序
#
#
# ▶ 情况四：阶段二（神经元实验）换数据
# ------------------------------------------------------------
# 不需要改代码，直接把新的 .swc 文件放进 swc_data/ 文件夹
# 然后运行 stage2_neuron/batch_plot_all.py，自动批量处理
#
#
# ▶ 常见问题
# ------------------------------------------------------------
# Q: 改了数据集但图没变？
# A: 确认改的是对应项目的 config.py，不是别的文件夹的
#
# Q: 第一次跑新数据集很慢？
# A: 第一次会联网下载数据，下一次就直接读本地缓存了
#
# Q: 数据太大跑不动？
# A: 主程序默认会截取前3000个样本做演示，结果图上会标注
# ============================================================
