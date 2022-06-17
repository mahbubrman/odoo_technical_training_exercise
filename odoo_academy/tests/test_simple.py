from odoo.tests.common import TransactionCase
from odoo.tests import tagged


@tagged('at_install', 'post_install')
class TestSimples(TransactionCase):

    def setUp(self, *args, **kwargs):
        super().setUp(*args, **kwargs)
        print("Simple Test setup done")

    def test_equal(self):
        """Testing Assertion for equals"""
        self.assertEqual(5+8, 13)
