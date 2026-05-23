import re
import string
import gensim
from bs4 import BeautifulSoup
class HtmlUtil:  
    """
    This is a class as util for html, supporting for formatting and extracting code from HTML text, including cleaning up the text and converting certain elements into specific marks.
    """

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


    @staticmethod
    def __format_line_feed(text):
        
        return text.replace('\n', ' ')

    @staticmethod


    def __format_code(text):


    def format_line_html_text(self, html_text):


    def extract_code_from_html_text(self, html_text):