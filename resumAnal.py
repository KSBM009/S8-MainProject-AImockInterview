from openai import OpenAI
import os
from dotenv import load_dotenv

load_dotenv()  # Load environment variables from .env file
deepseek_api_key = os.getenv("DEEPSEEK_API_KEY")

client = OpenAI(api_key=os.getenv("DEEPSEEK_API_KEY"), baseurl="https://openrouter.ai/api/v1/")

chat = client.chat.completions.create(
    model="deepseek/deepseek-r1:free",
    messages = [
        {"role": "system", "content": "You are an Interviewer. Provide some questions to ask a candidate."},
    ]
)

print(chat.choices[0].message.content)

# def extract_text_from_pdf(pdf_path):
#     with open(pdf_path, 'rb') as file:
#         reader = PyPDF2.PdfReader(file)
#         text = ''
#         for page_num in range(len(reader.pages)):
#             page = reader.pages[page_num]
#             text += page.extract_text()
#         return text

# def upload_file():
#     file_path = filedialog.askopenfilename(filetypes=[("PDF files", "*.pdf")])
#     if file_path:
#         resume_text = extract_text_from_pdf(file_path)
#         print("Extracted Resume Text:")
#         print(resume_text)
        
#         response = requests.post(
#             "https://api.deepseek.com/v1/generate-questions",
#             headers={"Authorization": f"Bearer {deepseek_api_key}"},
#             json={"text": resume_text}
#         )
        
#         if response.status_code == 200:
#             interview_questions = response.json().get("questions", [])
#             print("Generated Interview Questions:")
#             for question in interview_questions:
#                 print(question)
#         else:
#             print("Failed to generate interview questions. Status code:", response.status_code)
#             print("Error message:", response.text)
#     else:
#         print("No file selected.")

# if __name__ == "__main__":
#     root = tk.Tk()
#     root.withdraw()  # Hide the root window
#     upload_file()