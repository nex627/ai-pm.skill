import PyPDF2
import os

pdf_dir = r'D:\BaiduNetdiskDownload\【①】AI产品经理\AI产品经理书籍与面试'
out_dir = r'd:\note\蒸馏数据'
os.makedirs(out_dir, exist_ok=True)

pdfs = [f for f in os.listdir(pdf_dir) if f.endswith('.pdf')]
pdfs.sort()

for i, pdf_name in enumerate(pdfs, 1):
    pdf_path = os.path.join(pdf_dir, pdf_name)
    out_name = f'{i:02d}_{pdf_name.replace(".pdf", ".txt")}'
    out_path = os.path.join(out_dir, out_name)

    try:
        reader = PyPDF2.PdfReader(pdf_path)
        text_parts = []
        for page in reader.pages:
            t = page.extract_text()
            if t:
                text_parts.append(t)
        full_text = '\n---PAGE---\n'.join(text_parts)

        with open(out_path, 'w', encoding='utf-8') as f:
            f.write(full_text)

        print(f'[{i:02d}] {pdf_name} -> {len(reader.pages)} pages, {len(full_text)} chars')
    except Exception as e:
        print(f'[{i:02d}] {pdf_name} -> ERROR: {e}')
