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

    def extract_text_from_file(self, output_filepath):
        """
        Extract text from file in self.readers
        :param output_filepath: str, ouput file path to save to
        :return pdf_texts: list of str, each element is the text of one pdf file
        >>> handler = PDFHandler(['a.pdf', 'b.pdf'])
        >>> handler.extract_text_from_file('out.pdf')
        ['Test a.pdf', 'Test b.pdf']
        """

    def extract_text_from_file_with_page_number(self, output_filepath, page_number):
        """
        Extract text from file in self.readers
        :param output_filepath: str, ouput file path to save to
        :param page_number: int, page number to extract text from
        :return pdf_texts: list of str, each element is the text of one pdf file
        >>> handler = PDFHandler(['a.pdf', 'b.pdf'])
        >>> handler.extract_text_from_file_with_page_number('out.pdf', 1)
        ['Test a.pdf', 'Test b.pdf']
        """

    def extract_text_from_file_with_page_number_and_text_length(self, output_filepath, page_number, text_length):
        """
        Extract text from file in self.readers
        :param output_filepath: str, ouput file path to save to
        :param page_number: int, page number to extract text from
        :param text_length: int, text length to extract text from
        :return pdf_texts: list of str, each element is the text of one pdf file
        >>> handler = PDFHandler(['a.pdf', 'b.pdf'])
        >>> handler.extract_text_from_file_with_page_number_and_text_length('out.pdf', 1, 2)
        ['Test a.pdf', 'Test b.pdf']
        """

    def extract_text_from_file_with_page_number_and_text_length_and_text_content(self, output_filepath, page_number, text_length, text_content):
        """
        Extract text from file in self.readers
        :param output_filepath: str, ouput file path to save to
        :param page_number: int, page number to extract text from
        :param text_length: int, text length to extract text from
        :param text_content: str, text content to extract text from
        :return pdf_texts: list of str, each element is the text of one pdf file
        >>> handler = PDFHandler(['a.pdf', 'b.pdf'])
        >>> handler.extract_text_from_file_with_page_number_and_text_length_and_text_content('out.pdf', 1, 2, 'Test a.pdf')
        ['Test a.pdf']
        """

    def extract_text_from_file_with_page_number_and_text_length_and_text_content_and_text_content(self, output_filepath, page_number, text_length, text_content, text_content_2):
        """
        Extract text from file in self.readers
        :param output_filepath: str, ouput file path to save to
        :param page_number: int, page number to extract text from
        :param text_length: int, text length to extract text from
        :param text_content: str, text content to extract text from
        :param text_content_2: str, text content to extract text from
        :return pdf_texts: list of str, each element is the text of one pdf file
        >>> handler = PDFHandler(['a.pdf', 'b.pdf'])
        >>> handler.extract_text_from_file_with_page_number_and_text_length_and_text_content_and_text_content('out.pdf', 1, 2, 'Test a.pdf', 'Test b.pdf')
        ['Test a.pdf', 'Test b.pdf']
        """

    def extract_text_from_file_with_page_number_and_text_length_and_text_content_and_text_content_and_text_content(self, output_filepath, page_number, text_length, text_content, text_content_2, text_content_3):
        """
        Extract text from file in self.readers
        :param output_filepath: str, ouput file path to save to
        :param page_number: int, page number to extract text from
        :param text_length: int, text length to extract text from
        :param text_content: str, text content to extract text from
        :param text_content_2: str, text content to extract text from
        :param text_content_3: str, text content to extract text from
        :return pdf_texts: list of str, each element is the text of one pdf file
        >>> handler = PDFHandler(['