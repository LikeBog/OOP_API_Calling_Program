from abc_api_base import APIBase

BASE_URL = 'https://api.agify.io/'

class APIAgify(APIBase):
    def __init__(self, params, timeout=10):
        super().__init__(BASE_URL, params, timeout)

    def call_api(self):
        self.__data = self.get_api()
        return self.status, self.message

    def __str__(self):
        data = self.__data
        ret = f'\n{data['name']} is {data['age']} years old.'
        
        return ret
