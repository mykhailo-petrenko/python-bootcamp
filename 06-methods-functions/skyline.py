import unittest

def skyline(s):
    result = ''

    for i in range(len(s)):
        if i%2 == 0:
            result += s[i].lower()
        else:
            result += s[i].upper()

    return result


class TestSkyline(unittest.TestCase):
    def test_basic(self):
        self.assertEqual(skyline('Anthropomorphism'), 'aNtHrOpOmOrPhIsM')

if __name__ == '__main__':
    unittest.main()
