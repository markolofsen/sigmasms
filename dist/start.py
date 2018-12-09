import requests, json


class SIGMA(object):

    token = False
    default_sender = 'B-Media'

    def __init__(self, username, password):

        post = {
            'username': username,
            'password': password,
        }

        r = requests.post(url='https://online.sigmasms.ru/api/login', json=post)
        response = r.content.decode('utf8')
        self.token = json.loads(response)['token']

    def send(self, recipients=[], message='Empty', sender=default_sender):

        headers = {
            'charset': 'utf-8',
            'Content-Type': 'application/json',
            'Authorization': self.token,
            'Access-Control-Allow-Origin': '*',
            # 'X-RateLimit-Limit': 100000,
            # 'X-RateLimit-Remaining': 99999,
            # 'X-Frame-Options': 'SAMEORIGIN',
        }

        post = {
            "recipient": recipients,
            "type": "sms",
            "payload": {
                "sender": sender,
                "text": message,
            }
        }

        r = requests.post(url='https://online.sigmasms.ru/api/sendings', json=post, headers=headers)
        response = r.content.decode('utf8')
        return json.loads(response)


    def status(self, msg_id=''):
        headers = {
            'charset': 'utf-8',
            'Content-Type': 'application/json',
            'Authorization': self.token,
        }

        r = requests.get(url='https://online.sigmasms.ru/api/sendings/{msg_id}'.format(msg_id=msg_id), headers=headers)
        response = r.content.decode('utf8')
        return json.loads(response)


if __name__ == '__main__':
    
    pass

    sigma_username = '****'
    sigma_password = '****'

    res = SIGMA(username=sigma_username, password=sigma_password).send(sender='B-Media', message='Hello Mark!!!', recipients=['+34649052927',])
    print(res)


    # msg_id = 'c81736cd-2919-4e6f-ac91-********'
    # msg_id = res['id']
    # status = SIGMA(username=sigma_username, password=sigma_password).status(msg_id=msg_id)
    # print(status)
    