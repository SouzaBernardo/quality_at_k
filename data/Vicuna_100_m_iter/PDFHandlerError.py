import PyPDF2
class PDFHandler:  
    """
    The class allows merging multiple PDF files into one and extracting text from PDFs using PyPDF2 library.
    """

    def __init__(self, filepaths):
        """
        takes a list of file paths filepaths as a parameter.
        It creates a list named readers using PyPDF2, where each reader opens a file from the given paths.
        """
        self.filepaths = filepaths
        self.readers = [PyPDF2.PdfFileReader(fp) for fp in filepaths]



    def merge_pdfs(self, output_filepath):
        """
        Read files in self.readers which stores handles to multiple PDF files.
        Merge them to one pdf and update the page number, then save in disk.
        :param output_filepath: str, ouput file path to save to
        :return: str, "Merged PDFs saved at {output_filepath}" if successfully merged
        >>> handler = PDFHandler(['a.pdf', 'b.pdf'])
        >>> handler.merge_pdfs('out.pdf')
        Merged PDFs saved at out.pdf
        """
        for reader in self.readers:
            pdf = PyPDF2.PdfFileReader(reader)
            page_count = pdf.getNumPages()
            merged_pdf = PyPDF2.PdfFileWriter()
            for i in range(page_count):
                page = pdf.getPage(i)
                merged_pdf.addPage(page)
            merged_pdf.write(output_filepath)

    def extract_text_from_pdfs(self):
        pdf_texts = []
        for reader in self.readers:
            pdf = PyPDF2.PdfFileReader(reader)
            page_count = pdf.getNumPages()
            merged_pdf = PyPDF2.PdfFileWriter()
            for i in range(page_count):
                page = pdf.getPage(i)
                text = page.extractText()
                merged_pdf.addPage(page)
            pdf_texts.append(merged_pdf.getDocumentInfo().title)
        return pdf_texts