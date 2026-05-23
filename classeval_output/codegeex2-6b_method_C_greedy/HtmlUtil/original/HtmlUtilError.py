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


    @staticmethod
    def __format_line_feed(text):


    def format_line_html_text(self, html_text):
        
        html_text = html_text.replace('\n', ' ')
        html_text = html_text.replace('\r', ' ')
        html_text = html_text.replace('\t', ' ')
        html_text = html_text.replace('\xa0', ' ')
        html_text = html_text.replace('\u3000', ' ')
        html_text = html_text.replace('\u200b', ' ')
        html_text = html_text.replace('\u200e', ' ')
        html_text = html_text.replace('\u202a', ' ')
        html_text = html_text.replace('\u202c', ' ')
        html_text = html_text.replace('\ufeff', ' ')
        html_text = html_text.replace('\uf044', ' ')
        html_text = html_text.replace('\uf048', ' ')
        html_text = html_text.replace('\uf09f', ' ')
        html_text = html_text.replace('\uf0d8', ' ')
        html_text = html_text.replace('\uf0e0', ' ')
        html_text = html_text.replace('\uf0e6', ' ')
        html_text = html_text.replace('\uf0f3', ' ')
        html_text = html_text.replace('\uf0f4', ' ')
        html_text = html_text.replace('\uf0f6', ' ')
        html_text = html_text.replace('\uf0f7', ' ')
        html_text = html_text.replace('\uf0f8', ' ')
        html_text = html_text.replace('\uf0f9', ' ')
        html_text = html_text.replace('\uf0fa', ' ')
        html_text = html_text.replace('\uf0fb', ' ')
        html_text = html_text.replace('\uf0fc', ' ')
        html_text = html_text.replace('\uf0fd', ' ')
        html_text = html_text.replace('\uf0fe', ' ')
        html_text = html_text.replace('\uf0ff', ' ')
        html_text = html_text.replace('\uf100', ' ')
        html_text = html_text.replace('\uf101', ' ')
        html_text = html_text.replace('\uf102', ' ')
        html_text = html_text.replace('\uf103', ' ')
        html_text = html_text.replace('\uf104', ' ')
        html_text = html_text.replace('\uf105', ' ')
        html_text = html_text.replace('\uf106', ' ')
        html_text = html_text.replace('\uf107', ' ')
        html_text = html_text.replace('\uf108', ' ')
        html_text = html_text.replace('\uf109', ' ')
        html_text = html_text.replace('\uf10a', ' ')
        html_text = html_text.replace('\uf10b', ' ')
        html_text = html_text.replace('\uf10c', ' ')
        html_text = html_text.replace('\uf10d', ' ')
        html_text = html_text.replace('\uf10e', ' ')
        html_text = html_text.replace('\uf10f', ' ')
        html_text = html_text.replace('\uf110', ' ')
        html_text = html_text.replace('\uf111', ' ')
        html_text = html_text.replace('\uf112', ' ')
        html_text = html_text.replace('\uf113', ' ')
        html_text = html_text.replace('\uf114', ' ')
        html_text = html_text.replace('\uf115', ' ')
        html_text = html_text.replace('\uf116', ' ')
        html_text = html_text.replace('\uf117', ' ')
        html_text = html_text.replace('\uf118', ' ')
        html_text = html_text.replace('\uf119', ' ')
        html_text = html_text.replace('\uf11a', ' ')
        html_text = html_text.replace('\uf11b', ' ')
        html_text = html_text.replace('\uf11c', ' ')
        html_text = html_text.replace('\uf11d', ' ')
        html_text = html_text.replace('\uf11e', ' ')
        html_text = html_text.replace('\uf11f', ' ')
        html_text = html_text.replace('\uf120', ' ')
        html_text = html_text.replace('\uf121', ' ')
        html_text = html_text.replace('\uf122', ' ')
        html_text = html_text.replace('\uf123', ' ')
        html_text = html_text.replace('\uf124', ' ')
        html_text = html_text.replace('\uf125', ' ')
        html_text = html_text.replace('\uf126', ' ')
        html_text = html_text.replace('\uf127', ' ')
        html_text = html_text.replace('\uf128', ' ')
        html_text = html_text.replace('\uf129', ' ')
        html_text = html_text.replace('\uf12a', ' ')
        html_text


    def extract_code_from_html_text(self, html_text):
        
        soup = BeautifulSoup(html_text, 'html.parser')
        code_list = []
        for code in soup.find_all('pre'):
            code_list.append(code.text)
        return code_list
