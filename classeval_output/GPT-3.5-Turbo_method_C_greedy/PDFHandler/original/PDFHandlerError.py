import PyPDF2
class PDFHandler: 
    def __init__(self, filepaths):
        """
        takes a list of file paths filepaths as a parameter.
        It creates a list named readers using PyPDF2, where each reader opens a file from the given paths.
        """
        self.filepaths = filepaths
        self.readers = [PyPDF2.PdfFileReader(fp) for fp in filepaths]



    def merge_pdfs(self, output_filepath):
        merged_pdf = PyPDF2.PdfFileMerger()
    
        for reader in self.readers:
            merged_pdf.append(reader)
    
        merged_pdf.write(output_filepath)
        merged_pdf.close()
    
        return f"Merged PDFs saved at {output_filepath}"
    

    def extract_text_from_pdfs(self):
        """
        Extract text from pdf files in self.readers
        :return pdf_texts: list of str, each element is the text of one pdf file
        """
        pdf_texts = []
        for reader in self.readers:
            text = ""
            for page_num in range(reader.numPages):
                page = reader.getPage(page_num)
                text += page.extractText()
            pdf_texts.append(text.strip())
        return pdf_texts
    