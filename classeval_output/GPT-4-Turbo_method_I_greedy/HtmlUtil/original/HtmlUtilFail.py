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



    def __format_line_feed(text):
        """
        Replace consecutive line breaks with a single line break
        :param text: string with consecutive line breaks
        :return:string, replaced text with single line break
        """
        return re.sub('\n+', '\n', text)
    def format_line_html_text(self, html_text):
        """
        get the html text without the code, and add the code tag -CODE- where the code is
        :param html_text:string
        :return:string
        """
        soup = BeautifulSoup(html_text, 'html.parser')
    
        # Replace all <pre> tags with the code mark
        for pre in soup.find_all('pre'):
            pre.replace_with(self.CODE_MARK)
    
        # Get the text from the soup object, replacing line breaks with spaces
        text = soup.get_text(separator=' ')
    
        # Format the line breaks in the text
        text = self.__format_line_feed(text)
    
        return text
    def extract_code_from_html_text(self, html_text):
        """
        extract codes from the html body
        :param html_text: string, html text
        :return: the list of code
        """
        soup = BeautifulSoup(html_text, 'html.parser')
        code_list = []
    
        # Find all <pre> tags in the soup object
        for pre in soup.find_all('pre'):
            # If the <pre> tag contains a <code> tag, get the text from the <code> tag
            if pre.code:
                code_list.append(pre.code.get_text())
            # If the <pre> tag does not contain a <code> tag, get the text from the <pre> tag
            else:
                code_list.append(pre.get_text())
    
        return code_list
    
