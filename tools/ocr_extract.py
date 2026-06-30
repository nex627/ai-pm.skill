import fitz
import easyocr
import sys
import os
import numpy as np

pdf_path = sys.argv[1]
out_path = sys.argv[2]

print(f"Loading PDF: {pdf_path}")
doc = fitz.open(pdf_path)
print(f"Total pages: {len(doc)}")

print("Initializing easyocr (first run will download model)...")
reader = easyocr.Reader(['ch_sim', 'en'], gpu=False)

text_parts = []
for i, page in enumerate(doc):
    pix = page.get_pixmap(dpi=200)
    img = np.frombuffer(pix.samples, dtype=np.uint8).reshape(pix.height, pix.width, pix.n)
    if pix.n == 4:
        img = img[:, :, :3]

    results = reader.readtext(img)
    page_text = "\n".join([r[1] for r in results if r[1].strip()])

    if page_text.strip():
        text_parts.append(f"=== PAGE {i+1} ===\n{page_text}")

    if (i + 1) % 5 == 0 or i == len(doc) - 1:
        print(f"  Processed {i+1}/{len(doc)} pages, accumulated {len(''.join(text_parts))} chars")

full_text = "\n".join(text_parts)
with open(out_path, "w", encoding="utf-8") as f:
    f.write(full_text)

print(f"Done! Total text: {len(full_text)} chars")
doc.close()
