from enum import Enum


class HTMLNode():
    def __init__ (self, tag=None, value=None, children=None, props=None):
        self.tag = tag
        self.value = value
        self.children = children
        self.props = props

    def to_html(self):
        raise NotImplementedError("to_html method not implemented")
    
    def props_to_html(self):
        propstring = ""
        for prop in self.props:
            propstring = f'{propstring} {prop}="{self.props[prop]}"'
        return propstring
    
    def __repr__(self):
            return f'HTMLNode:{self.tag}, {self.value}, {self.children}, {self.props}'

class LeafNode(HTMLNode):
    def __init__(self, tag, value, props=None):
        super().__init__(tag, value, None, props)
    
    def to_html(self):

        if self.value is None:
            raise ValueError('LeafNode must have a value', self)
        if self.tag is None:
            return f'{self.value}'

        if self.props:
            return f'<{self.tag}{self.props_to_html()}>{self.value}</{self.tag}>' 
        
        return f'<{self.tag}>{self.value}</{self.tag}>'
    
    def __repr__(self):
        return f"LeafNode({self.tag}, {self.value}, {self.props})"
    
class ParentNode(HTMLNode):
    def __init__(self, tag=None, children=None, props=None):
        super().__init__(tag, None, children, props)

    def to_html(self):

        if not self.tag:
            raise ValueError('ParentNode must have a tag')
        if not self.children:
                raise ValueError('ParentNode must have children')
        
        childpen = "" # a string variable to collect all LeafNodes
        
        for child in self.children:
            if not child.children:
                childpen += child.to_html()
            else:
                childpen += child.to_html()

        return f'<{self.tag}>{childpen}</{self.tag}>'
