import PyPDF2

def count_pdf_pages(pdf_file_path):
    try:
        pdf_reader = PyPDF2.PdfReader(pdf_file_path)
        num_pages = len(pdf_reader.pages)
        return num_pages
    except Exception as e:
        print(f"Error: {e}")
        return None

# Replace 'your_pdf_file.pdf' with the path to your PDF file
pdf_file_path = r"E:\\c++\\avxm\\sample2.pdf"
page_count = count_pdf_pages(pdf_file_path)

if page_count is not None:
    print(f'The PDF file "{pdf_file_path}" has {page_count} pages.')
else:
    print('Failed to count pages in the PDF.')
