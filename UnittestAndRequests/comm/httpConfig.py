import requests
import json
class httpConfig():
    #封装两个方法，请求类型分别是get和post,然后根据请求类型调用不同的方法
    def send_post(self,url,data):
        response= requests.post(url=url,data=data)
        res=response.text
        return res
    def send_get(self,url,data):
        response=requests.get(url=url,data=data)
        res=response.text
        return res
    def choose_method(self,method,url,data):#根据传入的method类型来判断调用哪个方法
        if method=="post" or method=="POST":
            result=self.send_post(url,data)
        elif method=="get" or method=="GET":
            result=self.send_get(url,data)
        else:
            result={"暂不支持此请求类型！"}
        return result

if __name__=="__main__":
    res=httpConfig().choose_method("post","http://127.0.0.1:8888/login", {'username': 'root','pwd':'123456'})
    print(res)