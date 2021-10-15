from unittest import TestCase, main
from welltest.functions import *

class WellTestCase(TestCase):
    def test_r_from_rd_m(self):
        self.assertEqual(r_from_rd_m(1), 0.1)


# Executing the tests in the above test case class
if __name__ == "__main__":
  main()