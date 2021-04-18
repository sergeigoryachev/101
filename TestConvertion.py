import unittest
import os
from csvtoparquet import convert_to_parquet

class TestConvertion(unittest.TestCase):
    def setUp(self):
        pass

    def test_extension(self):
        files = convert_to_parquet()
        result = all(True for item in files if item.endswith(".parquet"))
        self.assertEqual(result, True)

if __name__ == "__main__":
    unittest.main()



