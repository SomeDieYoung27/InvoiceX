import os
import tempfile
import json
import logging

import PyPDF2
import pytesseract
from dotenv import load_dotenv
from flask import Flask, jsonify, render_template, request
from openai import OpenAI
from PIL import Image

pytesseract.pytesseract.tesseract_cmd = r"C:\Program Files\Tesseract-OCR\tesseract.exe"

load_dotenv()
client = OpenAI(api_key=os.getenv("OPENAI_API_KEY"))

app = Flask(__name__)
logging.basicConfig(level=logging.DEBUG)

def extract_text_from_pdf(file):
    try:
        reader = PyPDF2.PdfReader(file)
        text = ""
        for page in reader.pages:
            text += page.extract_text()
        return text.strip()
    except Exception as e:
        logging.error(f"Error extracting text from PDF: {str(e)}")
        return None

def extract_text_from_image(file):
    try:
        image = Image.open(file)
        text = pytesseract.image_to_string(image)
        return text.strip()
    except Exception as e:
        logging.error(f"Error extracting text from image: {str(e)}")
        return None

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
    try:
        response = client.chat.completions.create(
            model="gpt-3.5-turbo",
            messages=[
                {
                    "role": "system",
                    "content": "You are a helpful assistant that extracts information from invoices.",
                },
                {"role": "user", "content": prompt},
            ],
        )
        return response.choices[0].message.content
    except Exception as e:
        logging.error(f"Error in OpenAI API call: {str(e)}")
        return None

def process_invoice(file, filename):
    file_extension = os.path.splitext(filename)[1].lower()

    if file_extension == ".pdf":
        text = extract_text_from_pdf(file)
    elif file_extension in [".png", ".jpg", ".jpeg"]:
        text = extract_text_from_image(file)
    else:
        return {"error": "Unsupported file format"}

    if text is None:
        return {"error": "Failed to extract text from the file"}

    logging.debug(f"Extracted text: {text[:500]}...")  # Log first 500 characters

    details = extract_invoice_details(text)
    
    if details is None:
        return {"error": "Failed to extract invoice details"}

    try:
        json_details = json.loads(details)
        return json_details
    except json.JSONDecodeError as e:
        logging.error(f"JSON decode error: {str(e)}")
        return {"error": "Failed to parse invoice details", "raw_output": details}

@app.route("/", methods=["GET", "POST"])
def index():
    if request.method == "POST":
        if "file" not in request.files:
            return jsonify({"error": "No file part"})

        file = request.files["file"]

        if file.filename == "":
            return jsonify({"error": "No selected file"})

        if file:
            with tempfile.NamedTemporaryFile(delete=False) as temp:
                file.save(temp.name)
                temp_path = temp.name

            result = process_invoice(temp_path, file.filename)

            os.unlink(temp_path)

            return jsonify(result)

    return render_template("index.html")

if __name__ == "__main__":
    app.run(debug=True)
