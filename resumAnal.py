import PyPDF2
import tkinter as tk
from tkinter import filedialog

def extract_text_from_pdf(pdf_path):
    with open(pdf_path, 'rb') as file:
        reader = PyPDF2.PdfFileReader(file)
        text = ''
        for page_num in range(reader.numPages):
            page = reader.getPage(page_num)
            text += page.extract_text()
        return text

def upload_file():
    file_path = filedialog.askopenfilename(filetypes=[("PDF files", "*.pdf")])
    if file_path:
        resume_text = extract_text_from_pdf(file_path)
        print("Extracted Text from Resume:")
        print(resume_text)

if __name__ == "__main__":
    root = tk.Tk()
    root.withdraw()  # Hide the root window
    upload_file()