from simplyhosting.client import Client
import unittest

class Test_ip(unittest.TestCase):
    def setUp(self):
        self.client = Client(api_key='a', api_secret='b')
        self.optional_data={'optionalParam': 'value'}

    def test_set_ptr_set_data_successfully(self):
        self.client.ip().set_ptr('192.168.0.1', self.optional_data)
        request = self.client.request
        self.assertEqual('192.168.0.1', request.data['ip'])
        self.assertEqual('value', request.data['optionalParam'])