from pathlib import Path
from PyPDF2 import PdfReader


def pdf_to_txt(src: Path, dst: Path) -> None:
    """Extract selectable text from a PDF into a UTF-8 .txt file.
)
    """
    reader = PdfReader(str(src))
    chunks = []
    for page in reader.pages:
        text = page.extract_text() or ""
        chunks.append(text.rstrip())
    content = "\n\n".join(chunks).strip()
    dst.write_text(content, encoding="utf-8")
