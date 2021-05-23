import unittest
import os
import hashlib
import time
from csvtoparquet import convert_to_parquet

CHUNK = 65536
class TestConvertion(unittest.TestCase):
    def setUp(self):
        pass

    def test_extension(self):
        start = time.time()
        files_hash = []
        files = convert_to_parquet()
        for item in files:
            md5 = hashlib.md5()
            with open(item, 'rb') as test_parquet_file:
                while True:
                    data = test_parquet_file.read(CHUNK)
                    if not data:
                        break
                    md5.update(data)
            print(md5.hexdigest())
            self.assertEqual(test_parquet_file, files)
        finish = time.time()
        print(finish - start)
        
if __name__ == "__main__":
    unittest.main()
