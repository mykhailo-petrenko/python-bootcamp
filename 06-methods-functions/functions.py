def pig_latin(word):
    first_letter = word[0]
    is_vowel = first_letter in 'aeiou'

    return word[(not is_vowel):] + (first_letter * (not is_vowel)) + 'ay'


import unittest

class TestPigLatin(unittest.TestCase):
    def test_vovwel(self):
        self.assertEqual(pig_latin('apple'), 'appleay')

    def test_consonant(self):
        self.assertEqual(pig_latin('word'), 'ordway')

if __name__ == '__main__':
    unittest.main()