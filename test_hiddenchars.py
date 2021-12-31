import unittest
from hiddenchars import HiddenChars

class TestHiddenChars(unittest.TestCase):
    def __init__(self, *args, **kwargs):
        super(TestHiddenChars, self).__init__(*args, **kwargs)
        self.hiddenChars = HiddenChars("unicodeEmojis.json")

    def test_getReveal_nohiddenchars(self):
        # Arrange
        expected = "🐋🐋🐋"
        input = "🐋🐋🐋"

        # Act
        actual = self.hiddenChars.getReveal(input) 

        # Assert
        self.assertEqual(actual, expected)

    def test_getReveal_hidden200D(self):
        # Arrange
        expected = f"{self.hiddenChars.revealSymbol}eth.eth"
        input = "‍eth.eth"

        # Act
        actual = self.hiddenChars.getReveal(input) 

        # Assert
        self.assertEqual(actual, expected)

    def test_getReveal_hiddenFE0F(self):
        # Arrange
        expected = f"🐋{self.hiddenChars.revealSymbol}"*3
        input = "🐋️🐋️🐋️"

        # Act
        actual = self.hiddenChars.getReveal(input) 

        # Assert
        self.assertEqual(actual, expected)

    def test_getReveal_testUmlaute(self):
        # Arrange
        expected = "ähh.eth"
        input = "ähh.eth"

        # Act
        actual = self.hiddenChars.getReveal(input) 

        # Assert
        self.assertEqual(actual, expected)

if __name__ == '__main__':
    unittest.main()