import xml.etree.ElementTree as ET
class XMLProcessor:  
    """
    This is a class as XML files handler, including reading, writing, processing as well as finding elements in a XML file.
    """

    def __init__(self, file_name):
        """
        Initialize the XMLProcessor object with the given file name.
        :param file_name:string, the name of the XML file to be processed.
        """
        self.file_name = file_name
        self.root = None



    def read_xml(self):
        """
        Reads the XML file and returns the root element.
        :return: Element, the root element of the XML file.
        """
        try:
            tree = ET.parse(self.file_name)
            root = tree.getroot()
            self.root = root
            return root
        except Exception as e:
            print(f"Error reading XML file: {e}")
            return None

    def write_xml(self, file_name):
        """
        Writes the XML data to the specified file.
        :param file_name: string, the name of the file to write the XML data.
        :return: bool, True if the write operation is successful, False otherwise.
        """
        try:
            tree = ET.parse(self.file_name)
            root = tree.getroot()
            file = open(file_name, "w")
            file.write(ET.tostring(root, encoding="unicode"))
            file.close()
            return True
        except Exception as e:
            print(f"Error writing XML file: {e}")
            return False

    def process_xml_data(self, file_name):
        try:
            tree = ET.parse(self.file_name)
            root = tree.getroot()
            file = open(file_name, "w")
            for child in root.findall():
                if child.get('data'):
                    data = child.get('data')
                    child.set('data', 'modified_data')
                    file.write(ET.tostring(child, encoding="unicode"))
            file.close()
            return True
        except Exception as e:
            print(f"Error writing XML file: {e}")
            return False

    def find_element(self, element_name):
        """
        Finds the XML elements with the specified name.
        :param element_name: string, the name of the elements to find.
        :return: list, a list of found elements with the specified name.
        >>> xml_processor = XMLProcessor('test.xml')
        >>> root = xml_processor.read_xml()
        >>> items = xml_processor.find_element('item')
        >>> for item in items:
        >>>     print(item.text)
        apple
        banana
        orange
        """
        try:
            tree = ET.parse(self.file_name)
            root = tree.getroot()
            elements = root.findall(element_name)
            return elements
        except Exception as e:
            print(f"Error reading XML file: {e}")
            return None