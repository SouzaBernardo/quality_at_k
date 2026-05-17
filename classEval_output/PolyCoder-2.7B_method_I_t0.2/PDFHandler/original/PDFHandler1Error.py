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
        # merge multiple PDFs
        merged_pdf_files = []
        for reader in self.readers:
            merged_pdf_files.append(reader.merge_pdf(output_filepath))
        # save to disk
        merged_pdf_files = [f for f in merged_pdf_files if f!= output_filepath]
        # update page number
        merged_pdf_files[0].update_page_number()
        return merged_pdf_files




    def extract_text_from_pdfs(self):
        """
        Extract text from pdf files in self.readers
        :return pdf_texts: list of str, each element is the text of one pdf file
        >>> handler = PDFHandler(['a.pdf', 'b.pdf'])
        >>> handler.extract_text_from_pdfs()
        ['Test a.pdf', 'Test b.pdf']
        """
        # extract text from multiple PDFs
        pdf_texts = []
        for reader in self.readers:
            pdf_texts.append(reader.extract_text_from_pdf())
        # save to disk
        pdf_texts = [f for f in pdf_texts if f!= "Test a.pdf" and f!= "Test b.pdf"]
        # update page number
        pdf_texts[0].update_page_number()
        return pdf_texts



