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
        # Replace consecutive line breaks with a single line break
        text = re.sub(r'\n+', r'\n', text)
        return text

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
        # Extract the code from the HTML text
        code = self.extract_code_from_html_text(html_text)
        
        # Add the code tag to the HTML text
        html_text = re.sub(r'<code>(.*?)</code>', r'<code>{}</code>'.format(code), html_text)
        
        return html_text

    def extract_code_from_html_text(self, html_text):
        """
        extract codes from the html body
        :param html_text: string, html text
        :return: the list of code
        """
        code_list = []
        for line in re.split('\n', html_text):
            if line.strip() == '>':
                self.SPACE_MARK.insert(0, line.strip())
            elif line.strip() == '<pre>':
                self.SPACE_MARK.insert(0, line.strip())
            elif line.strip() == '<code>':
                code = line.strip().split('</code><code>')[1].strip()
                if code:
                    self.CODE_MARK.insert(0, code)
                    code_list.append(code)
            elif line.strip() == '>':
                self.SPACE_MARK.insert(0, line.strip())
        return code_list