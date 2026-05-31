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

    def __format_line_feed(text):
        """
        Replace consecutive line breaks with a single line break
        :param text: string with consecutive line breaks
        :return:string, replaced text with single line break
        """
        lines = text.split('\n')
        formatted_text = ''
        for line in lines:
            formatted_text += line + '\n'
        return formatted_text

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
        soup = BeautifulSoup(html_text, 'html.parser')
        html_text = soup.get_text()
        html_text = HtmlUtil.__format_line_feed(html_text)
        html_text = html_text.replace('\t', '    ')
        html_text = html_text.replace('\n', ' ')
        html_text = html_text.replace('\r', ' ')
        html_text = html_text.replace(' ', ' ')
        html_text = html_text.replace('-CODE-', '-CODE-')
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
        soup = BeautifulSoup(html_text, 'html.parser')
        html_text = soup.get_text()
        html_text = HtmlUtil.__format_line_feed(html_text)
        html_text = html_text.replace('\t', '    ')
        html_text = html_text.replace('\n', ' ')
        html_text = html_text.replace('\r', ' ')
        html_text = html_text.replace(' ', ' ')
        html_text = html_text.replace('-CODE-', '-CODE-')
        html_text = html_text.replace('-SPACE-', '-SPACE-')
        html_text = html_text.replace('-JSON-', '-JSON-')
        html_text = html_text.replace('-MARKUP_LANGUAGE-', '-MARKUP_LANGUAGE-')
        html_text = html_text.replace('-URL-', '-URL-')
        html_text = html_text.replace('-NUMBER-', '-NUMBER-')
        html_text = html_text.replace('-TRACE-', '-TRACE-')
        html_text = html_text.replace('-COMMAND-', '-COMMAND-')
        html_text = html_text.replace('-COMMENT-', '-COMMENT-')
        html_text = html_text.replace('-SPACE-', '-SPACE-')
        html_text = html_text.replace('-SPACE-', '-SPACE-')
        html_text = html_text.replace('-SPACE-', '-SPACE-')
        html_text = html_text.replace('-SPACE-', '-SPACE-')
        html_text = html_text.replace('-SPACE-', '-SPACE-')
        html_text = html_text.replace('-SPACE-', '-SPACE-')
        html_text = html_text.replace('-SPACE-', '-SPACE-')
        html_text = html_text.replace('-SPACE-', '-SPACE-')
        html_text = html_text.replace('-SPACE-', '-SPACE-')
        html_text = html_text.replace('-SPACE-', '-SPACE-')
        html_text = html_text.replace('-SPACE-', '-SPACE-')
        html_text = html_text.replace('-SPACE-', '-SPACE-')
        html_text = html_text.replace('-SPACE-', '-SPACE-')
        html_text = html_text.replace('-SPACE-', '-SPACE-')
        html_text = html_text.replace('-SPACE-', '-SPACE-')
        html_text = html_text.replace('-SPACE-', '-SPACE-')
        html_text = html_text.replace('-SPACE-', '-SPACE-')
        html_text = html_text.replace('-SPACE-', '-SPACE-')
        html_text = html_text.replace('-SPACE-', '-SPACE-')
        html_text = html_text.replace('-SPACE-', '-SPACE-')
        html_text = html_text.replace('-SPACE-', '-SPACE-')
        html_text = html_text.replace('-SPACE-', '-SPACE-')
        html_text = html_text.replace('-SPACE-', '-SPACE-')
        html_text = html_text.replace('-SPACE-', '-SPACE-')
        html_text = html_text.replace('-SPACE-', '-SPACE-')
        html_text = html_text.replace('-SPACE-', '-SPACE-')
        html_text = html_text.replace('-SPACE-', '-SPACE-')
        html_text = html_text.replace('-SPACE-', '-SPACE-')
        html_text = html_text.replace('-SPACE-', '-SPACE-')
        html_text = html_text.replace('-SPACE-', '-SPACE-')
        html_text = html_text.replace('-SPACE-', '-SPACE-')
        html_text = html_text.replace('-SPACE-', '-SPACE-')
        html_text = html_text.replace('-SPACE-', '-SPACE-')
        html_text = html_text.replace('-SPACE-', '-SPACE-')
        html_text = html_text.replace('-SPACE-', '-SPACE-')
        html_text = html_text.replace('-SPACE-', '-SPACE-')
        html_text = html_text.replace('-SPACE-', '-SPACE-')
        html_text = html_text.replace('-SPACE-', '-SPACE-')
        html_text = html_text.replace('-SPACE-', '-SPACE-')
        html_text = html_text.replace('-SPACE-', '-SPACE-')
        html_text = html_text.replace('-SPACE-', '-SPACE-')
        html_text = html_text.replace('-SPACE-', '-SPACE-')
        html_text = html_text.replace('-SPACE-', '-SPACE-')
        html_text = html_text.replace('-SPACE-', '-SPACE-')
        html_text = html_text.replace('-SPACE-', '-SPACE-')
        html_text = html_text.replace('-SPACE-', '-SPACE-')
        html_text = html_text.replace('-SPACE-', '-SPACE-')
        html_text = html_text.replace('-SPACE-', '-SPACE-')
        html_text = html_text.replace('-SPACE-', '-SPACE-')
        html_text = html_text.replace('-SPACE-', '-SPACE-')
        html_text = html_text.replace('-SPACE-', '-SPACE-')
        html_text = html_text.replace('-SPACE-', '-SPACE-')
        html_text = html_text.replace('-SPACE-', '-SPACE-')
        html_text = html_text.replace('-SPACE-', '-SPACE-')
        html_text = html_text.replace('-SPACE-', '-SPACE-')
        html_text = html_text.replace('-SPACE-', '-SPACE-')
        html_text = html_text.replace('-SPACE-', '-SPACE-')
        html_text = html_text.replace('-SPACE-', '-SPACE-')
        html_text = html_text.replace('-SPACE-', '-SPACE-')
        html_text = html_text.replace('-SPACE-', '-SPACE-')
        html_text = html_text.replace('-SPACE-', '-SPACE-')
        html_text = html_text.replace('-SPACE-', '-SPACE-')
        html_text = html_text.replace('-SPACE-', '-SPACE-')
        html_text = html_text.replace('-SPACE-', '-SPACE-')
        html_text = html_text.replace('-SPACE-', '-SPACE-')
        html_text = html_text.replace('-SPACE-', '-SPACE-')
        html_text = html_text.replace('-SPACE-', '-SPACE-')
        html_text = html_text.replace('-SPACE-', '-SPACE-')
        html_text = html_text.replace('-SPACE-', '-SPACE-')
        html_text = html_text.replace('-SPACE-', '-SPACE-')
        html_text = html_text.replace('-SPACE-', '-SPACE-')
        html_text = html_text.replace('-SPACE-', '-SPACE-')
        html_text = html_text.replace('-SPACE-', '-SPACE-')
        html_text = html_text.replace('-SPACE-', '-SPACE-')
        html_text = html_text.replace('-SPACE-', '-SPACE-')
        html_text = html_text.replace('-SPACE-', '-SPACE-')
        html_text = html_text.replace('-SPACE-', '-SPACE-')
        html_text = html_text.replace('-SPACE-', '-SPACE-')
        html_text = html_text.replace('-SPACE-', '-SPACE-')
        html_text = html_text.replace('-SPACE-', '-SPACE-')
        html_text = html_text.replace('-SPACE-', '-SPACE-')
        html_text = html_text.replace('-SPACE-', '-SPACE-')
        html_text = html_text.replace('-SPACE-', '-SPACE-')
        html_text = html_text.replace('-SPACE-', '-SPACE-')
        html_text = html_text.replace('-SPACE-', '-SPACE-')
        html_text = html_text.replace('-SPACE-', '-SPACE-')
        html_text = html_text.replace('-SPACE-', '-SPACE-')
        html_text = html_text.replace('-SPACE-', '-SPACE-')
        html_text = html_text.replace('-SPACE-', '-SPACE-')
        html_text = html_text.replace('-SPACE-', '-SPACE-')
        html_text = html_text.replace('-SPACE-', '-SPACE-')
        html_text = html_text.replace('-SPACE-', '-SPACE-')
        html_text = html_text.replace('-SPACE-', '-SPACE-')
        html_text = html_text.replace('-SPACE-', '-SPACE-')
        html_text = html_text.replace('-SPACE-', '-SPACE-')
        html_text = html_text.replace('-SPACE-', '-SPACE-')
        html_text = html_text.replace('-SPACE-', '-SPACE-')
        html_text = html_text.replace('-SPACE-', '-SPACE-')
        html_text = html_text.replace('-SPACE-', '-SPACE