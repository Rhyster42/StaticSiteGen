from textnode import TextNode, TextType

def split_nodes_delimiter(old_nodes, delimiter, text_type):
    new_nodes = []

    for old_node in old_nodes:
        if old_node.text_type != TextType.TEXT:
            new_nodes.append(old_node)
            continue

        text = old_node.text
        start_index = text.find(delimiter)

        if start_index == -1:
            new_nodes.append(old_node)
            continue

        end_index = text.find(delimiter, start_index + len(delimiter))
        if end_index == -1:
            raise Exception(f'No closing delimiter found for {delimiter}')
        
        before_text = text[:start_index]

        between_text = text[start_index + len(delimiter):end_index]

        after_text = text[end_index + len(delimiter):]

        if before_text:
            new_nodes.append(TextNode(before_text, TextType.TEXT))
        new_nodes.append(TextNode(between_text, text_type))

        remaining_nodes = (split_nodes_delimiter([TextNode(after_text, TextType.TEXT)], delimiter, text_type))

        new_nodes.extend(remaining_nodes)

    return new_nodes