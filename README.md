<img width="524" alt="swipe" src="https://github.com/user-attachments/assets/b69811d1-c3f4-45a3-9199-91ca263cd3a6">







# InvoiceX

InvoiceAlchemy is a Python-based tool that extracts key information from invoice PDFs using OpenAI's GPT-3.5 model. It automates the process of parsing invoice details, making it easier to process and analyze invoice data.

## Features

- Extracts text from PDF invoices
- Uses AI to parse and structure invoice information
- Extracts customer details, product information (including HSN codes), and total amount
- Outputs structured data in JSON format

## Prerequisites

Before you begin, ensure you have met the following requirements:

- Python 3.7 or higher
- An OpenAI API key

## Installation

1. Clone the repository:
   
 git clone https://github.com/SomeDieYoung27/InvoiceAlchemy.git
 cd InvoiceAlchemy

2. Install the required dependencies:
   pip install -r requirements.txt

3. Set up your environment variables:
- Create a `.env` file in the root directory
- Add your OpenAI API key:
  ```
  OPENAI_API_KEY=your_api_key_here
  ```

 ## Usage

 1. Place your invoice PDF in the project directory or specify the full path to the PDF.

 2. Run the script:
    python app.py

3. The script will output the extracted invoice details in JSON format.

## Configuration

You can modify the `extract_invoice_details` function in `app.py` to customize the information extracted from invoices.

## Contributing

Contributions to InvoiceX are welcome. Please follow these steps:

1. Fork the repository
2. Create a new branch (`git checkout -b feature/AmazingFeature`)
3. Make your changes
4. Commit your changes (`git commit -m 'Add some AmazingFeature'`)
5. Push to the branch (`git push origin feature/AmazingFeature`)
6. Open a Pull Request

## License

Distributed under the MIT License. See `LICENSE` for more information.

## Contact

Email - shashwat 12028@gmail.com
