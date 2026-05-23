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
        """
        for fp in self.readers:
            with open(output_filepath, 'wb') as f:
                f.write(fp.getPageData(0))
            output_page_number = 1
            for fp in self.readers:
                with open(output_filepath, 'rb') as f:
                    page_data = f.read()
                    output_page_number += 1
                    if output_page_number >= len(self.readers):
                        break
                    f.write(page_data[:output_page_number * 4])
            print(f"Merged PDFs saved at {output_filepath}")

    def extract_text_from_pdfs(self):
        """
        Extract text from pdf files in self.readers
        :return pdf_texts: list of str, each element is the text of one pdf file
        >>> handler = PDFHandler(['a.pdf', 'b.pdf'])
        >>> handler.extract_text_from_pdfs()
        ['Test a.pdf', 'Test b.pdf']
        """
        pdf_texts = []
        for fp in self.readers:
            pdf_texts.append(fp.extractText())
        return pdf_texts