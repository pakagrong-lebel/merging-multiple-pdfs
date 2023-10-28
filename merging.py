# Python script to merge multiple PDFs into a single PDF
import PyPDF2
def merge_pdfs(input_paths, output_path):
    pdf_merger = PyPDF2.PdfMerger()
    for path in input_paths:
        with open(path, 'rb') as f:
            pdf_merger.append(f)
            with open(output_path, 'wb') as f:
                pdf_merger.write(f)







