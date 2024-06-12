class HTMLNode():
    def __init__(self, tag=None, value=None, children=[], props={}):
        self.tag = tag
        self.value = value
        self.children = children
        self.props = props

    def to_html(self):
        raise NotImplementedError("to_html is not implemented")

    def props_to_html(self):
        string = "" 
        for item in self.props:
            string = f"{string} {item}=\"{self.props[item]}\""
        return string

    def __repr__(self):
        return f"HTMLNode({self.tag}, {self.value}, children: {self.children}, {self.props})"


class ParentNode(HTMLNode):
    def __init__(self, tag=None, children=[], props={}):
       super().__init__(tag, None, children, props) 

    def to_html(self):
        if self.tag == None:
            raise ValueError("Node has no tag")
        elif len(self.children) == 0:
            raise ValueError("Parent Node has no children")

        children_text = ""
        for item in self.children:
            children_text += item.to_html() 

        return f"<{self.tag}{self.props_to_html()}>{children_text}</{self.tag}>"

    def __repr__(self):
        return f"ParentNode({self.tag}, children: {self.children}, {self.props})"



class LeafNode(HTMLNode):
    def __init__(self, tag=None, value=None, props={}):
        super().__init__(tag, value, [], props)

    def to_html(self):
        if self.value == None:
            raise ValueError("All leaf nodes require a value")
        elif self.tag == None:
            return self.value
        return f"<{self.tag}{self.props_to_html()}>{self.value}</{self.tag}>"

    def __repr__(self):
        return f"LeafNode({self.tag}, {self.value}, {self.props})"
