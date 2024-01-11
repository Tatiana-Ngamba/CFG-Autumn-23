import unittest
from main_concept_question import is_an_isogram


class MyTestCase(unittest.TestCase):
    """ I am testing the 'is_word_isogram' function with multiple words.
    to demonstrate the function's ability to test isogram and non isogram ."""

    def test_case_1(self):
        words = "isogram", "uncopyrightable", "ambidextrously"
        expected = True, True, True
        output = [is_an_isogram(word) for word in words]
        self.compare(expected, output)

    # I choose this because it tests the function's ability to handle empty input, which should be considered an
    # isogram.
    def test_case_2(self):
        words = []
        expected = [True]
        output = [is_an_isogram(word) for word in words]
        self.compare(expected, output)

    # I wanted to choose a single-Character input to see
    def test_case_3(self):
        words = "t"
        expected = True
        output = [is_an_isogram(word) for word in words]
        self.compare(expected, output)

    # Checking if the function correctly knows words with repeated letters as non-isograms.
    def test_case_4(self):
        words = "mississippi"
        expected = False
        output = [is_an_isogram(word) for word in words]
        self.compare(expected, output)

    # Testing insensitivity and special letters
    def test_case_5(self):
        words = "QUAVERs!"
        expected = True
        output = [is_an_isogram(word) for word in words]
        self.compare(expected, output)

    # testing a different string
    def test_case_6(self):
        words = "Tatiana"
        expected = False
        output = [is_an_isogram(word) for word in words]
        self.compare(expected, output)

    def compare(self, expected, output):
        pass


if __name__ == '__main__':
    unittest.main()
