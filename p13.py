# http://www.pythonchallenge.com/pc/return/disproportional.html
# http://www.pythonchallenge.com/pc/return/italy.html

import xmlrpc.client
import ctx

sr = xmlrpc.client.ServerProxy('http://www.pythonchallenge.com/pc/phonebook.php')
# print(sr.system.listMethods())
# print(sr.system.methodHelp("phone"))

print(sr.phone("Bert"))
