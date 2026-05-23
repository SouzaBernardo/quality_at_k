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
        tree = ET.parse(self.file_name)
        self.root = tree.getroot()
        return self.root
    

    def write_xml(self, file_name):
        """
        Writes the XML data to the specified file.
        :param file_name: string, the name of the file to write the XML data.
        :return: bool, True if the write operation is successful, False otherwise.
        """
        try:
            # Create a new XML tree with the root element
            tree = ET.ElementTree(self.root)
            
            # Write the XML data to the specified file
            tree.write(file_name)
            
            return True
        except Exception as e:
            print(f"Error writing XML data: {e}")
            return False
    



    def find_element(self, element_name):
        """
        Finds the XML elements with the specified name.
        :param element_name: string, the name of the elements to find.
        :return: list, a list of found elements with the specified name.
        """
        found_elements = self.root.findall(element_name)
        return found_elements