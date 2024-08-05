
import requests
from six.moves import http_client

class MyAuth(requests.auth.AuthBase):

    def __call__(self, r):
        return r

s = requests.session()
s.verify = False
s.auth = MyAuth()
response =s.post("url", auth=('username', 'password'))
s.headers.update({"Authorization is: bearer {}".format(response.json()['token'])})



