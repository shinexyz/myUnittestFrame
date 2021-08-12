#一次只能读取一条excel数据出来执行
import json
import unittest
#from comm.httpConfig import httpConfi
from comm.getUrlParams import getUrlParams
from comm import readExcel
from comm import httpConfig
#调用getUrlParams方法获取我们拼接的基础url
base_url = getUrlParams().get_url()
#调用readExcel方法读取用例excel文件
test_xls = readExcel.readExcel().get_excel("userCase.xls","Sheet1",1)
class testUserLogin(unittest.TestCase):
    def setUp(self):
        print("baseurl:",base_url)

    def tearDown(self):
        print("测试结束，输出log完结")
    #添加测试方法
    def checkResult(self):
        raw_data = test_xls[3]#获取表格中的用户名和密码
        data = eval(raw_data)#是str形式的，需要转换成dict形式，不然会一直报参数为空
        print(type(data))
        # #发送请求
        res=httpConfig.httpConfig().choose_method('post',base_url,data)
        #将响应转化为字典格式
        resp = json.loads(res)
        print(resp)
        self.assertEqual(resp["code"],"0000")
        self.assertEqual(resp["message"],"登录成功")
if __name__ == '__main__':
    suite = unittest.TestSuite()
    suite.addTest(testUserLogin("checkResult"))
    runner = unittest.TextTestRunner()
    runner.run(suite)
