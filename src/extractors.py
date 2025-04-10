import re
from textnode import TextNode, TextType

def extract_markdown_images(text):
    return re.findall(r'!\[([^\[\]]*)\]\(([^\(\)]*)\)', text)

def extract_markdown_links(text):
    return re.findall(r'(?<!!)\[([^\[\]]*)\]\(([^\(\)]*)\)', text)

def split_nodes_image(old_nodes):
    new_nodes = []

    for old_node in old_nodes:
        if old_node.text_type != TextType.TEXT:
            new_nodes.append(old_node)
            continue

        text = old_node.text
        matches = extract_markdown_images(text)

        if not matches:
            new_nodes.append(old_node)
            continue

        # Loop over matches, manually search their positions
        current_index = 0

        for alt, url in matches:
            match_text = f'![{alt}]({url})'
            found_at = text.find(match_text, current_index)

            if found_at == -1:
                raise Exception("Markdown is missing")

            # Text before image
            if found_at > current_index:
                before_text = text[current_index:found_at]
                new_nodes.append(TextNode(before_text, TextType.TEXT))

            # Image node
            new_nodes.append(TextNode(alt, TextType.IMAGE, url))

            current_index = found_at + len(match_text)

        # Any text after last image
        if current_index < len(text):
            after_text = text[current_index:]
            new_nodes.append(TextNode(after_text, TextType.TEXT))

    return new_nodes




def split_nodes_link(old_nodes):
    new_nodes = []

    for old_node in old_nodes:
        if old_node.text_type != TextType.TEXT:
            new_nodes.append(old_node)
            continue

        text = old_node.text
        matches = extract_markdown_links(text)

        if not matches:
            new_nodes.append(old_node)
            continue

        current_index = 0

        for alt, url in matches:
            match_text = f'[{alt}]({url})'
            found_at = text.find(match_text, current_index)

            if found_at == -1:
                raise Exception("Markdown is missing")

            if found_at > current_index:
                before_text = text[current_index:found_at]
                new_nodes.append(TextNode(before_text, TextType.TEXT))

            new_nodes.append(TextNode(alt, TextType.LINK, url))

            current_index = found_at + len(match_text)

        if current_index < len(text):
            after_text = text[current_index:]
            new_nodes.append(TextNode(after_text, TextType.TEXT))

    return new_nodes