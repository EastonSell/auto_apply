"""Generate PDF files from text."""
from pathlib import Path
from fpdf import FPDF


class PDFGenerator:
    def __init__(self, output_dir: str = "pdfs") -> None:
        self.output_dir = Path(output_dir)
        self.output_dir.mkdir(exist_ok=True)

    def create_pdf(self, text: str, filename: str) -> Path:
        pdf = FPDF()
        pdf.add_page()
        pdf.set_font("Arial", size=12)
        for line in text.splitlines():
            pdf.cell(200, 10, txt=line, ln=1)
        path = self.output_dir / filename
        pdf.output(str(path))
        return path
