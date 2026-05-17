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

    def extract_text_from_pdfs(self):
        """
        Extract text from pdf files in self.readers
        :return pdf_texts: list of str, each element is the text of one pdf file
        >>> handler = PDFHandler(['a.pdf', 'b.pdf'])
        >>> handler.extract_text_from_pdfs()
        ['Test a.pdf', 'Test b.pdf']
        """

    def extract_text_from_file(self, file_path):
        """
        Extract text from file in self.readers
        :param file_path: str, file path to read from
        :return pdf_texts: list of str, each element is the text of one pdf file
        >>> handler = PDFHandler(['a.pdf', 'b.pdf'])
        >>> handler.extract_text_from_file('out.pdf')
        ['Test a.pdf', 'Test b.pdf']
        """

    def extract_text_from_file_list(self, file_list):
        """
        Extract text from file list in self.readers
        :param file_list: list of str, file paths to read from
        :return pdf_texts: list of str, each element is the text of one pdf file
        >>> handler = PDFHandler(['a.pdf', 'b.pdf'])
        >>> handler.extract_text_from_file_list(['out.pdf'])
        ['Test a.pdf', 'Test b.pdf']
        """

    def extract_text_from_file_list_with_page_number(self, file_list, page_number):
        """
        Extract text from file list in self.readers
        :param file_list: list of str, file paths to read from
        :param page_number: int, page number to extract text from
        :return pdf_texts: list of str, each element is the text of one pdf file
        >>> handler = PDFHandler(['a.pdf', 'b.pdf'])
        >>> handler.extract_text_from_file_list_with_page_number(['out.pdf'], 1)
        ['Test a.pdf', 'Test b.pdf']
        """

    def extract_text_from_file_list_with_page_number_and_text_list(self, file_list, page_number, text_list):
        """
        Extract text from file list in self.readers
        :param file_list: list of str, file paths to read from
        :param page_number: int, page number to extract text from
        :param text_list: list of str, text to extract from file list
        :return pdf_texts: list of str, each element is the text of one pdf file
        >>> handler = PDFHandler(['a.pdf', 'b.pdf'])
        >>> handler.extract_text_from_file_list_with_page_number_and_text_list(['out.pdf'], 1, ['Test a.pdf', 'Test b.pdf'])
        ['Test a.pdf', 'Test b.pdf']
        """

    def extract_text_from_file_list_with_page_number_and_text_list_and_text_list(self, file_list, page_number, text_list, text_list):
        """
        Extract text from file list in self.readers
        :param file_list: list of str, file paths to read from
        :param page_number: int, page number to extract text from
        :param text_list: list of str, text to extract from file list
        :param text_list: list of str, text to extract from file list
        :return pdf_texts: list of str, each element is the text of one pdf file
        >>> handler = PDFHandler(['a.pdf', 'b.pdf'])
        >>> handler.extract_text_from_file_list_with_page_number_and_text_list_and_text_list(['out.pdf'], 1, ['Test a.pdf', 'Test b.pdf'])
        ['Test a.pdf', 'Test b.pdf']
        """

    def extract_text_from_file_list_with_page_number_and_text_list_and_text_list_and_text_list(self, file_list, page_number, text_list, text_list, text_list):
        """
        Extract text from file list in self.readers
        :param file_list: list of str, file paths to read from
        :param page_number: int, page number to extract text from
        :param text_list: list of str, text to extract from file list
        :param text_list: list of str, text to extract from file list
        :param text_list: list of str, text to extract from file list
        :return pdf_texts: list of str, each element is the text of one pdf file
        >>> handler = PDFHandler(['a.pdf', 'b.pdf'])
        >>> handler.extract_text_from_file_list_with_page_number_and_text_list_and_text_list_and_text_list(['out.pdf'], 1, ['Test a.pdf', 'Test b.pdf'])
        ['Test a.pdf', 'Test b.pdf']
        """

    def extract_text_from_file_list_with_page_number_and_text_list_and_text_list_and_text_list_and_text_list(self, file_list, page_number, text_list, text_list,