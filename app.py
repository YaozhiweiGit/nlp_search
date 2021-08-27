#!/usr/bin/python3
# -*- encoding: utf-8 -*-
'''
@File    :   app.py
@Time    :   2021/08/26 19:07:57
@Author  :   yaozhiwei 
@Version :   1.0
@Contact :   1322093265@qq.com
'''

# here put the import lib
from  flask import  request,Flask,jsonify
import flask
import json

import synonyms
# print("飞机： ",synonyms.nearby("飞机"))
# #首先app = Flask(__name__)这部分是一个初始化的过程;__name__代表当前的python文件。把当前的python文件当做一个服务启动
app = Flask(__name__)
app.debug = True
@app.route('/test/')
# 这是个事例get访问本机http://0.0.0.0:7777/index 响应信息"msg":"这是个响应信息","msg_code":"0000"
@app.route("/nlp_search",methods=['get','post'])
def nlp_search():
    keyword = flask.request.values.get('keyword')
    if keyword:
        try:
            keywords = str(synonyms.nearby(keyword))
        except Exception as e:
            print("调用synmoyms报错")
        if '[]' in keywords:
            res = {"msg":"接口调用成功","msg_code":"1",keyword:'未查询到有关数据'}
        else:
            res = {"msg": "接口调用成功", "msg_code": "0", keyword: keywords}
    else :
        res={"msg":"接口调用失败，请携带关键词重新请求","msg_code":"2"}
    return json.dumps(res,ensure_ascii=False)



    # if not request.data:  # 检测是否有数据
    #     return ('fail')
    # 获取到POST过来的数据，因为我这里传过来的数据需要转换一下编码。根据具体情况而定
    # keyword = request.data.decode('utf-8')
    # # 把区获取到的数据转为JSON格式
    # student_json = json.loads(keyword)
    # # 返回JSON数据
    # return jsonify(student_json)


#这是个实例post请求,定义的接口只有两个参数'username'、'password'，没有任何业务校验，参数都不为空则服务返回接口调用成功，参数为空则服务返回接口调用失败
# @server.route('/index',methods=['get','post'])
# def index():
#     #那么如果要接受传入的参数，则可用以下方法
#     keyword=flask.request.values.get('keyword')
#     if keyword:
#         res={"msg":"接口调用成功","msg_code":"0000",'result':keyword}
#     else :
#         res={"msg":"接口调用失败，必填项为空","msg_code":"9999"}
#     return json.dumps(res,ensure_ascii=False)
if __name__ == "__main__":
    app.run(port=5000, host='0.0.0.0')