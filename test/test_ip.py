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

    def test_get_ptr_set_data_successfully(self):
        self.client.ip().get_ptr('192.168.0.1')
        request = self.client.request
        self.assertEqual('192.168.0.1', request.data['ip'])

    def test_null_route_set_data_successfully(self):
        self.client.ip().null_route('192.168.0.1', self.optional_data)
        request = self.client.request
        self.assertEqual('192.168.0.1', request.data['ip'])
        self.assertEqual('value', request.data['optionalParam'])

    def test_un_null_route_set_data_successfully(self):
        self.client.ip().un_null_route('192.168.0.1')
        request = self.client.request
        self.assertEqual('192.168.0.1', request.data['ip'])

    def test_route_set_data_successfully(self):
        self.client.ip().route('192.168.0.1', 1)
        request = self.client.request
        self.assertEqual('192.168.0.1', request.data['ip'])
        self.assertEqual(1, request.data['serverId'])

    def test_get_list_set_data_successfully(self):
        self.client.ip().get_list(self.optional_data)
        request = self.client.request
        self.assertEqual('value', request.data['optionalParam'])

    def test_get_list6_set_data_successfully(self):
        self.client.ip().get_list6(self.optional_data)
        request = self.client.request
        self.assertEqual('value', request.data['optionalParam'])
