import requests
import json

#设置代理
proxies = {'http': 'http://localhost:8888', 'https': 'http://localhost:8888'}


#从api中获取已有的知识图谱
#返回类型是python字典类数据
def getDBpedia(str):
    url = 'https://api.ownthink.com/kg/knowledge?entity='+str
    response=requests.get(url,proxies=proxies)#这里返回的json数据
    # result=open('a.json','w')
    # result.write(response.text)#yang.text将yang这个json数据以字符形式使用
    # result.close()#这里一定要关闭文件，不然写不进去
    jsonFile=json.loads(response.text)
    return jsonFile

#将获取的json文件转化成三元组
def json2triad(jsonFile):
    result=[]
    if (jsonFile['message'] == 'success') and ('entity' in jsonFile['data']):
        entity=jsonFile['data']['entity']
        for item in jsonFile['data']['avp']:
            result.append([entity,item[0],item[1]])
    return result



json2triad(getDBpedia("宇宙学"))