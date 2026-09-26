# Extracting text with PyPDF

# PyPDF allows us to extract text from PDF documents, making it useful
# for working with multi-page documents such as employee policies,
# reports, and other business documents.
#
# In this exercise, load the "US_Employee_Policy.pdf" file, extract
# its text page by page, and combine the extracted content into a
# single string.
#
# This combined text can then be used as input for a
# question-answering pipeline.

# Instructions:
# - Import the required class from the "pypdf" library.
# - Use the class to load the "US_Employee_Policy.pdf" file.
# - Access each page in the PDF.
# - Extract the text from each page using the appropriate method.
# - Combine the extracted text into a single string.

from pypdf import PdfReader

# Extract text from the PDF
reader = PdfReader("US_Employee_Policy.pdf")

# Extract text from all pages
document_text = ""
for page in reader.pages: 
    document_text += page.extract_text()

print(document_text)


    # US Employee Policy Document
    # Welcome to the US Employee Policy document. This document outlines the policies and benefits
    # available to all employees. Please read carefully to understand your entitlements and
    # responsibilities.
    # 1. Vacation Policy:
    # Employees are entitled to 25 vacation days annually.
    # 2. Sick Leave:
    # Employees may take up to 10 sick days per year.
    # 3. Notice Period:
    # Employees are required to give a 2-week notice before resignation.Work and Leave Policies
    # 4. Public Holidays:
    # The company observes 12 public holidays annually.
    # 5. Maternity Leave:
    # Employees are entitled to up to 16 weeks of maternity leave.
    # 6. Paternity Leave:
    # Employees are entitled to up to 10 days of paternity leave.
    # 7. Volunteer Days:
    # Each employee is allowed 1 volunteer day annually to contribute to social causes.Additional Information
    # 8. Probation Period:
    # New employees undergo a 3-month probation period.
    # 9. Remote Work:
    # Employees may work remotely up to 2 days per week.
    # 10. Retirement Age:
    # The standard retirement age is 65 years.
    # For further questions, please contact the HR department.