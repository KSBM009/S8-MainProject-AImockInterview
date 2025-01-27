import PyPDF2
import tkinter as tk
import openai
import os
from tkinter import filedialog
from dotenv import load_dotenv

load_dotenv()  # Load environment variables from .env file
openai.api_key = os.getenv("OPENAI_API_KEY")

def extract_text_from_pdf(pdf_path):
    with open(pdf_path, 'rb') as file:
        reader = PyPDF2.PdfReader(file)
        text = ''
        for page_num in range(len(reader.pages)):
            page = reader.pages[page_num]
            text += page.extract_text()
        return text

def upload_file():
    file_path = filedialog.askopenfilename(filetypes=[("PDF files", "*.pdf")])
    if file_path:
        resume_text = extract_text_from_pdf(file_path)
        print("Extracted Resume Text:")
        print(resume_text)
        response = openai.Completion.create(
            model="gpt-4o-mini",
            prompt=f"Generate interview questions based on the following resume text:\n\n{resume_text}",
            max_tokens=150
        )
        interview_questions = response.choices[0].text.strip()
        print("Generated Interview Questions:")
        print(interview_questions)
    else:
        print("No file selected.")

if __name__ == "__main__":
    root = tk.Tk()
    root.withdraw()  # Hide the root window
    upload_file()