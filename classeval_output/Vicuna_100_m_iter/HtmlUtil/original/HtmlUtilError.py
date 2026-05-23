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
        # Replace consecutive line breaks with a single line break
        text = text.replace('\n\n', '\n')
        return text

    def format_line_html_text(html_text):
        """
        get the html text without the code, and add the code tag -CODE- where the code is
        :param html_text:string
        :return:string
        >>>htmlutil = HtmlUtil()
        >>>htmlutil.format_line_html_text(<html>
        >>>    <body>
        >>>        <h1>Title</h1>
        >>>        <p>This is a paragraph.</p>
        >>>        <pre>print('Hello, world!')</pre>
        >>>        <p>Another paragraph.</p>
        >>>        <pre><code>for i in range(5):
        >>>            print(i)</code></pre>
        >>>    </body>
        >>></html>)
        Title
        This is a paragraph.
        -CODE-
        Another paragraph.
        -CODE-
        """
        # Replace consecutive line breaks with a single line break
        html_text = html_text.replace('\n\n', '\n')
    
        # Split the text into lines
        lines = html_text.split('\n')
    
        # Initialize a list to store the cleaned lines
        cleaned_lines = []
    
        # Iterate over the lines
        for line in lines:
            # Check if the line contains a code block
            if re.search(r'<pre><code>(.*)</code></pre>', line):
                # Get the code block
                code_block = re.search(r'<pre><code>(.*)</code></pre>', line).group(1)
    
                # Get the code block with the -CODE- tag
                cleaned_code_block = code_block.replace('<code>', '<code>' + self.MARKUP_LANGUAGE_MARK + '</code>')
                cleaned_code_block = cleaned_code_block.replace('</code>', self.MARKUP_LANGUAGE_MARK + '</code>')
    
                # Add the cleaned code block to the list
                cleaned_lines.append(cleaned_code_block)
    
            # Check if the line contains a URL
            elif re.search(r'<a href="(.*)"', line):
                # Get the URL
                url = re.search(r'<a href="(.*)"', line).group(1)
    
                # Add the -URL- tag to the cleaned line
                cleaned_lines.append(self.SPACE_MARK + url + self.SPACE_MARK)
    
            # Check if the line contains a number
            elif re.search(r'\d+', line):
                # Get the number
                number = re.search(r'\d+', line).group(0)
    
                # Add the -NUMBER- tag to the cleaned line
                cleaned_lines.append(self.SPACE_MARK + number + self.SPACE_MARK)
    
            # Check if the line contains a trace
            elif re.search(r'<pre><code class="traceback">(.*)</code></pre>', line):
                # Get the trace
                trace = re.search(r'<pre><code class="traceback">(.*)</code></pre>', line).group(1)
    
                # Add the -TRACE- tag to the cleaned line
                cleaned_lines.append(self.SPACE_MARK + trace + self.SPACE_MARK)
    
            # Check if the line contains a command
            elif re.search(r'<span class="command">(.*)</span>', line):
                # Get the command
                command = re.search(r'<span class="command">(.*)</span>', line).group(1)
    
                # Add the -COMMAND- tag to the cleaned line
                cleaned_lines.append(self.SPACE_MARK + command + self.SPACE_MARK)
    
            # Check if the line contains a comment
            elif re.search(r'<!--(.*)-->', line):
                # Get the comment
                comment = re.search(r'<!--(.*)-->', line).group(1)
    
                # Add the -COMMENT- tag to the cleaned line
                cleaned_lines.append(self.SPACE_MARK + comment + self.SPACE_MARK)
    
            # Check if the line contains code
            elif re.search(r'<pre><code>(.*)</code></pre>', line):
                # Get the code
                code = re.search(r'<pre><code>(.*)</code></pre>', line).group(1)
    
                # Add the -CODE- tag to the cleaned line
                cleaned_lines.append(self.SPACE_MARK + code + self.SPACE_MARK)
    
            # Add the cleaned line to the list
            cleaned_lines.append(line)
    
        # Return the cleaned lines
        return '\n'.join(cleaned_lines)

