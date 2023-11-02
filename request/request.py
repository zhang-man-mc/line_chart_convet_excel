import requests


class MyRequest:
    def __init__(self):
        requests.packages.urllib3.disable_warnings()
        self.session = requests.session()
        self.session.headers = {
            "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/114.0.0.0 Safari/537.36",
        }

    # def get_session(self):
    #     if self.session == None :
    #         requests.packages.urllib3.disable_warnings()
    #         self.session = requests.session()
    #         self.session.headers = {
    #             'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/114.0.0.0 Safari/537.36',
    #         }
    #     return self.session

    def post(self, url, data):
        r = self.get_session().post(url, data=data, verify=False)
        if r.status_code != 200:
            return False
        return r.text


_my_request = MyRequest()
request_post = _my_request.post
