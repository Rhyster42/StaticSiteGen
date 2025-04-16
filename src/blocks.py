from enum import Enum
from htmlnode import LeafNode, ParentNode
from textnode import text_node_to_html_node, TextNode, TextType
from extractors import text_to_text_nodes

def markdown_to_blocks(markdown):
    blocks = markdown.split("\n\n")
    filtered_blocks = []
    for block in blocks:
        if block == "":
            continue
        block = block.strip()
        filtered_blocks.append(block)
    return filtered_blocks

class BlockType(Enum):
    PARAGRAPH = 'paragraphs'
    HEADING = 'heading'
    CODE = 'code'
    QUOTE = 'quote'
    UNORDERED_LIST = 'unordered list'
    ORDERED_LIST = 'ordered list'

def block_to_block_type(block):
        if block.startswith('#'):
            return BlockType.HEADING
        elif block.startswith("```") and block.endswith("```"):
            return BlockType.CODE
        elif lines_start_with(block, '>'):
            return BlockType.QUOTE
        elif lines_start_with(block, '- '):
            return BlockType.UNORDERED_LIST
        elif ordered_list_check(block):
            return BlockType.ORDERED_LIST
        else:
            return BlockType.PARAGRAPH
        
    # Helper function for block_type
def lines_start_with(block, char): 
    lines = block.split('\n')
    for line in lines:
        if line.startswith(char):
            continue
        else:
            return False
    return True

    # Helper function for specifically ordered list
def ordered_list_check(block):
    line_num = 1
    lines = block.split('\n')
    for line in lines:
        if line.startswith(f'{line_num}. '):
            line_num += 1
            continue
        else:
            return False
    return True

def markdown_to_html_node(markdown):
    
    blocks = markdown_to_blocks(markdown)

    new_blocks = []

    for block in blocks:
        block_type = block_to_block_type(block)

        html_node = block_to_html_node(block, block_type)

        new_blocks.append(html_node)

    return ParentNode('div', new_blocks)

def block_to_html_node(block, block_type):
    match block_type:
        case BlockType.PARAGRAPH:
        # Replace newlines with spaces for paragraphs
            paragraph_content = block.replace('\n', ' ')
            return ParentNode('p', text_to_children(paragraph_content))
        case BlockType.HEADING:
            hash_count = len(block) - len(block.lstrip('#'))
            heading_content = block.lstrip('#').strip()  # Remove # and any leading/trailing whitespace
            return ParentNode(f'h{hash_count}', text_to_children(heading_content))
        case BlockType.CODE:
            text = block[4:-3]
            print(text)
    
            code_node = TextNode(text, TextType.TEXT)
            html_node = text_node_to_html_node(code_node)
            code = ParentNode('code', [html_node])
            return ParentNode('pre', [code])

        case BlockType.QUOTE:
            lines = block.split("\n")
            new_lines = []
            for line in lines:
                if not line.startswith(">"):
                    raise ValueError("invalid quote block")
                new_lines.append(line.lstrip(">").strip())
            content = " ".join(new_lines)
            return ParentNode('blockquote', text_to_children(content))
        case BlockType.UNORDERED_LIST:
            return list_to_node('ul', block)
        case BlockType.ORDERED_LIST:
            return list_to_node('ol', block)
        case __:
            raise Exception("Unkown block type, cannot convert to html node.")

def list_to_node(list_type, block):    
    lines = block.split('\n')
    new_nodes = []
    for line in lines:
        new_line = line.lstrip(' -1234567890.')
        text_nodes = text_to_children(new_line)
        new_nodes.append(ParentNode('li', text_nodes))
    return ParentNode(list_type, new_nodes)
        
def text_to_children(text):
    text_nodes = text_to_text_nodes(text)
    new_nodes_list = []
    for node in text_nodes:
        new_html_node = text_node_to_html_node(node)
        new_nodes_list.append(new_html_node)
    return new_nodes_list
        
    pass