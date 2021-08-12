import os
from comm import getPathInfo
import configparser
path=getPathInfo.get_path()#实例化，先获取文件所在的路径
config_path=os.path.join(path, '../config/config.ini')#然后把文件路径和文件名拼接起来，获得文件的绝对路径
config=configparser.ConfigParser()#调用外部的读取配置文件的方法
config.read(config_path,encoding="utf-8")#读取文件中的内容

class getConfig():
    def get_http(self,name):
        value = config.get("HTTP",name)
        return value
    def get_EMAIL(self,name):
        value = config.get("EMAIL",name)
        return value
if __name__=="__main__":
    print("HTTP的baseUrl配置为：",getConfig().get_http("baseUrl"))
    print("发送邮件消息的开关为：",getConfig().get_EMAIL("on_off"))