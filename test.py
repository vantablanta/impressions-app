import unittest
from app.models import User, Pitch, Comments

class UserModelTest(unittest.TestCase):
    def setUp(self):
        self.new_user = User(password='michelle/2020')

    def test_password_setter(self):
        self.assertTrue(self.new_user.pass_secure is not None)
    
    def test_no_access_password(self):
        with self.assertRaises(AttributeError):
            self.new_user.secure_password

    def test_password_verification(self):
        self.assertTrue(self.new_user.verify_password('michelle/2020'))

class UserModelTest(unittest.TestCase):
    def setUp(self):
        self.new_pitch = Pitch(password='michelle/2020')

    def test_password_verification(self):
        self.assertEqual(self.new_pitch('michelle/2020'))


        