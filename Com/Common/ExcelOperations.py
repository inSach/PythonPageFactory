import openpyxl


class ExcelOperations():
    def __init__(self, file_path):
        self.wb = openpyxl.load_workbook(file_path)


    def get_worksheet(self, sheet_name):
        wb = self.wb
        ws = wb.get_sheet_by_name(sheet_name)
        return ws


    def get_ws_cell(self, sheet_name, x, y):
        ws = self.get_worksheet(sheet_name)
        cell_object = ws.cell(x, y)
        return cell_object