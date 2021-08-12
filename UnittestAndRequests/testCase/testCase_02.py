#一次能执行一个excel中全部的用例数据
import unittest
from comm.getUrlParams import getUrlParams
from comm import readExcel
from comm import httpConfig
import time
from BeautifulReport import BeautifulReport
from comm import getPathInfo
#调用getUrlParams方法获取我们拼接的基础url
base_url = getUrlParams().get_url()
lst = []
class testUserLogin(unittest.TestCase):
    @classmethod
    def setUpClass(self):
        #根据excel中数据的条数，循环来读取数据，添加到列表lst中
        rowNumber = 3
        for i in range(1,rowNumber+1):
            # 调用readExcel方法读取用例excel文件
            test_xls = readExcel.readExcel().get_excel("userCase.xls", "Sheet1", i)
            lst.append(test_xls)
    def setUp(self):
        print("baseurl:",base_url)

    def tearDown(self):
        print("测试结束，输出log完结")
    #添加测试方法
    def test_checkResult(self):
        for item in lst:
            request_method = item[1]
            request_date = eval(item[3])
            expect_data = eval(item[4])
            expect_code = expect_data["code"]
            expect_message = expect_data["message"]
            resp = httpConfig.httpConfig().choose_method(request_method,base_url,request_date)
            res = eval(resp)#转换一下类型
            self.assertEqual(res["code"],expect_code)
            self.assertEqual(res["message"],expect_message)
#结合beautifulReport
if __name__ == '__main__':
    nowTime = time.strftime("%Y%m%d%H%M%S")
    filename = '测试报告_'+nowTime
    filepath = '../report'
    suite = unittest.TestSuite()
    suite.addTest(testUserLogin("test_checkResult"))
    result = BeautifulReport(suite)
    result.report(filename=filename, description='testUserLogin.测试报告',report_dir=filepath)
