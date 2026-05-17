import unittest
from utils.validators import validate_email

class TestValidators(unittest.TestCase):
    def test_email_regex(self):
        self.assertTrue(validate_email("test@example.com"))
        self.assertFalse(validate_email("invalid-email"))

if __name__ == "__main__":
    unittest.main()
