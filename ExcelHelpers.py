from xlrd import open_workbook

designators = ['TASK', 'PROGRAM', 'STRATEGY']


class ExcelTypes:
    Task = None
    Program = None
    Strategy = None
    Replacements = []


class TagData:
    TagName = None
    TagDescription = None


def get_sheet_values(file_path):
    __items = []
    __count = 0
    wb = open_workbook(file_path)
    for s in wb.sheets():
        values = []
        for row in range(1, s.nrows):
            row_data = ExcelTypes()
            row_data.Strategy = wb.sheet_names()[__count]
            col_names = s.row(0)
            col_value = {}
            for name, col in zip(col_names, range(s.ncols)):
                value = s.cell(row, col).value
                col_name = str(name.value).upper()
                if col_name in designators:
                    if col_name == "PROGRAM":
                        row_data.Program = value

                    elif col_name == "TASK":
                        if len(value) > 0:
                            row_data.Task = value

                else:
                    tag = TagData()
                    if ":" in value:
                        tag_name, tag_desc = value.split(":")
                        tag.TagDescription = tag_desc
                        tag.TagName = tag_name
                        col_value.update({name.value: tag})
                    else:
                        tag.TagName = value
                        col_value.update({name.value: tag})

            values.append(col_value)
            row_data.Replacements = col_value
            __items.append(row_data)
        values.clear()
        __count += 1
    return __items


if __name__ == "__main__":
    items = get_sheet_values(f_path)
    for item in items:
        print(item)
        print("Accessing one single value (eg. Program): {0}".format(item.Program))
