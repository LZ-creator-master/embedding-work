"""
generate_report_pdf.py —— 生成黑白汇报PDF
"""
from reportlab.lib.pagesizes import A4
from reportlab.lib.styles import getSampleStyleSheet, ParagraphStyle
from reportlab.lib.units import cm
from reportlab.lib.enums import TA_CENTER, TA_LEFT
from reportlab.platypus import SimpleDocTemplate, Paragraph, Spacer, PageBreak, Image
from reportlab.pdfbase import pdfmetrics
from reportlab.pdfbase.ttfonts import TTFont
import os

# 注册中文字体（黑体）
font_path = r"C:\Windows\Fonts\simhei.ttf"
if not os.path.exists(font_path):
    font_path = r"C:\Windows\Fonts\simsun.ttc"
pdfmetrics.registerFont(TTFont('Chinese', font_path))

output_path = r"C:\Users\ASUS\PycharmProjects\embedding work\流形学习实验汇报.pdf"

doc = SimpleDocTemplate(
    output_path,
    pagesize=A4,
    leftMargin=2.5*cm,
    rightMargin=2.5*cm,
    topMargin=2.5*cm,
    bottomMargin=2.5*cm,
)

styles = getSampleStyleSheet()

# 标题样式
title_style = ParagraphStyle(
    'CustomTitle',
    parent=styles['Title'],
    fontName='Chinese',
    fontSize=18,
    leading=24,
    alignment=TA_CENTER,
    spaceAfter=20,
    textColor='black',
)

# 一级标题
h1_style = ParagraphStyle(
    'H1',
    parent=styles['Heading1'],
    fontName='Chinese',
    fontSize=14,
    leading=20,
    spaceBefore=15,
    spaceAfter=10,
    textColor='black',
)

# 二级标题
h2_style = ParagraphStyle(
    'H2',
    parent=styles['Heading2'],
    fontName='Chinese',
    fontSize=12,
    leading=18,
    spaceBefore=10,
    spaceAfter=6,
    textColor='black',
)

# 正文
body_style = ParagraphStyle(
    'Body',
    parent=styles['Normal'],
    fontName='Chinese',
    fontSize=10.5,
    leading=18,
    spaceAfter=6,
    textColor='black',
    firstLineIndent=21,
)

# 列表项（不缩进）
list_style = ParagraphStyle(
    'List',
    parent=styles['Normal'],
    fontName='Chinese',
    fontSize=10.5,
    leading=18,
    spaceAfter=4,
    textColor='black',
    leftIndent=20,
)

story = []

# 标题
story.append(Paragraph('流形学习经典算法实验汇报', title_style))
story.append(Spacer(1, 0.5*cm))

# 第一部分：数据集介绍
story.append(Paragraph('一、实验数据集介绍', h1_style))

datasets = [
    ('1. Iris 鸢尾花数据集', [
        '来源：UCI Machine Learning Repository，Fisher 1936年经典数据',
        '规模：150样本 × 4维，3类（山鸢尾、变色鸢尾、维吉尼亚鸢尾）',
        '内容：花萼长度、花萼宽度、花瓣长度、花瓣宽度四个植物学特征',
        '特点：流形学习入门测试集，三类边界清晰，是最简单的对照数据',
    ]),
    ('2. Wine 葡萄酒数据集', [
        '来源：UCI id=109，意大利同一地区三种葡萄酿制的葡萄酒',
        '规模：178样本 × 13维，3类',
        '内容：酒精含量、苹果酸、镁、总酚、黄酮类、颜色强度、脯氨酸等13种化学成分',
        '特点：真实化学测量数据，适合作为医学/化学类真实数据代表',
    ]),
    ('3. Breast Cancer 乳腺癌数据集', [
        '来源：UCI威斯康星医学院，乳腺肿块细针穿刺细胞数据',
        '规模：569样本 × 30维，2类（良性、恶性）',
        '内容：细胞核半径、纹理、周长、面积等10个特征的均值、标准差、最差值',
        '特点：二分类医学数据，线性可分程度高，作为简单数据对照组',
    ]),
    ('4. Dermatology 皮肤病数据集', [
        '来源：UCI id=33，奥地利维也纳大学皮肤科临床数据',
        '规模：366样本 × 34维，6类',
        '内容：皮损形态学特征、家族史、年龄等，含缺失值（?）',
        '特点：多类医学数据，6种皮肤病症状相似，有缺失值干扰，是难度较高的数据',
    ]),
    ('5. Digits 手写数字数据集', [
        '来源：sklearn内置，UCI手写数字数据库子集',
        '规模：1797样本 × 64维（8×8灰度图），10类（0-9）',
        '内容：低分辨率手写数字图像像素值',
        '特点：图像类高维数据代表，10类细粒度区分，数字4和9、3和8形态相似',
    ]),
    ('6. PBMC3k 单细胞免疫细胞数据集（导师推荐方向）', [
        '来源：10x Genomics公开单细胞测序数据，对应导师推荐的scBaseCount方向',
        '规模：约2700个细胞 × 13714个基因维度，8类免疫细胞',
        '内容：外周血单个核细胞的基因表达谱',
        '特点：超高维数据代表，对应单细胞生物信息学前沿方向',
    ]),
]

