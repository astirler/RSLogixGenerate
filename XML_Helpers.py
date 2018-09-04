import copy
from lxml import etree


def get_data(file_path):
    __xml = XMLElements()

    # Open XML document using parser
    parser = etree.XMLParser(strip_cdata=False)
    with open(file_path, 'rb') as f:
        __xml_file = etree.XML(f.read(), parser)
    # make a copy of the xml so it can be changed and added to project folder later
    __xml.XML = copy.deepcopy(__xml_file)

    # get the controller xml then get the data to work on
    controller = __xml.XML.getchildren()
    __xml.Tags = controller[0].find("Tags")
    __xml.Programs = controller[0].find("Programs")
    __xml.Routines = __xml.Programs[0].find("Routines")
    return __xml


def find_element_by_name(name, xml):
    """
    :arg name name of the element
    :arg xml xml from root
    :rtype: xml element
    """
    for element in xml:
        items = element.items()
        if items[0][1] == name:
            return element
    return


def rename_attributes(elem, excel_structure):
    parser = etree.XMLParser(strip_cdata=False)
    string_elem = etree.tostring(elem).decode("utf-8")

    for old_name, new_name in excel_structure.Replacements.items():

        if old_name in string_elem:
            string_elem = string_elem.replace(old_name, new_name.TagName)
        else:
            print("Strategy {}: {} not in element so no replacement done".format(excel_structure.Strategy, old_name))
    reformed_elem = etree.fromstring(string_elem, parser=parser)
    reformed_elem = remove_unused_elements(reformed_elem)
    return reformed_elem


def insert_element(element, parent):
    parent.append(element)
    return


def get_elements(list_input):
    output = []
    for _list in list_input:
        for elements in _list:
            output.append(elements.getchildren())
    return output


def remove_unused_elements(elem):
    children = elem.getchildren()
    for elements in children:
        grand_children = elements.getchildren()
        for gg in grand_children:
            try:
                _gg = gg.getchildren()
                for _element in _gg:
                    if _element.get("Operand") == "":
                        gg.remove(_element)
            except Exception as ex:
                print(ex)
    return elem


def tag_writer(row_data, xml_elements):
    for old_name, new_name in row_data.Replacements.items():
        try:
            tag = find_element_by_name(old_name, xml_elements.Tags)
            tag.set("Name", new_name.TagName)
            try:
                tag.find("Description").text = etree.CDATA(new_name.TagDescription)
            except Exception as ex:
                print(ex)
        except Exception as ex:
            print(ex)


class XMLElements:
    ProgramTags = None
    Tags = None
    Routines = None
    Programs = None
    Tasks = None
    XML = None
