from parser_pdf import get_text_from_pdf
from gpt_ai import get_payments_info


def payments_parse_process(file_path):
    text=get_text_from_pdf(file_path)
    info=get_payments_info(text)
    return info

print(payments_parse_process("example.pdf"))