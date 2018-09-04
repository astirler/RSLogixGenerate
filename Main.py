import glob, os
from lxml import etree
from Helpers.XML_Helpers import get_data, rename_attributes, tag_writer
from Helpers.ExcelHelpers import get_sheet_values

e_path = input("Please enter the path to the Excel Spreadsheet: ")

path = input("Please enter the path to the strategy folder: ")

records = {}

# open the file folder for the samples from export
for filename in glob.glob(os.path.join(path, '*.L5X')):
    record_name = os.path.basename(filename).strip('.L5X')
    __xml = get_data(filename)
    records[record_name] = __xml

sheet_data = get_sheet_values(e_path)


new_records = []

for each in sheet_data:
    try:
        # pull the sample element for copying
        sample = records[each.Strategy]
        # change the tags
        tag_writer(each, sample)
        # rename the element and the data while in string format then return and insert
        rename_attributes(sample.Routines, each)
        # append the xml to the output file
        new_records.append(sample.XML)
    except Exception as ex:
        print(ex)

file_num = 0
# create the output folder in the same file as the imported data
out_path = path + r'\Output'

# if the folder does not exist in the input data folder create it now
if not os.path.exists(out_path):
    os.makedirs(out_path)

# for each of the generated strategies put it in the output folder
for xml in new_records:
    with open(out_path+r"\RSGenerateExp{}.L5X".format(file_num), 'w') as new_xml:
        new_xml.write(etree.tostring(xml, pretty_print=True, xml_declaration=True, encoding="utf-8",
                                     standalone="yes").decode('utf-8'))
        file_num += 1
