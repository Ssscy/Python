import itchat,requests,json
from itchat.content import *

apiUrl = 'http://www.tuling123.com/openapi/api'
apiKey = 'a72a0b16fc50453cb9c2f7d35b312282'

@itchat.msg_register(TEXT)
def auto_reply(msg):
    fromUser = msg['FromUserName']
    info = msg['Text'].encode('utf-8')
    payload = {'key': apiKey, 'info': info}
    headers = {'Content-type': 'text/html', 'charset': 'utf-8'}
    response = requests.post(apiUrl, data=json.dumps(payload), headers=headers)
    reply = json.loads(response.text).get('text')

    myself = itchat.search_friends()['UserName']
    if not fromUser == myself:
        itchat.send(reply,toUserName=msg['FromUserName'])


itchat.auto_login(hotReload=True)
itchat.run()
