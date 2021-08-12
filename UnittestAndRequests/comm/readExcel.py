import os
from comm import getPathInfo #导入我们自己写的类，返回项目的绝对路径
from xlrd import open_workbook
import json
path=getPathInfo.get_path()

class readExcel():
    def get_excel(self,xls_name,sheet_name,id):#xls_name-用例的excel文件名称，sheet_name-excel中的sheetName
        case=[]#使用列表来存放我们excel文件中的内容
        xls_path = os.path.join(path,'../data',xls_name)
        file=open_workbook(xls_path)
        sheet=file.sheet_by_name(sheet_name)#根据sheet_name来获取打开的Excel文件中的sheet
        # 读取指定的行数
        ls = sheet.row_values(id)
        return ls
if __name__=="__main__":
    ls=readExcel().get_excel("userCase.xls", "Sheet1",1)
    print(ls)
