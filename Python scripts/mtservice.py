import urllib

params = {}
params['authkey']= 'secret5'
params['mtserverid'] = 'MT4Live1'
params['login']= '1231231231'
params['password']='abc123'
params['group']='demoforex'
params['name']='Name2'
params['country']='B'
params['city']='C'
params['state']='D'
params['zip']='10007'
params['address']='E'
params['phone']='03'
params['email']='a@bc.com'
#params['ssn']=
params['leverage']='200'

params = urllib.urlencode(params)
f = urllib.urlopen("http://172.20.30.202:8088/createAccount",params)
print f.read()[:100]
#f.listen(100)