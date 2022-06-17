from odoo.tests.common import TransactionCase


class TestBook(TransactionCase):
    def setUp(self, *args, **kwargs):
        super().setUp(*args, **kwargs)

        # Test with access_security
        user_admin = self.env.ref("base.user_admin")
        self.env(user=user_admin)

        # Create a test book entry
        self.Book = self.env["library.book"]
        self.book1 = self.Book.create({
            "name": "Odoo Development Essentials",
            "isbn": "879-1-78439-279-6"})

    def test_book_create(self):
        """New Books are active by default"""
        self.assertEqual(self.book1.active, True)
