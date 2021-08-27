#/usr/bin/python3
#-*-    coding=utf-8    -*-
#@Time  :   2021/8/27/027 
#@Author :  yaozhiwei
#@File : test.py
#@Software : PyCharm
import synonyms
aa = synonyms.nearby("渡漆")
aa = str(aa)
res={"msg":"接口调用成功","msg_code":"0000",'渡漆':aa}
print(res)