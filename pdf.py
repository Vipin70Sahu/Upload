import gradio as gr  
import fitz  
import io

def show_filename_and_full_text(file):
    if file:
        file_bytes = file.read_bytes()
        doc = fitz.open(stream=io.BytesIO(file_bytes), filetype="pdf")
        
        full_text = ""
        for page_num in range(doc.page_count):
            full_text += doc[page_num].get_text() + "\n"
        
        
        doc.close()
        
        return file.name, full_text
    
    return "No file uploaded", ""

pdf_upload = gr.File(label="Upload a PDF", file_types=['.pdf'])
pdf_filename = gr.Textbox(label="PDF Filename")
full_text = gr.Textbox(label="PDF Full Text", lines=20)

iface = gr.Interface(
    fn=show_filename_and_full_text,
    inputs=pdf_upload,
    outputs=[pdf_filename, full_text],
    title="PDF Upload and Display",
    description="Upload a PDF file and display the filename and text from the entire document."
)
# Launch 
iface.launch()

