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
        :param file_path: str, path to file to extract text from
        :return text: str, text extracted from file
        >>> handler = PDFHandler(['a.pdf', 'b.pdf'])
        >>> handler.extract_text_from_file('out.pdf')
        'Test a.pdf'
        """

    def extract_text_from_file_and_save(self, file_path):
        """
        Extract text from file in self.readers
        :param file_path: str, path to file to extract text from
        :return text: str, text extracted from file
        >>> handler = PDFHandler(['a.pdf', 'b.pdf'])
        >>> handler.extract_text_from_file_and_save('out.pdf')
        'Test a.pdf'
        """

    def extract_text_from_file_and_save_to_disk(self, file_path):
        """
        Extract text from file in self.readers
        :param file_path: str, path to file to extract text from
        :return text: str, text extracted from file
        >>> handler = PDFHandler(['a.pdf', 'b.pdf'])
        >>> handler.extract_text_from_file_and_save_to_disk('out.pdf')
        'Test a.pdf'
        """

    def extract_text_from_file_and_save_to_disk_and_save(self, file_path):
        """
        Extract text from file in self.readers
        :param file_path: str, path to file to extract text from
        :return text: str, text extracted from file
        >>> handler = PDFHandler(['a.pdf', 'b.pdf'])
        >>> handler.extract_text_from_file_and_save_to_disk_and_save('out.pdf')
        'Test a.pdf'
        """

    def extract_text_from_file_and_save_to_disk_and_save_to_disk(self, file_path):
        """
        Extract text from file in self.readers
        :param file_path: str, path to file to extract text from
        :return text: str, text extracted from file
        >>> handler = PDFHandler(['a.pdf', 'b.pdf'])
        >>> handler.extract_text_from_file_and_save_to_disk_and_save_to_disk('out.pdf')
        'Test a.pdf'
        """

    def extract_text_from_file_and_save_to_disk_and_save_to_disk_and_save(self, file_path):
        """
        Extract text from file in self.readers
        :param file_path: str, path to file to extract text from
        :return text: str, text extracted from file
        >>> handler = PDFHandler(['a.pdf', 'b.pdf'])
        >>> handler.extract_text_from_file_and_save_to_disk_and_save_to_disk_and_save('out.pdf')
        'Test a.pdf'
        """

    def extract_text_from_file_and_save_to_disk_and_save_to_disk_and_save_to_disk(self, file_path):
        """
        Extract text from file in self.readers
        :param file_path: str, path to file to extract text from
        :return text: str, text extracted from file
        >>> handler = PDFHandler(['a.pdf', 'b.pdf'])
        >>> handler.extract_text_from_file_and_save_to_disk_and_save_to_disk_and_save_to_disk('out.pdf')
        'Test a.pdf'
        """

    def extract_text_from_file_and_save_to_disk_and_save_to_disk_and_save_to_disk_and_save(self, file_path):
        """
        Extract text from file in self.readers
        :param file_path: str, path to file to extract text from
        :return text: str, text extracted from file
        >>> handler = PDFHandler(['a.pdf', 'b.pdf'])
        >>> handler.extract_text_from_file_and_save_to_disk_and_save_to_disk_and_save_to_disk_and_save('out.pdf')
        'Test a.pdf'
        """

    def extract_text_from_file_and_save_to_disk_and_save_to_disk_and_save_to_disk_and_save_to_disk(self, file_path):
        """
        Extract text from file in self.readers