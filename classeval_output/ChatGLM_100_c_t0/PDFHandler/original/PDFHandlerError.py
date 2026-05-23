Here is the completed `PDFHandler` class:
```python
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
            with open(reader.get_pdf_file(), 'rb') as f:
                pdf_content = f.read()
            pdf_content = PyPDF2.PdfFileReader.parse(pdf_content)
            pdf_page_number = 0
            for i in range(pdf_content.getNumPages()):
                pdf_page = pdf_content.getPage(i)
                pdf_text = pdf_page.extractText()
                pdf_page_number += 1
                output_path = f"{output_filepath}.pdf"
                with open(output_path, 'wb') as f:
                    f.write(pdf_content.getPageTextStream(pdf_page_number, pdf_page.getPageTextEncoding())
                print(f"Merged PDFs saved at {output_path}")
        return output_path

    def extract_text_from_pdfs(self):
        """
         Extract text from pdf files in self.readers
        :return pdf_texts: list of str, each element is the text of one pdf file
        >>> handler = PDFHandler(['a.pdf', 'b.pdf'])
        >>> handler.extract_text_from_pdfs()
        ['Test a.pdf', 'Test b.pdf']
        """
        for reader in self.readers:
            with open(reader.get_pdf_file(), 'rb') as f:
                pdf_content = f.read()
            pdf_content = PyPDF2.PdfFileReader.parse(pdf_content)
            pdf_page_number = 0
            for i in range(pdf_content.getNumPages()):
                pdf_page = pdf_content.getPage(i)
                pdf_text = pdf_page.extractText()
                pdf_texts.append(pdf_text)
        return pdf_texts
```