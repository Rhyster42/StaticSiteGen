from enum import Enum

def markdown_to_blocks(markdown):
    blocks = markdown.strip().split('\n\n')

    new_blocks = []

    for block in blocks:
        lines = [line.strip() for line in block.split('\n')]

        new_block = '\n'.join(lines)

        new_blocks.append(new_block)
    
    return new_blocks

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