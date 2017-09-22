#coding=utf-8
#import urllibc
import suds
import sys
reload(sys)
sys.setdefaultencoding('utf-8')
def TestSuds() :
    try:
          from suds import WebFault
          from suds.client import Client
          from suds.xsd.doctor import ImportDoctor, Import
          imp = Import('http://www.w3.org/2001/XMLSchema', location='http://www.w3.org/2001/XMLSchema.xsd')
          imp.filter.add('http://WebXml.com.cn/')
          doc = ImportDoctor(imp)
          url = 'http://www.webxml.com.cn/WebServices/WeatherWebService.asmx?wsdl'
          client = Client(url, doctor=doc, cache=None)
          print (client)
          print (client.service.getWeatherbyCityName ('温州'))
    except Exception as err:
        print(err)
TestSuds()