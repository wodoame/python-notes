# PyPDF2 is a Python library that allows you to work with PDF files.
# If you want to read text from a PDF using PyPDF2, you can follow these steps:

# 1. Install PyPDF2:
#    You can install PyPDF2 using pip by running the following command in your terminal or command prompt:
#    pip install PyPDF2

# Note that some functions used here may have been deprecated as they have provided new naming conventions for them 
# They have moved to using snake case naming convention

# 2. Use PyPDF2 to read text from a PDF:
   import PyPDF2

   def read_pdf(file_path):
       with open(file_path, 'rb') as file:
           # Create a PDF reader object
           pdf_reader = PyPDF2.PdfReader(file)
           # But from the documentation a pdf reader was created by just passing in the file path without creating a file object like this: 
           pdf_reader = PyPDF2.PdfReader(file_path)  # Anyone that works works

           # Get the number of pages in the PDF
           num_pages = len(pdf_reader.pages)

           # Initialize an empty string to store the text
           text = ''

           # Iterate through all pages and extract text
           for page_num in range(num_pages):
               # Get the page
               page = pdf_reader.pages[page_num] # pdf_reader.pages is an object like a list and so the page indexing starts from 0.
                                                 # Therefore the first page is pdf_reader.pages[0]

               # Extract text from the page
               text += page.extract_text()

           return text

   # Replace 'your_file.pdf' with the path to your PDF file
   pdf_file_path = 'your_file.pdf'
   extracted_text = read_pdf(pdf_file_path)

   print(extracted_text)
   

   # Replace 'your_file.pdf' with the path to your actual PDF file.

# Note: PyPDF2 may not work well with all types of PDFs, especially those with complex structures or encrypted content.
# If you encounter issues, you might want to explore other libraries like PyMuPDF (MuPDF) or PyPDFium, which can handle a wider range of PDFs.

# PyMuPDF (MuPDF) and PyPDFium are alternative libraries to PyPDF2 that offer some advantages in certain scenarios:

# 1. **Support for More PDF Features:**
#    - **PyMuPDF (MuPDF):** MuPDF is known for its high-performance rendering and support for a wide range of PDF features.
#     It can handle more complex PDF structures, making it suitable for documents with advanced graphics, annotations, and encryption.

#    - **PyPDFium:** PyPDFium is another alternative that aims to provide better support for modern PDF features. It supports features like annotations, form fields, and more.

# 2. **Better Text Extraction:**
#    - **PyMuPDF (MuPDF):** MuPDF is often praised for its accurate text extraction capabilities. It can handle a variety of PDF layouts and is more likely to preserve the original formatting.

#    - **PyPDFium:** PyPDFium also focuses on accurate text extraction and has been designed to handle various PDF structures.

# 3. **Active Development:**
#    - **PyMuPDF (MuPDF):** MuPDF is actively maintained and updated. It is a robust library with a strong focus on performance and accuracy.

#    - **PyPDFium:** PyPDFium, as of my last knowledge update in January 2022, was actively developed by the Foxit Software company.

# 4. **Licensing:**
#    - **PyMuPDF (MuPDF):** MuPDF is open-source and available under the Affero General Public License (AGPL).
#     This means you can use it freely in open-source projects, but you may need to be cautious with its use in proprietary applications.

#    - **PyPDFium:** PyPDFium is developed by Foxit Software, which also offers commercial PDF solutions.
#       Licensing may vary, so it's important to check and ensure compliance with any licensing requirements.

# 5. **Performance:**
#    - **PyMuPDF (MuPDF):** MuPDF is known for its fast rendering and extraction speed. It's designed to be efficient, making it a good choice for applications with performance considerations.

#    - **PyPDFium:** PyPDFium is developed by Foxit, a company known for its PDF technology. It also aims to provide good performance.

# When choosing a PDF library, consider the specific requirements of your project, the complexity of the PDF files you're working with, and any licensing considerations.
# Each library has its strengths, and the best choice depends on your use case. Always check the latest documentation for the most up-to-date information on features and compatibility.


# To read a PDF file line by line using PyPDF2, you can modify the code to split the extracted text into lines.
# Here's an example:

import PyPDF2

def read_pdf_line_by_line(file_path):
    with open(file_path, 'rb') as file:
        # Create a PDF reader object
        pdf_reader = PyPDF2.PdfReader(file)

        # Get the number of pages in the PDF
        num_pages = len(pdf_reader.pages)

        # Initialize an empty list to store lines of text
        lines = []

        # Iterate through all pages and extract text line by line
        for page_num in range(num_pages):
            # Get the page
            page = pdf_reader.pages[page_num]

            # Extract text from the page and split it into lines
            lines += page.extract_text().split('\n')
            # python (or I think the new versions) support a method called splitlines() on strings
            # so you could do this instead
            lines += page.extract_text().splitlines()
            

        return lines

# Replace 'your_file.pdf' with the path to your PDF file
pdf_file_path = 'your_file.pdf'
extracted_lines = read_pdf_line_by_line(pdf_file_path)

# Print each line
for line in extracted_lines:
    print(line)

# This code extracts the text from each page, splits it into lines using the `split('\n')` method, and then appends the lines to the `lines` list.
# The result is a list where each element represents a line of text from the PDF.

# Keep in mind that the quality of the text extraction can vary depending on the PDF file's content and structure.
# If the PDF has complex formatting, the extracted text may not be perfectly organized into lines.
