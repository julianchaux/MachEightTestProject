import unittest

from app import checkSumPair

class TestApp(unittest.TestCase):
    total_sum = 0
    numbers = []

    def setUp(self):
        self.total_sum = 10
        self.numbers = [1,15,14,25,-25,-1,6,4,-15,35]

    def test_app(self):
        result = checkSumPair(self.numbers, self.total_sum)
        if len(result):
            for i in range(len(result)):            
                self.assertEqual(result[i][0] + result[i][1], self.total_sum)
        else:
            print(f"No pair of numbers in {self.numbers} satisfies the total sum of {self.total_sum}")

if __name__ == '__main__':
    unittest.main()