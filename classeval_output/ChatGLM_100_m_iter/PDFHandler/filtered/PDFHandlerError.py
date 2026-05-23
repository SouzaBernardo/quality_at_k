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
        
        Here is an example of how to use the method:
        >>> handler = PDFHandler(['a.pdf', 'b.pdf'])
        >>> handler.merge_pdfs('out.pdf')
        Merged PDFs saved at out.pdf
        """
        for fp in self.readers:
            with open(output_filepath, 'rb') as f:
                pdf = PyPDF2.PdfFileReader(fp).getPage(0).extractText()
            pdf = pdf.replace('&copy; 2016 Adobe Systems Inc.')
            pdf = pdf.replace('&copy; 2016 Adobe Systems Inc.', 'Adobe Systems Inc.')
            self.readers.remove(fp)
            with open(output_filepath, 'wb') as f:
                f.write(pdf)

    def extract_text_from_pdfs(self):
        """
         Extract text from pdf files in self.readers
        :return pdf_texts: list of str, each element is the text of one pdf file
        >>> handler = PDFHandler(['a.pdf', 'b.pdf'])
        >>> handler.extract_text_from_pdfs()
        ['Test a.pdf', 'Test b.pdf']
        """
        return self.extract_text_from_pdfs()