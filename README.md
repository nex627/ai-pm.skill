# AI产品经理知识蒸馏

从12个AI产品经理相关PDF中蒸馏出的核心知识框架。

## 目录结构

```
ai-pm-knowledge/
├── distilled/          # 蒸馏结果（核心内容）
│   └── AI产品经理资料蒸馏.md
├── raw-text/           # PDF提取的原始文本
│   ├── 01-12_*.txt
├── tools/              # 提取工具脚本
│   ├── extract_pdfs.py     # PyPDF2批量提取
│   ├── fitz_extract.py     # PyMuPDF提取
│   └── ocr_extract.py      # easyocr扫描版提取
└── .gitignore
```

## 蒸馏内容概览

| 板块 | 内容 |
|------|------|
| 全局认知 | AI产业结构三层模型、PM分类、四大核心能力 |
| 思维模型 | 系统化思维、四大AI思维、心力四力、可演进性 |
| 需求落地 | 需求发现6类、场景评估4条件、ToB优先逻辑 |
| 技术知识 | 语音交互指标体系、数据标注流程、深度学习速查 |
| 关键洞察 | NLP瓶颈、Chatbot缺App、盖尔定律、康威定律 |

## 数据压缩

- 原始PDF：12个，21.2 MB
- 蒸馏文档：~10 KB
- 压缩比：~2100:1

## 工具依赖

- Python 3.13+
- PyPDF2 / PyMuPDF（PDF文本提取）
- easyocr（扫描版PDF OCR，需联网下载模型）

## 注意事项

- #10 面试高频100题为扫描版PDF，需OCR工具提取
- #12 200页PPT为图片为主，部分需OCR提取
- 原始PDF文件不包含在本仓库中
