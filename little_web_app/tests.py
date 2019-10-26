import unittest
import little_web_app


class TestHello(unittest.TestCase):

    def setUp(self):
        little_web_app.app.testing = True
        self.app = little_web_app.app.test_client()

    def test_hello(self):
        rv = self.app.get('/')
        self.assertEqual(rv.status, '200 OK')
        self.assertEqual(rv.data, b'Hello World')

    def test_hello_count(self):
        rv = self.app.get('/hellos/3')
        self.assertEqual(rv.status, '200 OK')
        self.assertEqual(rv.data, b'hello\n\nhello\n\nhello\n\n')

    def test_hello_name(self):
        name = 'Simon'
        rv = self.app.get(f'/hello/{name}')
        self.assertEqual(rv.status, '200 OK')
        self.assertIn(bytearray(f"{name}", 'utf-8'), rv.data)

if __name__ == '__main__':
    unittest.main()