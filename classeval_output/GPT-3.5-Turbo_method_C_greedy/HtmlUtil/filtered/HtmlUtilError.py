import re
import string
import gensim
from bs4 import BeautifulSoup
class HtmlUtil: 
    def __init__(self):
        """
        Initialize a series of labels
        """
        self.SPACE_MARK = '-SPACE-'
        self.JSON_MARK = '-JSON-'
        self.MARKUP_LANGUAGE_MARK = '-MARKUP_LANGUAGE-'
        self.URL_MARK = '-URL-'
        self.NUMBER_MARK = '-NUMBER-'
        self.TRACE_MARK = '-TRACE-'
        self.COMMAND_MARK = '-COMMAND-'
        self.COMMENT_MARK = '-COMMENT-'
        self.CODE_MARK = '-CODE-'

    @staticmethod




    def format_line_html_text(self, html_text):
        soup = BeautifulSoup(html_text, 'html.parser')
        code_tags = soup.find_all('code')
        for code_tag in code_tags:
            code_tag.insert_before(self.CODE_MARK)
        return soup.get_text()
    

    def extract_code_from_html_text(self, html_text):
        soup = BeautifulSoup(html_text, 'html.parser')
        code_elements = soup.find_all('code')
        code_list = [code.get_text() for code in code_elements]
        return code_list