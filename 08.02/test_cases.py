import unittest

def reverseList(arr):
    for i in range(len(arr) // 2):
        right = len(arr) - 1 - i
        arr[i], arr[right] = arr[right], arr[i]
    return arr

def isPalindrome(arr):
    for i in range(len(arr) // 2):
        right = len(arr) - 1 - i
        if arr[i] != arr[right]:
            return False
    return True

def coin(change):
    coinAmount = []
    coinAmount.append(change // 25)
    change %= 25
    coinAmount.append(change // 10)
    change %= 10
    coinAmount.append(change // 5)
    change %= 5
    coinAmount.append(change)
    return coinAmount

def factorial(n):
    if n == 1:
        return 1
    else:
        return n * factorial(n - 1)

def fibonacci(n):
    if n == 0:
        return 0
    if n == 1:
        return 1
    return fibonacci(n-2) + fibonacci(n - 1)


class ReverseListTest(unittest.TestCase):
    def test_One(self):
        self.assertEqual(reverseList([1, 2, 3, 4, 5]), [5, 4, 3, 2, 1])

    def test_Two(self):
        self.assertEqual(reverseList([11, 12, 13, 14, 15]), [15, 14, 13, 12, 11])

    def test_Three(self):
        self.assertEqual(reverseList([0]), [0])

class IsPalindromeTest(unittest.TestCase):
    def test_One(self):
        self.assertEqual(isPalindrome("racecar"), True)
    def test_Two(self):
        self.assertEqual(isPalindrome("raceca"), False)
    def test_Three(self):
        self.assertEqual(isPalindrome("r"), True)

class CoinTest(unittest.TestCase):
    def test_One(self):
        self.assertEqual(coin(87), [3,1,0,2])
    def test_Two(self):
        self.assertEqual(coin(75), [3,0,0,0])
    def test_Three(self):
        self.assertEqual(coin(0), [0,0,0,0])

class FactorialTest(unittest.TestCase):
    def test_One(self):
        self.assertEqual(factorial(1), 1)
    def test_Two(self):
        self.assertEqual(factorial(2), 2)
    def test_Three(self):
        self.assertEqual(factorial(3), 6)

class FibonacciTest(unittest.TestCase):
    def test_One(self):
        self.assertEqual(fibonacci(0), 0)
    def test_Two(self):
        self.assertEqual(fibonacci(1), 1)
    def test_Three(self):
        self.assertEqual(fibonacci(2), 1)


def setUp(self):
    # add the setUp tasks
    print("running setUp")

# any task you want run after the tests are executed, put them in the tearDown method
def tearDown(self):
    # add the tearDown tasks
    print("running tearDown tasks")

if __name__ == '__main__':
    unittest.main()