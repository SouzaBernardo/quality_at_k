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
        for i in range(len(lines)):
            if i % 2 == 0:
                lines[i] = '\n' + lines[i]
        return '\n'.join(lines)

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
        # Replace consecutive line breaks with a single line break
        self.__format_line_feed(html_text)
        
        # Add the code mark to the end of the line
        html_text = re.sub(r'\n\s+', r'\n\n-CODE-', html_text)
        
        return html_text

    def extract_code_from_html_text(self, html_text):
        """
        extract codes from the html body
        :param html_text: string, html text
        :return: the list of code
        """
        # Extract the code tags from the HTML
        code_tags = re.findall(r'<code.*?</code>', html_text)
        
        # Extract the codes from the code tags
        code_codes = []
        for code_tag in code_tags:
            if code_tag.isdigit():
                code_code = code_tag.strip()
                if code_code:
                    code_codes.append(code_code)
            elif code_tag.is_html_code():
                code_text = code_tag.text.strip()
                if code_text:
                    code_codes.append('-CODE-')
                    code_text = code_text.strip()
                    if code_text:
                        code_codes.append('-CODE-')
                    else:
                        code_codes.append('-CODE-')
                else:
                    code_codes.append('-CODE-')
        
        return code_codes