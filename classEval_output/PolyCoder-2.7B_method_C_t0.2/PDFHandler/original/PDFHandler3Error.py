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
        # open files in self.readers
        for reader in self.readers:
            # open file in reader
            fp = reader.open()
            # write to file
            fp.write(output_filepath)
            # close file
            fp.close()
            # update page number
            self.update_page_number(fp)
            # save file
            fp.close()
            # update page number
            self.update_page_number(fp)
            # save file
            fp.close()
            # update page number
            self.update_page_number(fp)
            # save file
            fp.close()
            # update page number
            self.update_page_number(fp)
            # save file
            fp.close()
            # update page number
            self.update_page_number(fp)
            # save file
            fp.close()
            # update page number
            self.update_page_number(fp)
            # save file
            fp.close()
            # update page number
            self.update_page_number(fp)
            # save file
            fp.close()
            # update page number
            self.update_page_number(fp)
            # save file
            fp.close()
            # update page number
            self.update_page_number(fp)
            # save file
            fp.close()
            # update page number
            self.update_page_number(fp)
            # save file
            fp.close()
            # update page number
            self.update_page_number(fp)
            # save file
            fp.close()
            # update page number
            self.update_page_number(fp)
            # save file
            fp.close()
            # update page number
            self.update_page_number(fp)
            # save file
            fp.close()
            # update page number
            self.update_page_number(fp)
            # save file
            fp.close()
            # update page number
            self.update_page_number(fp)
            # save file
            fp.close()
            # update page number
            self.update_page_number(fp)
            # save file
            fp.close()
            # update page number
            self.update_page_number(fp)
            # save file
            fp.close()
            # update page number
            self.update_page_number(fp)
            # save file
            fp.close()
            # update page number
            self.update_page_number(fp)
            # save file
            fp.close()
            # update page number
            self.update_page_number(fp)
            # save file
            fp.close()
            # update page number
            self.update_page_number(fp)
            # save file
            fp.close()
            # update page number
            self.update_page_number(fp)
            # save file
            fp.close()
      

    def extract_text_from_pdfs(self):
        """
        Extract text from pdf files in self.readers
        :return pdf_texts: list of str, each element is the text of one pdf file
        >>> handler = PDFHandler(['a.pdf', 'b.pdf'])
        >>> handler.extract_text_from_pdfs()
        ['Test a.pdf', 'Test b.pdf']
        """
        for reader in self.readers:
            for text in reader.extract_text():
                yield text


