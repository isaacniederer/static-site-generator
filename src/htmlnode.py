class HTMLNode():
    def __init__(self, tag=None, value=None, children=[], props={}):
        self.tag = tag
        self.value = value
        self.children = children
        self.props = props

    def to_html(self):
        raise NotImplementedError()

    def props_to_html(self):
        string = None
        for item in self.props:
            if string == None:
                string = f"{item}={self.props[item]}"
            else: 
                string = f"{string} {item}={self.props[item]}"

        return string

    def __repr__(self):
        tag_string = f"Tag: {self.tag}"
        value_string = f"Value: {self.value}"
        children_string = "Children:"
        if self.children != None:
            children_string += "\n("
            for item in self.children:
                children_string += f"\n{str(item)}"
            children_string += ")\n"
        else:
            children_string += " None"
        props_string = f"Props: {self.props}"
        return tag_string + "\n" + value_string + "\n" + children_string + "\n" + props_string + "\n"



class ParentNode(HTMLNode):
    def __init__(self, tag=None, children=[], props={}):
       super().__init__(tag, None, children, props) 

    def to_html(self):
        if self.tag == None:
            raise ValueError("Node has no tag")
        elif len(self.children) == 0:
            raise ValueError("Parent Node has no children")
        
        new_str = "<" + self.tag + ">"
        for item in self.children:
            if item.tag == None:
                new_str += item.value
            else:
                new_str += "<" + item.tag + ">" + item.value + "</" + item.tag + ">" 

        return new_str + "</" + self.tag + ">"



class LeafNode(HTMLNode):
    def __init__(self, tag=None, value=None, props={}):
        super().__init__(tag, value, [], props)

    def to_html(self):
        if self.value == None:
            raise ValueError("All leaf nodes require a value")
        elif self.tag == None:
            return self.value
        else:
            if self.props == None:
                return f"<{self.tag}>{self.value}</{self.tag}>"
            else:
                props_string = self.tag
                for item in self.props:
                    props_string += f" {item}=\"{str(self.props[item])}\""
                return f"<{props_string}>{self.value}</{self.tag}>"
