import unittest
from hiddenchars import HiddenChars

class TestHiddenChars(unittest.TestCase):
    def __init__(self, *args, **kwargs):
        super(TestHiddenChars, self).__init__(*args, **kwargs)
        self.hiddenChars = HiddenChars("unicodeEmojis.json")

    def test_getReveal_nohiddenchars(self):
        # Arrange
        expected = "πππ"
        input = "πππ"

        # Act
        actual = self.hiddenChars.getReveal(input) 

        # Assert
        self.assertEqual(actual, expected)

    def test_getReveal_hidden200D(self):
        # Arrange
        expected = f"{self.hiddenChars.revealSymbol}eth.eth"
        input = "βeth.eth"

        # Act
        actual = self.hiddenChars.getReveal(input) 

        # Assert
        self.assertEqual(actual, expected)

    def test_getReveal_hiddenFE0F(self):
        # Arrange
        expected = f"π{self.hiddenChars.revealSymbol}"*3
        input = "ποΈποΈποΈ"

        # Act
        actual = self.hiddenChars.getReveal(input) 

        # Assert
        self.assertEqual(actual, expected)

    def test_getReveal_testUmlaute(self):
        # Arrange
        expected = "Γ€hh.eth"
        input = "Γ€hh.eth"

        # Act
        actual = self.hiddenChars.getReveal(input) 

        # Assert
        self.assertEqual(actual, expected)

if __name__ == '__main__':
    unittest.main()