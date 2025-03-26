from enum import Enum

class TextType(Enum):
    Normal_Text = "Normal Text"
    Bold_Text = "**Bold text**"
    Italic_Text = "_Italic text_"
    Code_Text = "'Code text'"
    
class TextNode():
    def __init__(self, text, text_type, url=None):
        self.text = text
        self.text_type = text_type
        self.url = url

    def __eq__(textnode1, textnode2):
        if textnode1 == textnode2:
            return True
        return False
    
    def __repr__ (self):
        return f'TextNode({self.text},{self.text_type},{self.url})'
