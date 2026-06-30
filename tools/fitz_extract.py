import fitz
import sys
import os

pdf_path = sys.argv[1]
out_path = sys.argv[2]

doc = fitz.open(pdf_path)
text_parts = []

for i, page in enumerate(doc):
    text = page.get_text()
    if text.strip():
        text_parts.append(f"=== PAGE {i+1} ===\n{text}")

full_text = "\n".join(text_parts)
with open(out_path, "w", encoding="utf-8") as f:
    f.write(full_text)

print(f"Pages: {len(doc)}, Text chars: {len(full_text)}")
doc.close()
