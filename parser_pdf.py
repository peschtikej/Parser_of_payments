from PyPDF2 import PdfReader


def get_text_from_pdf(file_path: str) -> str:
    reader = PdfReader(file_path)
    page = reader.pages[0]
    text = page.extract_text()
    return text
