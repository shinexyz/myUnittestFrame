from flask import request
import flask
import json

#创建一个服务，把当前这个python文件作为一个服务
server = flask.Flask(__name__)
#@server.route将普通的函数转换为服务，里面是登录路径，支持的请求方式
@server.route('/login',methods=['get','post'])
def login():
    #获取url中传递的请求参数
    username = request.values.get('username')
    pwd = request.values.get('pwd')
    #根据用户名和密码来模拟几种情况
    if username and pwd:
        if username =="root" and pwd=="123456":
            resu={"code":"0000","message":"登录成功"}
            return json.dumps(resu,ensure_ascii=False)#将字典转换成json格式
        else:
            resu={"code":"1001","message":"账号或密码错误"}
            return json.dumps(resu, ensure_ascii=False)
    else:
        resu = {"code": "1005", "message": "必填参数为空"}
        return json.dumps(resu, ensure_ascii=False)
if __name__ == '__main__':
    server.run(debug=True, port=8888, host='127.0.0.1')