for name, items in datasets:
    story.append(Paragraph(name, h2_style))
    for item in items:
        story.append(Paragraph('• ' + item, list_style))

story.append(PageBreak())

# 第二部分：实验对比图
story.append(Paragraph('二、多数据集降维效果对比', h1_style))
story.append(Paragraph(
    '下图为六个数据集上三种方法的对比结果：左列为PCA 3D原始结构，中列为t-SNE 2D，右列为UMAP 2D。'
    '从上到下难度递增：Iris → Wine → Breast Cancer → Dermatology → Digits → PBMC3k（单细胞）。',
    body_style
))
story.append(Spacer(1, 0.3*cm))

# 插入对比图
img_path = r"C:\Users\ASUS\PycharmProjects\embedding work\summary_comparison.png"
img = Image(img_path, width=16*cm, height=20*cm)
story.append(img)
story.append(Spacer(1, 0.3*cm))
story.append(Paragraph('图1 多数据集 × 多算法降维效果对比', ParagraphStyle(
    'caption', parent=body_style, alignment=TA_CENTER, firstLineIndent=0, fontSize=9
)))

story.append(PageBreak())

# 第三部分：算法局限性
story.append(Paragraph('三、经典流形算法的局限性总结', h1_style))
story.append(Paragraph('基于以上五个数据集从易到难的对比实验，t-SNE与UMAP在以下场景中表现不足：', body_style))

limitations = [
    ('局限1：高维空间下参数极度敏感', [
        '现象：困惑度或近邻数微调后，降维结果完全不同',
        '原因：高维空间距离失真，算法基于距离判断近邻，距离本身已不可靠',
        '典型数据：Digits（64维）、Dermatology（34维）',
    ]),
    ('局限2：多类细粒度分类时类间粘连', [
        '现象：形态相似的类别被揉成一团，类边界模糊不清',
        '原因：算法只保证局部近邻不被拆散，不保证远距离类别被拉开',
        '典型数据：Dermatology（6类皮肤病）、Digits（10类数字）',
    ]),
    ('局限3：只关注局部结构，全局关系丢失', [
        '现象：散点图上团分得很开，但类与类之间的远近关系是错误的',
        '原因：t-SNE与UMAP优化目标是局部条件概率，不约束全局相对位置',
        '典型数据：所有数据集均存在，复杂数据上尤为明显',
    ]),
    ('局限4：类不平衡时小类结构失真', [
        '现象：样本量少的类别被挤成小团，或被拉到极远位置',
        '原因：小类近邻数量少，局部结构估计不稳定',
        '典型数据：Dermatology中病例数较少的皮肤病类型',
    ]),
    ('局限5：大样本下计算成本爆炸', [
        '现象：大规模数据上t-SNE运行时间极长，内存占用高',
        '原因：t-SNE复杂度为O(N²)，UMAP稍好但仍受限',
        '典型数据：图像数据集、单细胞测序数据（数万至数十万样本）',
    ]),
    ('局限6：对噪声与缺失值鲁棒性差', [
        '现象：数据存在缺失或噪声时，降维结果混乱',
        '原因：距离计算被噪声污染，近邻图构建出错',
        '典型数据：Dermatology（含缺失值）',
    ]),
]

for name, items in limitations:
    story.append(Paragraph(name, h2_style))
    for item in items:
        story.append(Paragraph('• ' + item, list_style))

story.append(Spacer(1, 0.5*cm))

# 总结
story.append(Paragraph('四、结论', h1_style))
story.append(Paragraph(
    't-SNE与UMAP仅适用于简单小数据的可视化任务。面对高维、多类、细粒度、大规模的真实数据时，'
    '两类经典算法均存在结果不稳定、全局结构失真、计算效率低下等问题。'
    '这正是本项目研究自适应权重融合算法的核心动机：通过融合局部与全局结构信息，'
    '在保持局部精细分离的同时，维护真实的全局类间关系。',
    body_style
))

doc.build(story)
print(f"PDF已生成: {output_path}")
