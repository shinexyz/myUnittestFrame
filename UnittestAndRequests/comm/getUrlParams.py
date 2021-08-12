from comm import readConfig
'''
调用readConfig文件里写的方法，获取配置文件中的baseurl来拼接出我们实际需要的url
'''
readConfig = readConfig.getConfig()
class getUrlParams():
    def get_url(self):
        new_url = readConfig.get_http("scheme")+'://'+readConfig.get_http('baseUrl')+':8888'+'/login'+'?'
        return new_url

#print(getUrlParams().get_url())
#http://127.0.0.0:8888/login?