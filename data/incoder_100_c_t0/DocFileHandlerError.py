class DocFileHandler:  
    """
    This is a class that handles Word documents and provides functionalities for reading, writing, and modifying the content of Word documents.
    """

    def __init__(self, file_path):
        """
        Initializes the DocFileHandler object with the specified file path.
        :param file_path: str, the path to the Word document file.
        """
        self.file_path = file_path


    def read_text(self):
        """
        Reads the content of a Word document and returns it as a string.
        :return: str, the content of the Word document.
        """
        doc = Document(self.file_path)
        return doc.text

    def write_text(self, content, font_size=12, alignment='left'):
        """
        Writes the specified content to a Word document.
        :param content: str, the text content to write.
        :param font_size: int, optional, the font size of the text (default is 12).
        :param alignment: str, optional, the alignment of the text ('left', 'center', or 'right'; default is 'left').
        :return: bool, True if the write operation is successful, False otherwise.
        """
        doc = Document(self.file_path)
        doc.add_paragraph(content, font_size=font_size, alignment=alignment)
        return doc.save(self.file_path)

    def add_heading(self, heading, level=1):
        """
        Adds a heading to the Word document.
        :param heading: str, the text of the heading.
        :param level: int, optional, the level of the heading (1, 2, 3, etc.; default is 1).
        :return: bool, True if the heading is successfully added, False otherwise.
        """
        doc = Document(self.file_path)
        doc.add_heading(heading, level)
        return doc.save(self.file_path)

    def add_paragraph(self, content, font_size=12, alignment='left'):
        """
        Adds a paragraph to the Word document.
        :param content: str, the text of the paragraph.
        :param font_size: int, optional, the font size of the text (default is 12).
        :param alignment: str, optional, the alignment of the text ('left', 'center', or 'right'; default is 'left').
        :return: bool, True if the paragraph is successfully added, False otherwise.
        """
        doc = Document(self.file_path)
        doc.add_paragraph(content, font_size=font_size, alignment=alignment)
        return doc.save(self.file_path)

    def add_table(self, data):
        """
        Adds a table to the Word document with the specified data.
        :param data: list of lists, the data to populate the table.
        :return: bool, True if the table is successfully added, False otherwise.
        """
        doc = Document(self.file_path)
        doc.add_table(data)
        return doc.save(self.file_path)

    def add_image(self, image_path):
        """
        Adds an image to the Word document.
        :param image_path: str, the path to the image file.
        :return: bool, True if the image is successfully added, False otherwise.
        """
        doc = Document(self.file_path)
        doc.add_image(image_path)
        return doc.save(self.file_path)

    def add_table_data(self, table_data):
        """
        Adds data to the table in the Word document.
        :param table_data: list of lists, the data to populate the table.
        :return: bool, True if the table data is successfully added, False otherwise.
        """
        doc = Document(self.file_path)
        doc.add_table_data(table_data)
        return doc.save(self.file_path)

    def _get_alignment_value(self, alignment):
        """
        Returns the alignment value corresponding to the given alignment string.
        :param alignment: str, the alignment string ('left', 'center', or 'right').
        :return: int, the alignment value.
        """
        alignments = {
            'left': 0,
            'center': 1,
            'right': 2
        }
        return alignments[alignment]