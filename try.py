import gradio as gr
from PyPDF2 import PdfReader

def read_pdf(file):
    # Read the PDF file
    pdf_reader = PdfReader(file.name)
    text = ""
    for page_num in range(len(pdf_reader.pages)):
        text += pdf_reader.pages[page_num].extract_text() + "\n"
    return text

# Gradio interface
interface = gr.Interface(
    fn=read_pdf,
    inputs=gr.File(label="Upload PDF"),
    outputs=gr.Textbox(label="PDF Content"),
    title="PDF Uploader and Viewer",
    description="Upload a PDF file and view its content."
)

interface.launch()
