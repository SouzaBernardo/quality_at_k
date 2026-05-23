from docx import Document
from docx.shared import Pt
from docx.enum.text import WD_PARAGRAPH_ALIGNMENT


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

    def write_text(self, content, font_size=12, alignment='left'):
        """
        Writes the specified content to a Word document.
        :param content: str, the text content to write.
        :param font_size: int, optional, the font size of the text (default is 12).
        :param alignment: str, optional, the alignment of the text ('left', 'center', or 'right'; default is 'left').
        :return: bool, True if the write operation is successful, False otherwise.
        """

    def add_heading(self, heading, level=1):
        """
        Adds a heading to the Word document.
        :param heading: str, the text of the heading.
        :param level: int, optional, the level of the heading (1, 2, 3, etc.; default is 1).
        :return: bool, True if the heading is successfully added, False otherwise.
        """

    def add_table(self, data):
        """
        Adds a table to the Word document with the specified data.
        :param data: list of lists, the data to populate the table.
        :return: bool, True if the table is successfully added, False otherwise.
        """

    def _get_alignment_value(self, alignment):
        """
        Returns the alignment value corresponding to the given alignment string.
        :param alignment: str, the alignment string ('left', 'center', or 'right').
        :return: int, the alignment value.
        """
        if alignment == 'left':
            return WD_PARAGRAPH_ALIGNMENT.LEFT
        elif alignment == 'center':
            return WD_PARAGRAPH_ALIGNMENT.CENTER
        elif alignment == 'right':
            return WD_PARAGRAPH_ALIGNMENT.RIGHT
        else:
            return WD_PARAGRAPH_ALIGNMENT.JUSTIFIED

    def _get_paragraph_style(self, font_size, alignment):
        """
        Returns the paragraph style corresponding to the given font size and alignment.
        :param font_size: int, the font size of the paragraph (default is 12).
        :param alignment: str, the alignment of the paragraph ('left', 'center', or 'right'; default is 'left').
        :return: docx.enum.style.ParagraphStyle, the paragraph style.
        """
        paragraph_style = docx.enum.style.ParagraphStyle()
        paragraph_style.font.name = 'Arial'
        paragraph_style.font.size = Pt(font_size)
        paragraph_style.alignment = self._get_alignment_value(alignment)
        return paragraph_style

    def _get_table_style(self, font_size, alignment):
        """
        Returns the table style corresponding to the given font size and alignment.
        :param font_size: int, the font size of the table (default is 12).
        :param alignment: str, the alignment of the table ('left', 'center', or 'right'; default is 'left').
        :return: docx.enum.style.TableStyle, the table style.
        """
        table_style = docx.enum.style.TableStyle()
        table_style.name = 'TableStyleMedium1'
        table_style.font.name = 'Arial'
        table_style.font.size = Pt(font_size)
        table_style.alignment = self._get_alignment_value(alignment)
        return table_style

    def _get_table_cell_style(self, font_size, alignment):
        """
        Returns the table cell style corresponding to the given font size and alignment.
        :param font_size: int, the font size of the table cell (default is 12).
        :param alignment: str, the alignment of the table cell ('left', 'center', or 'right'; default is 'left').
        :return: docx.enum.style.TableCellStyle, the table cell style.
        """
        table_cell_style = docx.enum.style.TableCellStyle()
        table_cell_style.font.name = 'Arial'
        table_cell_style.font.size = Pt(font_size)
        table_cell_style.alignment = self._get_alignment_value(alignment)
        return table_cell_style

    def _get_table_row_style(self, font_size, alignment):
        """
        Returns the table row style corresponding to the given font size and alignment.
        :param font_size: int, the font size of the table row (default is 12).
        :param alignment: str, the alignment of the table row ('left', 'center', or 'right'; default is 'left').
        :return: docx.enum.style.TableRowStyle, the table row style.
        """
        table_row_style = docx.enum.style.TableRowStyle()
        table_row_style.font.name = 'Arial'
        table_row_style.font.size = Pt(font_size)
        table_row_style.alignment = self._get_alignment_value(alignment)
        return table_row_style

    def _get_table_column_style(self, font_size, alignment):
        """
        Returns the table column style corresponding to the given font size and alignment.
        :param font_size: int, the font size of the table column (default is 12).
        :param alignment: str, the alignment of the table column ('left', 'center', or 'right'; default is 'left').
        :return: docx.enum.style.TableColumnStyle, the table column style.
        """
        table_column_style = docx.enum.style.TableColumnStyle()
        table_column_style.font.name = 'Arial'
        table_column_style.font.size = Pt(font_size)
        table_column_style.alignment = self._get_alignment_value(alignment)
        return table_column_style

    def _get_table_header_style(self, font_size, alignment):
        """
        Returns the table header style corresponding to the given font size and alignment.
        :param font_size: int, the font size of the table header (default is 12).
        :param alignment: str, the alignment of the table header ('left', 'center', or 'right'; default is 'left').
        :return: docx.enum.style.TableHeaderStyle, the table header style.
        """
        table_header_style = docx.enum.style.TableHeaderStyle()
        table_header_style.font.name = 'Arial'
        table_header_style.font.size = Pt(font_size)
        table_header_style.alignment = self._get_alignment_value(alignment)
        return table_header_style

    def _get_table_footer_style(self, font_size, alignment):
        """
        Returns the table footer style corresponding to the given font size and alignment.
        :param font_size: int, the font size of the table footer (default is 12).
        :param alignment: str, the alignment of the table footer ('left', 'center', or 'right'; default is 'left').
        :return: docx.enum.style.TableFooterStyle, the table footer style.
        """
        table_footer_style = docx.enum.style.TableFooterStyle()
        table_footer_style.font.name = 'Arial'
        table_footer_style.font.size = Pt(font_size)
        table_footer_style.alignment = self._get_alignment_value(alignment)
        return table_footer_style

    def _get_table_row_background_style(self, background_color):
        """
        Returns the table row background style corresponding to the given background color.
        :param background_color: str, the background color of the table row (default is 'FFFFFF').
        :return: docx.enum.style.TableRowBackgroundStyle, the table row background style.
        """
        table_row_background_style = docx.enum.style.TableRowBackgroundStyle()
        table_row_background_style.fill.fgColor = docx.enum.color.Color(background_color)
        return table_row_background_style

    def _get_table_column_background_style(self, background_color):
        """
        Returns the table column background style corresponding to the given background color.
        :param background_color: str, the background color of the table column (default is 'FFFFFF').
        :return: docx.enum.style.TableColumnBackgroundStyle, the table column background style.
        """
        table_column