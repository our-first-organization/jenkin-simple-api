import unittest
from app import app

class TestFlaskAPI(unittest.TestCase):
    
    def setUp(self):
        self.app = app.test_client()
        self.app.testing = True
    
    def test_plus(self):
        response = self.app.get('/plus/5/6')
        self.assertEqual(response.status_code, 200)
        self.assertEqual(response.data.decode('utf-8'), '11')

if __name__ == '__main__':
    unittest.main()
