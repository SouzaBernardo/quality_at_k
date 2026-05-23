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
            pdf = reader.getPage(0)
            pdf.update()
            pdf.mergePage(reader.getPage(1))
            output_file = PyPDF2.PdfFileWriter()
            output_file.addPage(pdf)
            output_filepath = output_filepath + '/' + reader.getFileName()
            output_file.write(output_filepath)

    def extract_text_from_pdfs(self):
        """
        Extract text from pdf files in self.readers
        :return pdf_texts: list of str, each element is the text of one pdf file
        >>> handler = PDFHandler(['a.pdf', 'b.pdf'])
        >>> handler.extract_text_from_pdfs()
        ['Test a.pdf', 'Test b.pdf']
        """
        text_list = []
        for reader in self.readers:
            text = reader.getPage(0).extractText()
            text_list.append(text)
        return text_list

Merge PDFs:

handler = PDFHandler(['a.pdf', 'b.pdf'])
handler.merge_pdfs('out.pdf')

Extract Text:

handler = PDFHandler(['a.pdf', 'b.pdf'])
handler.extract_text_from_pdfs()