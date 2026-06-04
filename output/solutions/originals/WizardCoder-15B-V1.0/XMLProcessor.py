Below is an instruction that describes a task. Write a response that appropriately completes the request.

### Instruction:
Please complete the class XMLProcessor in the following code.
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
        >>> xml_processor = XMLProcessor('test.xml')
        >>> root_element = xml_processor.read_xml()
        >>> print(root_element)
        <Element 'root' at 0x7f8e3b7eb180>
        """


    def write_xml(self, file_name):
        """
        Writes the XML data to the specified file.
        :param file_name: string, the name of the file to write the XML data.
        :return: bool, True if the write operation is successful, False otherwise.
        >>> xml_processor = XMLProcessor('test.xml')
        >>> root = xml_processor.read_xml()
        >>> success = xml_processor.write_xml('output.xml')
        >>> print(success)
        True
        """


    def process_xml_data(self, file_name):
        """
        Modifies the data in XML elements and writes the updated XML data to a new file.
        :param file_name: string, the name of the file to write the modified XML data.
        :return: bool, True if the write operation is successful, False otherwise.
        >>> xml_processor = XMLProcessor('test.xml')
        >>> root = xml_processor.read_xml()
        >>> success = xml_processor.process_xml_data('processed.xml')
        >>> print(success)
        True
        """


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

### Response:The class XMLProcessor is implemented as per the requirements mentioned in the prompt. The class has the following methods:

1. __init__(self, file_name): Initializes the XMLProcessor object with the given file name.

2. read_xml(self): Reads the XML file and returns the root element.

3. write_xml(self, file_name): Writes the XML data to the specified file.

4. process_xml_data(self, file_name): Modifies the data in XML elements and writes the updated XML data to a new file.

5. find_element(self, element_name): Finds the XML elements with the specified name.

The class uses the ElementTree module of Python to parse and manipulate XML data. The read_xml() method uses the parse() method of ElementTree to read the XML file and returns the root element. The write_xml() method uses the ElementTree.ElementTree.write() method to write the XML data to a file. The process_xml_data() method modifies the data in XML elements and writes the updated XML data to a new file. The find_element() method uses the ElementTree.Element.findall() method to find the XML elements with the specified name and returns a list of found elements.

Here's an example of how to use the class:

```python
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
        self.root = ET.parse(self.file_name).getroot()
        return self.root

    def write_xml(self, file_name):
        """
        Writes the XML data to the specified file.
        :param file_name: string, the name of the file to write the XML data.
        :return: bool, True if the write operation is successful, False otherwise.
        """
        try:
            self.root.write(file_name)
            return True
        except:
            return False

    def process_xml_data(self, file_name):
        """
        Modifies the data in XML elements and writes the updated XML data to a new file.
        :param file_name: string, the name of the file to write the modified XML data.
        :return: bool, True if the write operation is successful, False otherwise.
        """
        for item in self.root.findall('item'):
            item.text = item.text.upper()
        try:
            self.root.write(file_name)
            return True
        except:
            return False

    def find_element(self, element_name):
        """
        Finds the XML elements with the specified name.
        :param element_name: string, the name of the elements to find.
        :return: list, a list of found elements with the specified name.
        """
        return self.root.findall(element_name)

if __name__ == '__main__':
    xml_processor = XMLProcessor('test.xml')
    root = xml_processor.read_xml()
    print(root)
    items = xml_processor.find_element('item')
    for item in items:
        print(item.text)
    success = xml_processor.write_xml('output.xml')
    print(success)
    success = xml_processor.process_xml_data('processed.xml')
    print(success)
```

In this example, we create an instance of the XMLProcessor class with the file name 'test.xml'. We then call the read_xml() method to read the XML file and store the root element in the root variable. We print the root element to verify that it is a valid Element object. We then call the find_element() method to find all the 'item' elements in the XML file and store them in the items variable. We loop through the items variable and print the text of each item element. We then call the write_xml() method to write the XML data to a new file named 'output.xml'. We verify that the write operation was successful by checking the return value of the method. We then call the process_xml_data() method to modify the data in the 'item' elements and write the updated XML data to a new file named 'processed.xml'. We verify that the write operation was successful by checking the return value of the method.