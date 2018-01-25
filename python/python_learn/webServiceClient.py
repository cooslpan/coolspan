
#encoding:utf-8
#调用WebService的客户端
from suds.client import Client

ip = '127.0.0.1'
port = 8000
client = Client("http://%s:%s/?wsdl" % (ip, port))
#print(client)

### say_hello_plus
name = {}
name["first_name"] = "Kylin"
name["last_name"] = "Shu"

names = client.factory.create("NameArray")
names.Name.append(name)
names.Name.append(name)

r = client.service.say_hello_plus(names)
print(r)

### say_hello_plus2
names = client.factory.create("stringArray")
name = "Kylin"
names.string.append(name)
names.string.append(name)

#r = client.service.say_hello('AAA', 2)
#print(r)
r = client.service.say_hello_plus2(names)
print(r)