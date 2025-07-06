from PyPDF2 import PdfReader

def read_pdf_metadata(file_path):
    try:
        reader = PdfReader(file_path)
        info = reader.metadata

        print("📄 PDF Metadata:")
        print(f"Title: {info.title}")
        print(f"Author: {info.author}")
        print(f"Creator: {info.creator}")
        print(f"Producer: {info.producer}")
        print(f"Creation Date: {info.creation_date}")
        print(f"Mod Date: {info.modification_date}")

    except FileNotFoundError:
        print(" File not found. Please check the path.")
    except Exception as e:
        print(f" Error reading PDF: {e}")

file = input("Enter the path to the PDF file: ")
while ( ".pdf"  not  in  file):
    file = input(" Pls enter a valid PDF : ")


read_pdf_metadata(file)
