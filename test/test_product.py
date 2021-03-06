from simplyhosting.client import Client
import unittest


class Test_product(unittest.TestCase):
    def setUp(self):
        self.client = Client(api_key='a', api_secret='b')
        self.optional_data={'optionalParam': 'value'}

    def test_get_product_list_set_data_successfully(self):
        self.client.product().get_product_list(self.optional_data)
        request = self.client.request
        self.assertEqual('value', request.data['optionalParam'])

    def test_get_config_options_set_data_successfully(self):
        self.client.product().get_config_options(1)
        request = self.client.request
        self.assertEqual(1, request.data['productId'])

    def test_get_addons_set_data_successfully(self):
        self.client.product().get_addons(1)
        request = self.client.request
        self.assertEqual(1, request.data['productId'])

    def test_order_products_set_data_successfully(self):
        self.client.product().order_products(1, 'card', self.optional_data)
        request = self.client.request
        self.assertEqual(1, request.data['productId'])
        self.assertEqual('card', request.data['paymentMethod'])
        self.assertEqual('value', request.data['optionalParam'])

    def test_order_history_set_data_successfully(self):
        self.client.product().order_history(1)
        request = self.client.request
        self.assertEqual(1, request.data['orderId'])

    def test_cancel_service_set_data_successfully(self):
        self.client.product().cancel_service(1, 'My reason', self.optional_data)
        request = self.client.request
        self.assertEqual(1, request.data['serviceId'])
        self.assertEqual('My reason', request.data['reason'])
        self.assertEqual('value', request.data['optionalParam'])

    def test_cancel_pending_order_set_data_successfully(self):
        self.client.product().cancel_pending_order(1)
        request = self.client.request
        self.assertEqual(1, request.data['orderId'])

    def test_upgrade_service_set_data_successfully(self):
        self.client.product().upgrade_service(1, '22,69')
        request = self.client.request
        self.assertEqual(1, request.data['serviceId'])
        self.assertEqual('22,69', request.data['configOptions'])
