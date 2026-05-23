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
        
        merger = PyPDF2.PdfFileMerger()
        for reader in self.readers:
            merger.append(reader)
        merger.write(output_filepath)
        return "Merged PDFs saved at {}".format(output_filepath)


    def extract_text_from_pdfs(self):
        

        pdf_texts = []
        for reader in self.readers:
            pdf_texts.append(reader.getPage(0).extractText())
        return pdf_texts
