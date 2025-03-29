from enum import Enum


class HTMLNode():
    def __init__ (self, tag=None, value=None, children=None, props=None):
        self.tag = tag
        self.value = value
        self.children = children
        self.props = props

    def to_html(self):
        raise NotImplementedError
    
    def props_to_html(self):
        propstring = ""
        for prop in self.props:
            propstring = f'{propstring} {prop}="{self.props[prop]}"'
        return propstring
    
    def __repr__(self):
            print(f'HTMLNode:{self.tag}, {self.value}, {self.children}, {self.props}')

class LeafNode(HTMLNode):
    def __init__(self, tag, value, props=None):
        super().__init__(tag, value, None, props)
    
    def to_html(self):

        if self.value is None:
            raise ValueError('LeafNode must have a value')
        if self.tag is None:
            return {self.value}

        if self.props:
            return f'<{self.tag}{self.props_to_html()}>{self.value}</{self.tag}>' 
        
        return f'<{self.tag}>{self.value}</{self.tag}>'

        