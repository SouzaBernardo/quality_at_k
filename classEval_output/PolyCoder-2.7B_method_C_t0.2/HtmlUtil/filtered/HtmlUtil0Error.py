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
        return re.sub(self.SPACE_MARK,'', text)


    def format_line_html_text(self, html_text):
        """
        get the html text without the code, and add the code tag -CODE- where the code is
        :param html_text:string
        :return:string
        >>>htmlutil = HtmlUtil()
        >>>htmlutil.format_line_html_text(<html>
        >>> <body>
        >>>    <h1>Title</h1>
        >>>    <p>This is a paragraph.</p>
        >>>    <pre>print('Hello, world!')</pre>
        >>>    <p>Another paragraph.</p>
        >>>    <pre><code>for i in range(5):
        >>>    print(i)</code></pre>
        >>>    </body>
        >>>    </html>)
        Title
        This is a paragraph.
        -CODE-
        Another paragraph.
        -CODE-
        """
        if html_text:
            html_text = html_text.replace('\n', '<br />')
            html_text = re.sub(r'(?s)<br\s*/?>', self.SPACE_MARK, html_text)
            html_text = re.sub(r'(?s)<br\s*/?>', self.JSON_MARK, html_text)
            html_text = re.sub(r'(?s)<br\s*/?>', self.MARKUP_LANGUAGE_MARK, html_text)
            html_text = re.sub(r'(?s)<br\s*/?>', self.URL_MARK, html_text)
            html_text = re.sub(r'(?s)<br\s*/?>', self.NUMBER_MARK, html_text)
            html_text = re.sub(r'(?s)<br\s*/?>', self.TRACE_MARK, html_text)
            html_text = re.sub(r'(?s)<br\s*/?>', self.COMMAND_MARK, html_text)
            html_text = re.sub(r'(?s)<br\s*/?>', self.COMMENT_MARK, html_text)
            html_text = re.sub(r'(?s)<br\s*/?>', self.CODE_MARK, html_text)
        return html_text


    def extract_code_from_html_text(self, html_text):
        """
        extract codes from the html body
        :param html_text: string, html text
        :return: the list of code
        >>>htmlutil = HtmlUtil()
        >>>htmlutil.extract_code_from_html_text(<html>
        >>> <body>
        >>>    <h1>Title</h1>
        >>>    <p>This is a paragraph.</p>
        >>>    <pre>print('Hello, world!')</pre>
        >>>    <p>Another paragraph.</p>
        >>>    <pre><code>for i in range(5):
        >>>    print(i)</code></pre>
        >>>    </body>
        >>>    </html>)
        ["print('Hello, world!')", 'for i in range(5):\n                print(i)']
        """
        code_list = []
        for i in range(len(html_text)):
            if html_text[i] == self.SPACE_MARK:
                code_list.append(' ')
            elif html_text[i] == self.JSON_MARK:
                code_list.append('JSON')
            elif html_text[i] == self.MARKUP_LANGUAGE_MARK:
                code_list.append('MARKUP_LANGUAGE')
            elif html_text[i] == self.URL_MARK:
                code_list.append('URL')
            elif html_text[i] == self.NUMBER_MARK:
                code_list.append('NUMBER')
            elif html_text[i] == self.TRACE_MARK:
                code_list.append('TRACE')
            elif html_text[i] == self.COMMAND_MARK:
                code_list.append('COMMAND')
            elif html_text[i] == self.COMMENT_MARK:
                code_list.append('COMMENT')
            elif html_text[i] == self.CODE_MARK:
                code_list.append('CODE')
            else:
                code_list.append(html_text[i])
        return code_list