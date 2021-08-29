from argparse import ArgumentParser
from typing import List, Optional
from PyPDF2 import PdfFileMerger


def merge_pdfs(pdfs: List[str], output_pdf: Optional[str] = "./output.pdf") -> None:
    if len(pdfs) == 0:
        raise RuntimeError("No PDF files found.")

    merger = PdfFileMerger()

    for pdf in pdfs:
        merger.append(pdf)

    merger.write(output_pdf)
    merger.close()


if __name__ == "__main__":
    parser = ArgumentParser()
    parser.add_argument(
        "-o", "--output", type=str, help="Output PDF file.", default="./output.pdf"
    )
    parser.add_argument(
        "-f", "--files", nargs="*", help="PDF files to merge.", default=[]
    )
    output_pdf: str = parser.parse_args().output
    pdfs: List[str] = parser.parse_args().files

    print(f"====> Merging {len(pdfs)} files.")
    merge_pdfs(pdfs, output_pdf)
    print(f"====> Done. Result file: {output_pdf}.")
