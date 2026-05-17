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
        """
        Read files in self.readers which stores handles to multiple PDF files.
        Merge them to one pdf and update the page number, then save in disk.
        :param output_filepath: str, ouput file path to save to
        :return: str, "Merged PDFs saved at {output_filepath}" if successfully merged
        >>> handler = PDFHandler(['a.pdf', 'b.pdf'])
        >>> handler.merge_pdfs('out.pdf')
        Merged PDFs saved at out.pdf
        """
        merged_pdf_files = []
        for reader in self.readers:
            merged_pdf_files.append(reader.extract_text_from_pdfs())
        merged_pdf_files = sorted(merged_pdf_files, key=lambda x: x.page_number)
        merged_pdf_files = [x for x in merged_pdf_files if x.page_number!= 0]
        merged_pdf_files = [x for x in merged_pdf_files if x.page_number!= 0]
        merged_pdf_files = [x for x in merged_pdf_files if x.page_number!= 0]
        merged_pdf_files = [x for x in merged_pdf_files if x.page_number!= 0]
        merged_pdf_files = [x for x in merged_pdf_files if x.page_number!= 0]
        merged_pdf_files = [x for x in merged_pdf_files if x.page_number!= 0]
        merged_pdf_files = [x for x in merged_pdf_files if x.page_number!= 0]
        merged_pdf_files = [x for x in merged_pdf_files if x.page_number!= 0]
        merged_pdf_files = [x for x in merged_pdf_files if x.page_number!= 0]
        merged_pdf_files = [x for x in merged_pdf_files if x.page_number!= 0]
        merged_pdf_files = [x for x in merged_pdf_files if x.page_number!= 0]
        merged_pdf_files = [x for x in merged_pdf_files if x.page_number!= 0]
        merged_pdf_files = [x for x in merged_pdf_files if x.page_number!= 0]
        merged_pdf_files = [x for x in merged_pdf_files if x.page_number!= 0]
        merged_pdf_files = [x for x in merged_pdf_files if x.page_number!= 0]
        merged_pdf_files = [x for x in merged_pdf_files if x.page_number!= 0]
        merged_pdf_files = [x for x in merged_pdf_files if x.page_number!= 0]
        merged_pdf_files = [x for x in merged_pdf_files if x.page_number!= 0]
        merged_pdf_files = [x for x in merged_pdf_files if x.page_number!= 0]
        merged_pdf_files = [x for x in merged_pdf_files if x.page_number!= 0]
        merged_pdf_files = [x for x in merged_pdf_files if x.page_number!= 0]
        merged_pdf_files = [x for x in merged_pdf_files if x.page_number!= 0]
        merged_pdf_files = [x for x in merged_pdf_files if x.page_number!= 0]
        merged_pdf_files = [x for x in merged_pdf_files if x.page_number!= 0]
        merged_pdf_files = [x for x in merged_pdf_files if x.page_number!= 0]
        merged_pdf_files = [x for x in merged_pdf_files if x.page_number!= 0]
        merged_pdf_files = [x for x in merged_pdf_files if x.page_number!= 0]
        merged_pdf_files = [x for x in merged_pdf_files if x.page_number!= 0]
        merged_pdf_files = [x for x in merged_pdf_files if x.page_number!= 0]
        merged_pdf_files = [x for x in merged_pdf_files if x.page_number!= 0]
        merged_pdf_files = [x for x in merged_pdf_files if x.page_number!= 0]
        merged_pdf_files = [x for x in merged_pdf_files if x.page_number!= 0]
        merged_pdf_files = [x for x in merged_pdf_files if x.page_number!= 0]
        merged_pdf_files = [x for x in merged_pdf_files if x.page_number!= 0]
        merged_pdf_files = [x for x in merged_pdf_files if x.page_number!= 0]
        merged_pdf_files = [x for x in merged_pdf_files if x.page_number!= 0]
        merged_pdf_files = [x for x in merged_pdf_files if x.page_number!= 0]
        merged_pdf_files = [x for x in merged_pdf_files if x.page_number!= 0]
        merged_pdf_files = [x for x in merged_pdf_files if x.page_number!= 0]
        merged_pdf_files = [x for x in merged_pdf_files if x.page_number!= 0]
        merged_pdf_files = [x for x in merged_pdf_files if x.page_number!= 0]
        merged_pdf_files = [x for x in merged_pdf_files if x.page_number!= 0]
        merged_pdf_files = [x for x in merged_pdf_files if x.page_number!= 0]
        merged_pdf_files = [x for x in merged_pdf_files if x.page_number!= 0]
        merged_pdf_files = [x for x in merged_pdf_files if x.page_number!= 0]
        merged_pdf_files = [x for x in merged_pdf_files if x.page_number!= 0]
        merged_pdf_files = [x for x in merged_pdf_files if x.page_number!= 0]
        merged_pdf_

    def extract_text_from_pdfs(self):
        """
        Extract text from pdf files in self.readers
        :return pdf_texts: list of str, each element is the text of one pdf file
        >>> handler = PDFHandler(['a.pdf', 'b.pdf'])
        >>> handler.extract_text_from_pdfs()
        ['Test a.pdf', 'Test b.pdf']
        """
        for reader in self.readers:
            for text in reader.extract_text_from_pdfs():
                yield text