import unittest
from translator import englishToFrench, frenchToEnglish
class TestEnglishToFrench(unittest.TestCase):
    def test_translation(self):
        english_text = "Hello"
        expected_french_text = "Bonjour"
        translated_text = englishToFrench(english_text)
        self.assertEqual(translated_text, expected_french_text)

class TestFrenchToEnglish(unittest.TestCase):
    def test_translation(self):
        french_text = "Bonjour"
        expected_english_text = "Hello"
        translated_text = frenchToEnglish(french_text)
        self.assertEqual(translated_text, expected_english_text)

if __name__ == '__main__':
    unittest.main()
