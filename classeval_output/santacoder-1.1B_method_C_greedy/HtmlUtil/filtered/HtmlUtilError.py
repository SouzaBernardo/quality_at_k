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
        code_tag = soup.new_tag('code')
        code_tag['class'] = 'language-python'
        code_tag['data-language'] = 'python'
        code_tag['data-linenos'] = 'true'
        code_tag['data-linenostart'] = '1'
        code_tag['data-lineend'] = '0'
        code_tag['data-lineseparator'] = 'unix'
        code_tag['data-fold'] = 'false'
        code_tag['data-foldlevel'] = '0'
        code_tag['data-foldmarker'] = '0'
        code_tag['data-foldmarker-start'] = '0'
        code_tag['data-foldmarker-end'] = '0'
        code_tag['data-foldmarker-level'] = '0'
        code_tag['data-foldmarker-class'] = 'language-python'
        code_tag['data-foldmarker-style'] = 'null'
        code_tag['data-foldmarker-background'] = 'null'
        code_tag['data-foldmarker-border'] = 'null'
        code_tag['data-foldmarker-border-radius'] = 'null'
        code_tag['data-foldmarker-border-color'] = 'null'
        code_tag['data-foldmarker-border-style'] = 'null'
        code_tag['data-foldmarker-border-width'] = 'null'
        code_tag['data-foldmarker-padding'] = 'null'
        code_tag['data-foldmarker-padding-top'] = 'null'
        code_tag['data-foldmarker-padding-right'] = 'null'
        code_tag['data-foldmarker-padding-bottom'] = 'null'
        code_tag['data-foldmarker-padding-left'] = 'null'
        code_tag['data-foldmarker-margin'] = 'null'
        code_tag['data-foldmarker-margin-top'] = 'null'
        code_tag['data-foldmarker-margin-right'] = 'null'
        code_tag['data-foldmarker-margin-bottom'] = 'null'
        code_tag['data-foldmarker-margin-left'] = 'null'
        code_tag['data-foldmarker-margin-top-left'] = 'null'
        code_tag['data-foldmarker-margin-top-right'] = 'null'
        code_tag['data-foldmarker-margin-bottom-left'] = 'null'
        code_tag['data-foldmarker-margin-bottom-right'] = 'null'
        code_tag['data-foldmarker-margin-left-left'] = 'null'
        code_tag['data-foldmarker-margin-left-right'] = 'null'
        code_tag['data-foldmarker-margin-right-left'] = 'null'
        code_tag['data-foldmarker-margin-right-right'] = 'null'
        code_tag['data-foldmarker-margin-top-left-margin'] = 'null'
        code_tag['data-foldmarker-margin-top-right-margin'] = 'null'
        code_tag['data-foldmarker-margin-bottom-left-margin'] = 'null'
        code_tag['data-foldmarker-margin-bottom-right-margin'] = 'null'
        code_tag['data-foldmarker-margin-left-left-margin'] = 'null'
        code_tag['data-foldmarker-margin-left-right-margin'] = 'null'
        code_tag['data-foldmarker-margin-right-left-margin'] = 'null'
        code_tag['data-foldmarker-margin-right-right-margin'] = 'null'
        code_tag['data-foldmarker-margin-top-left-padding'] = 'null'
        code_tag['data-foldmarker-margin-top-right-padding'] = 'null'
        code_tag['data-foldmarker-margin-bottom-left-padding'] = 'null'
        code_tag['data-foldmarker-margin-bottom-right-padding'] = 'null'
        code_tag['data-foldmarker-margin-left-left-padding'] = 'null'
        code_tag['data-foldmarker-margin-left-right-padding'] = 'null'
        code_tag['data-foldmarker-margin-right-left-padding'] = 'null'
        code_tag['data-foldmarker-margin-right-right-padding'] = 'null'
        code_tag['data-foldmarker-margin-top-left-margin-top'] = 'null'
        code_tag['data-foldmarker-margin-top-right-margin-top'] = 'null'
        code_tag['data-foldmarker-margin-bottom-left-margin-top'] = 'null'
        code_tag['data-foldmarker-margin-bottom-right-margin-top'] = 'null'
        code_tag['data-foldmarker-margin-left-left-margin-top'] = 'null'
        code_tag['data-foldmarker-margin-left-right-margin-top'] = 'null'
        code_tag['data-foldmarker-margin-right-left-margin-top'] = 'null'
        code_tag['data-foldmarker-margin-right-right-margin-top'] = 'null'
        code_tag['data-foldmarker-margin-top-left-margin-right'] = 'null'
        code_tag['data-foldmarker-margin-top-right-margin-right'] = 'null'
        code_tag['data-foldmarker-margin-bottom-left-margin-right'] = 'null'
        code_tag['data-foldmarker-margin-bottom-right-margin-right'] = 'null'
        code_tag['data-foldmarker-margin-left-left-margin-right'] = 'null'
        code_tag['data-foldmarker-margin-left-right-margin-right'] = 'null'
        code_tag['data-foldmarker-margin-right-left-margin-right'] = 'null'
        code_tag['data-foldmarker-margin-right-right-margin-right'] = 'null'
        code_tag['data-foldmarker-margin-top-left-margin-bottom'] = 'null'
        code_tag['data-foldmarker-margin-top-right-margin-bottom'] = 'null'
        code_tag['data-foldmarker-margin-bottom-left-margin-bottom'] = 'null'
        code_tag['data-foldmarker-margin-bottom-right-margin-bottom'] = 'null'
        code_tag['data-foldmarker-margin-left-left-margin-bottom'] = 'null'
        code_tag['data-foldmarker-margin-left-right-margin-bottom'] = 'null'
        code_tag['data-foldmarker-margin-right-left-margin-bottom'] = 'null'
        code_tag['data-foldmarker-margin-right-right-margin-bottom'] = 'null'
        code_tag['data-foldmarker-margin-top-left-padding-top'] = 'null'
        code_tag['data-foldmarker-margin-top-right-padding-top'] = 'null'

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
        code_list = []
        for tag in soup.find_all('pre'):
            code_list.append(tag.text)
        return code_list