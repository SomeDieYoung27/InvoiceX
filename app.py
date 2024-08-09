import os
import PyPDF2
from openai import OpenAI
from dotenv import load_dotenv

# Load environment variables
load_dotenv()

# Set up OpenAI client
client = OpenAI(api_key=os.getenv("OPENAI_API_KEY"))

def extract_text_from_pdf(pdf_path):
    with open(pdf_path, 'rb') as file:
        reader = PyPDF2.PdfReader(file)
        text = ""
        for page in reader.pages:
            text += page.extract_text()
    return text

def extract_invoice_details(text):
    prompt = f"""
    Extract the following information from the invoice text:
    1. Customer details (name, address, phone, email)
    2. Products (name, HSN code, quantity, rate, total amount)
    3. Total Amount

    Invoice text:
    {text}

    Please format the output as JSON:
    {{
        "customer_details": {{
            "name": "",
            "address": "",
            "phone": "",
            "email": ""
        }},
        "products": [
            {{
                "name": "",
                "hsn_code": "",
                "quantity": "",
                "rate": "",
                "total_amount": ""
            }}
        ],
        "total_amount": ""
    }}
    """

    response = client.chat.completions.create(
        model="gpt-3.5-turbo",
        messages=[
            {"role": "system", "content": "You are a helpful assistant that extracts information from invoices."},
            {"role": "user", "content": prompt}
        ]
    )

    return response.choices[0].message.content

def process_invoice(pdf_path):
    text = extract_text_from_pdf(pdf_path)
    details = extract_invoice_details(text)
    return details

# Example usage
if __name__ == "__main__":
    pdf_path = "invoice.pdf"  # Replace with your actual PDF path
    invoice_details = process_invoice(pdf_path)
    print(invoice_details)