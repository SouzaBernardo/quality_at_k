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


    def find_elements(self, element_name):
        """
        Finds the XML elements with the specified name.
        :param element_name: string, the name of the elements to find.
        :return: list, a list of found elements with the specified name.
        >>> xml_processor = XMLProcessor('test.xml')
        >>> root = xml_processor.read_xml()
        >>> items = xml_processor.find_elements('item')
        >>> for item in items:
        >>>     print(item.text)
        apple
        banana
        orange
        """


    def find_elements_with_attribute(self, element_name, attribute_name, attribute_value):
        """
        Finds the XML elements with the specified name and attribute value.
        :param element_name: string, the name of the elements to find.
        :param attribute_name: string, the name of the attribute to find.
        :param attribute_value: string, the value of the attribute to find.
        :return: list, a list of found elements with the specified name and attribute value.
        >>> xml_processor = XMLProcessor('test.xml')
        >>> root = xml_processor.read_xml()
        >>> items = xml_processor.find_elements_with_attribute('item', 'name', 'banana')
        >>> for item in items:
        >>>     print(item.text)
        banana
        """


    def find_elements_with_attribute_value(self, element_name, attribute_name, attribute_value):
        """
        Finds the XML elements with the specified name and attribute value.
        :param element_name: string, the name of the elements to find.
        :param attribute_name: string, the name of the attribute to find.
        :param attribute_value: string, the value of the attribute to find.
        :return: list, a list of found elements with the specified name and attribute value.
        >>> xml_processor = XMLProcessor('test.xml')
        >>> root = xml_processor.read_xml()
        >>> items = xml_processor.find_elements_with_attribute_value('item', 'name', 'banana')
        >>> for item in items:
        >>>     print(item.text)
        banana
        """


    def find_elements_with_attribute_value_in_list(self, element_name, attribute_name, attribute_value_list):
        """
        Finds the XML elements with the specified name and attribute value.
        :param element_name: string, the name of the elements to find.
        :param attribute_name: string, the name of the attribute to find.
        :param attribute_value_list: list, the list of values of the attribute to find.
        :return: list, a list of found elements with the specified name and attribute value.
        >>> xml_processor = XMLProcessor('test.xml')
        >>> root = xml_processor.read_xml()
        >>> items = xml_processor.find_elements_with_attribute_value_in_list('item', 'name', ['banana', 'orange'])
        >>> for item in items:
        >>>     print(item.text)
        banana
        orange
        """


    def find_elements_with_attribute_value_in_list_and_attribute_name(self, element_name, attribute_name, attribute_value_list, attribute_name_list):
        """
        Finds the XML elements with the specified name and attribute value.
        :param element_name: string, the name of the elements to find.
        :param attribute_name: string, the name of the attribute to find.
        :param attribute_value_list: list, the list of values of the attribute to find.
        :param attribute_name_list: list, the list of names of the attributes to find.
        :return: list, a list of found elements with the specified name and attribute value.
        >>> xml_processor = XMLProcessor('test.xml')
        >>> root = xml_processor.read_xml()
        >>> items = xml_processor.find_elements_with_attribute_value_in_list_and_attribute_name('item', 'name', ['banana', 'orange'], ['name', 'price'])
        >>> for item in items:
        >>>     print(item.text)
        banana
        orange
        """


    def find_elements_with_attribute_value_in_list_and_attribute_name_and_attribute_value(self, element_name, attribute_name, attribute_value_list, attribute_name_list, attribute_value_list_list):
        """
        Finds the XML elements with the specified name and attribute value.
        :param element_name: string, the name of the elements to find.
        :param attribute_name: string, the name of the attribute to find.
        :param attribute_value_list: list, the list of values of the attribute to find.
        :param attribute_name_list: list, the list of names of the attributes to find.
        :param attribute_value_list_list: list, the list of values of the attributes to find.
        :return: list, a list of found elements with the specified name and attribute value.
        >>> xml_processor = XMLProcessor('test.xml')
        >>> root = xml_processor.read_xml()
        >>> items = xml_processor.find_elements_with_attribute_value_in_list_and_attribute_name_and_attribute_value('item', 'name', ['banana', 'orange'], ['name', 'price'], ['price', '100'])
        >>> for item in items:
        >>>     print(item.text)
        banana
        orange
        """


    def find_elements_with_attribute_value_in_list_and_attribute_name_and_attribute_value_in_list(self, element_name, attribute_name, attribute_value_list, attribute_name_list, attribute_value_list_list):
        """
        Finds the XML elements with the specified name and attribute value.
        :param element_name: string, the name of the elements to find.
        :param attribute_name: string, the name of the attribute to find.
        :param attribute_value_list: list, the list of values of the attribute to find.
        :param attribute_name_list: list, the list of names of the attributes to find.
        :param attribute_value_list_list: list, the list of values of the attributes to find.
        :return: list, a list of found elements with the specified name and attribute value.
        >>> xml_processor = XMLProcessor('test.xml')
        >>> root = xml_processor.read_xml()
        >>> items = xml_processor.find_elements_with_attribute_value_in_list_and_attribute_name_and_attribute_value_in_list('item