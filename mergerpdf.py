import os
from PyPDF2 import PdfReader, PdfWriter

def merge_pdfs(input_pdfs, output_pdf):
    pdf_writer = PdfWriter()

    for pdf_path, page_numbers in input_pdfs: 
        pdf = PdfReader(open(pdf_path, 'rb'))
        
        if "all" in page_numbers:
            # Include all pages from the PDF
            for page in pdf.pages:
                pdf_writer.add_page(page)
        else:
            # Include specific pages
            for page_number in page_numbers:
                page = pdf.pages[page_number - 1]  # Page numbers are 1-based
                pdf_writer.add_page(page)

    with open(output_pdf, 'wb') as output_file:
        pdf_writer.write(output_file)

input_pdfs = [] #stores the data of inputted pdfs of the user

pdf_folder = r""  # put the folder path of the PDFS that you want to merge between the ""
#example : /user/python/tanginamo/PDFCOMBINER

#user will input the file name here:
while True:
    pdf_file = input("\nEnter the PDF file name (e.g., filename.pdf) or type 'done' to finish: ")
    if pdf_file.lower() == 'done':
        break
    
    pdf_path = os.path.join(pdf_folder, pdf_file)
    
    #user will input the number of pages here:
    page_numbers_str = input(f"Enter the page numbers from '{pdf_file}' (e.g., 1,3,5) or 'all': ")
    if "all" in page_numbers_str.lower(): #if they enter all, all of the pages in the PDF will be selected.
        page_numbers = ["all"]
    else:
        page_numbers = [int(num.strip()) for num in page_numbers_str.split(",")] #else, it will count the entered pages number.
    
    input_pdfs.append((pdf_path, page_numbers)) 

output_pdf = 'mergedfiles.pdf'
output_pdf = os.path.join(pdf_folder, 'mergedfiles.pdf')  # Save in the same folder as the input PDFs


merge_pdfs(input_pdfs, output_pdf)

print('PDF pages merged successfully.')



