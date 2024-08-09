# InvoiceX

InvoiceX is a Python-based tool that extracts key information from invoice PDFs and images using OpenAI's GPT-3.5 model and OCR technology. It automates the process of parsing invoice details, making it easier to process and analyze invoice data.

<img width="652" alt="image" src="https://github.com/user-attachments/assets/3ea6bd10-00ca-4d23-a5e1-640aa71d3fea">

<br><br>

<img width="604" alt="image" src="https://github.com/user-attachments/assets/e2141aaa-3f33-4c7c-9635-d78c7664218a">

## Features

* Extracts text from PDF invoices and image files (PNG, JPG, JPEG)
* Uses OCR (Optical Character Recognition) for processing images
* Leverages AI to parse and structure invoice information
* Extracts customer details, product information (including HSN codes), and total amount
* Outputs structured data in JSON format
* Provides a web interface for easy file upload and processing

## Prerequisites

Before you begin, ensure you have met the following requirements:
- Python 3.7 or higher
- An OpenAI API key
- Tesseract OCR installed (for image processing)

## Installation

1. Clone the repository:

   git clone https://github.com/SomeDieYoung27/InvoiceAlchemy.git

2. Install the required dependencies:
   
   pip install -r requirements.txt

3. Set up your environment variables:
* Create a `.env` file in the root directory
* Add your OpenAI API key:
  ```
  OPENAI_API_KEY=your_api_key_here
  ```

4. Ensure Tesseract OCR is installed and the path is correctly set in the code:
```python
pytesseract.pytesseract.tesseract_cmd = r"C:\Program Files\Tesseract-OCR\tesseract.exe"


##Usage

1.Run the Flask application:
  python app.py

2.Open a web browser and go to http://localhost:5000
3.Upload an invoice PDF or image file through the web interface
4.The application will process the file and return the extracted invoice details in JSON format


##Configuration
You can modify the extract_invoice_details function in app.py to customize the information extracted from invoices.
Contributing
Contributions to InvoiceX are welcome. Please follow these steps:

##Fork the repository
Create a new branch (git checkout -b feature/AmazingFeature)
Make your changes
Commit your changes (git commit -m 'Add some AmazingFeature')
Push to the branch (git push origin feature/AmazingFeature)
Open a Pull Request

##License
Distributed under the MIT License. See LICENSE for more information.
Contact
Email - shashwat12028@gmail.com



