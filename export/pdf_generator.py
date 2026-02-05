from fpdf import FPDF

def export_pdf(data, path):
    pdf = FPDF()
    pdf.add_page()
    pdf.set_font("Arial", size=10)

    for item in data:
        pdf.multi_cell(0, 8, item)

    pdf.output(path)
