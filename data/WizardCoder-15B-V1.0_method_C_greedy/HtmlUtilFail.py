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


    def __format_line_feed(text):
        """
        Replace consecutive line breaks with a single line break
        :param text: string with consecutive line breaks
        :return:string, replaced text with single line break
        """
        return re.sub(r'\n+', '\n', text)

    def format_line_html_text(self, html_text):
        """
        get the html text without the code, and add the code tag -CODE- where the code is
        :param html_text:string
        :return:string
        """
        soup = BeautifulSoup(html_text, 'html.parser')
        # remove code blocks
        for code_block in soup.find_all('code'):
            code_block.decompose()
        # remove comments
        for comment in soup.find_all(string=lambda text: isinstance(text, Comment)):
            comment.extract()
        # remove script and style tags
        for script in soup.find_all('script'):
            script.decompose()
        for style in soup.find_all('style'):
            style.decompose()
        # remove attributes
        for tag in soup.find_all():
            tag.attrs = {}
        # remove tags
        for tag in soup.find_all():
            tag.unwrap()
        # remove multiple spaces
        text = re.sub(r'\s+','', soup.get_text())
        # replace line feed with space
        text = self.__format_line_feed(text)
        # remove punctuation
        text = text.translate(str.maketrans('', '', string.punctuation))
        # remove stop words
        stop_words = gensim.parsing.preprocessing.STOPWORDS
        text =''.join([word for word in text.split() if word not in stop_words])
        # add code tag
        code_text = self.extract_code_from_html_text(html_text)
        code_text = self.__format_line_feed(code_text)
        code_text = self.CODE_MARK + code_text
        # combine text and code
        text = text +'' + code_text
        # remove multiple spaces
        text = re.sub(r'\s+','', text)
        return text

    def extract_code_from_html_text(self, html_text):
        """
        Extract codes from the html body
        :param html_text: string, html text
        :return: the list of code
        """
        soup = BeautifulSoup(html_text, 'html.parser')
        code_blocks = soup.find_all('code')
        code_list = []
        for code_block in code_blocks:
            code = code_block.get_text()
            code_list.append(code)
        return code_list