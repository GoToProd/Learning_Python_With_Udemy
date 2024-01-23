import unittest
import lesson

class FizzbuzzTestCase(unittest.TestCase):
    
    def test_fizz(self):
        number = 3
        result = lesson.getReply(number)
        self.assertEquals(result, 'Fizz')
        
    def test_buzz(self):
        number = 5
        result = lesson.getReply(number)
        self.assertEquals(result, 'Buzz')
        
    def test_fizzbuzz(self):
        number = 15
        result = lesson.getReply(number)
        self.assertEquals(result, 'FizzBuzz')
        
if __name__ == '__main__':
    unittest.main()