import unittest
from arc import File
import keywords

class TestFile(unittest.TestCase):
    def test_1(self):
        kw = keywords.keywords
        filename = keywords.filename
        f = File(filename, kw)
        f.rename_to_keywords()
        print(f.keywords)

if __name__ == '__main__':
    unittest.main()


