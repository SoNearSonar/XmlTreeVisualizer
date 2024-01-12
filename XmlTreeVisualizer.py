import xml.etree.ElementTree as ET

class XmlTreeVisualizer:
    __tree = None

    def __init__(self, path):
        super().__init__()
        try:
            self.__tree = ET.parse(path)
            self.path = path
        except:
            print("Error parsing XML file")
            self.path = None

    def __str__(self):
        return f"XmlNodeReader object reading XML file at {self.path}"
    
    # Displays the tree as a string
    def display_tree(self):
        if self.__tree is None:
            return ""
        
        root = self.__tree.getroot()
        diagram = self.__tree.getroot().tag
        space_count = 0

        for child in root:
            diagram += f"\n{self.__format_node_visual(space_count)}|--> {child.tag}" + self.__display_child_nodes(child, space_count + 2)

        return diagram


    # Displays the children nodes of the parent node
    def __display_child_nodes(self, node, space_count):
        str = ""
        if len(node) == 0:
            return str
        
        for child in node:
            str += f"\n{self.__format_node_visual(space_count)}|--> {child.tag}" + self.__display_child_nodes(child, space_count + 2)

        return str


    # Formats spacing for each node in a tree
    def __format_node_visual(self, space_count):
        str = ""
        for _ in range(space_count):
            str += " "

        return str