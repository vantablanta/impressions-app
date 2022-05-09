import unittest
from app.models import User, Pitch, Comments

class UserModelTest(unittest.TestCase):
    def setUp(self):
        self.new_user = User(password='michelle/2020')

    def test_instance(self):
        self.assertTrue(isinstance(self.new_pitch, Pitch))

    def test_password_setter(self):
        self.assertTrue(self.new_user.pass_secure is not None)
    
    def test_no_access_password(self):
        with self.assertRaises(AttributeError):
            self.new_user.secure_password

    def test_password_verification(self):
        self.assertTrue(self.new_user.verify_password('michelle/2020'))

class PitchModelTest(unittest.TestCase):
    def setUp(self):
        self.new_pitch = Pitch("","","","")

    def test_instance(self):
        self.assertTrue(isinstance(self.new_pitch, Pitch))


class CommentModelTest(unittest.TestCase):
    def setUp(self):
        self.new_pitch = Comments("","","","")

    def test_instance(self):
        self.assertTrue(isinstance(self.new_pitch, Comments))

   
if __name__ == '__main__':
    unittest.main()


        