# Pygments is a Python library for syntax highlighting. It supports a wide range of programming languages and file formats. Here's a basic tutorial on how to use Pygments:

### Installing Pygments

# You can install Pygments using pip:
# pip install Pygments


### Basic Usage
from pygments import highlight
from pygments.lexers import get_lexer_by_name
from pygments.formatters import HtmlFormatter

# Define the code to be highlighted
code = """
def hello_world():
    print("Hello, World!")
"""

# Choose the lexer for the programming language (e.g., Python)
lexer = get_lexer_by_name("python")

# Choose the formatter (e.g., HTML)
formatter = HtmlFormatter()

# Highlight the code
highlighted_code = highlight(code, lexer, formatter)

# Print or save the highlighted code
print(highlighted_code)


### Customizing Output

# Pygments provides various options for customizing the output. For example, you can customize the style, line numbers, and more.
# Here's an example:


from pygments.styles import get_style_by_name

# Use a different style (e.g., 'monokai')
custom_style = get_style_by_name('monokai')
formatter = HtmlFormatter(style=custom_style, linenos=True)
# linenos is the linenumbers

# Highlight the code with the custom options
highlighted_code = highlight(code, lexer, formatter)

# Print or save the highlighted code
print(highlighted_code)


### Supported Lexers

# Pygments supports a variety of lexers for different languages.
# You can find a list of supported lexers in the Pygments documentation.


from pygments.lexers import get_all_lexers

# Get a list of all available lexers
all_lexers = list(get_all_lexers())

# Print the list of lexers
for lexer in all_lexers:
    print(lexer[0], lexer[1])

# There's a whole lot I saw in the documentation but below is a code snippet I wrote when practicing

from pygments import highlight
from pygments.lexers import PythonLexer
from pygments.formatters import HtmlFormatter
from pygments.lexers import get_lexer_by_name, guess_lexer, get_lexer_for_filename, get_all_lexers
from pygments import lex
from pygments.styles import get_all_styles, get_style_by_name, STYLE_MAP
# code = 'print "Hello World"'
# print(highlight(code, PythonLexer(), HtmlFormatter()))
# print(HtmlFormatter().get_style_defs('.highlight'))

code = """
from pygments import highlight
from pygments.lexers import PythonLexer
from pygments.formatters import HtmlFormatter
from pygments.lexers import get_lexer_by_name, guess_lexer, get_lexer_for_filename, get_all_lexers
from pygments import lex
from pygments.styles import get_all_styles, get_style_by_name, STYLE_MAP
# code = 'print "Hello World"'
# print(highlight(code, PythonLexer(), HtmlFormatter()))
# print(HtmlFormatter().get_style_defs('.highlight'))

# lexer = get_lexer_by_name('python', stripall=True)
# print(highlight(code, lexer, HtmlFormatter(linenos=True)))

# print(guess_lexer("console.log('Hello World')"))
# print(lex(code, PythonLexer()))
with open('test2.html', 'w') as outputFile: 
    highlight(code, get_lexer_by_name('javascript'), HtmlFormatter(style=get_style_by_name('stata_dark'), full=True), outputFile)

# print(get_lexer_for_filename('fixtures.md'))
# for lexer in get_all_lexers():
#     print(lexer[0])
    
for style in STYLE_MAP: 
    print(style)
    
from pygments import highlight
from pygments.lexers import PythonLexer
from pygments.formatters import HtmlFormatter
from pygments.lexers import get_lexer_by_name, guess_lexer

# code = 'print "Hello World"'
# print(highlight(code, PythonLexer(), HtmlFormatter()))
# print(HtmlFormatter().get_style_defs('.highlight'))

code = 'array = []\nfor element in elements:\n\tarray.push(elements)'
# lexer = get_lexer_by_name('python', stripall=True)
# print(highlight(code, lexer, HtmlFormatter(linenos=True)))

print(guess_lexer("console.log('Hello World')"))
"""
# lexer = get_lexer_by_name('python', stripall=True)
# print(highlight(code, lexer, HtmlFormatter(linenos=True)))

# print(guess_lexer("console.log('Hello World')"))
# print(lex(code, PythonLexer()))
with open('test2.html', 'w') as outputFile: 
    highlight(code, get_lexer_by_name('python'), HtmlFormatter(style=get_style_by_name('dracula'), full=True), outputFile)

# print(get_lexer_for_filename('fixtures.md'))
# for lexer in get_all_lexers():
#     print(lexer[0])
    
for style in STYLE_MAP: 
    print(style)

