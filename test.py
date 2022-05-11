import unittest
from app.models import User, Pitch, Comments

class UserModelTest(unittest.TestCase):
    def setUp(self):
        self.new_user = User("Michelle", "michelle@gmail.com", "1234")

    def test_instance(self):
        self.assertTrue(isinstance(self.new_user, User))

    def test_password_setter(self):
        self.assertTrue(self.new_user.password is not None)
    
    def test_no_access_password(self):
        with self.assertRaises(AttributeError):
            self.new_user.secure_password

class PitchModelTest(unittest.TestCase):
    def setUp(self):
        self.new_pitch = Pitch("Pitch Title","Pitch Category","Pitch Body","User ID")

    def test_instance(self):
        self.assertTrue(isinstance(self.new_pitch, Pitch))


class CommentModelTest(unittest.TestCase):
    def setUp(self):
        self.new_pitch = Comments("User ID","Comment Body","Pitch ID")

    def test_instance(self):
        self.assertTrue(isinstance(self.new_pitch, Comments))

   
if __name__ == '__main__':
    unittest.main()


        