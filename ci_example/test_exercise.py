# Contains all of the unit tests to grade Part 2 of the assignment: vim configuration

import unittest
import subprocess
import json
import inspect


class TestExercise(unittest.TestCase):
    def test_return10(self):
        """Ensures that the return10 function returns 10 with high probability"""
        import exercise

        for _ in range(100000):
            self.assertEqual(10, exercise.return10(), "\nreturn10 did not return 10")

    def test_buildList_return(self):
        """ensures that buildList returns a list from 0 to 9"""
        import exercise

        self.assertEqual(
            [i for i in range(10)], exercise.buildList(), "\nbuildList did not return a list from 0 to 9 (inclusive)"
        )
        self.assertRegex(
            inspect.getsource(exercise.buildList),
            r"for\s+(?:.*?)\s+in\s+range\s*\((?:0\s*,\s*)?\s*10\):",
            "\nwe didn't detect that buildList has been changed to use a for loop",
        )

    def test_buildList_for_loop(self):
        """ensures that buildList uses a for loop"""
        import exercise

        self.assertRegex(
            inspect.getsource(exercise.buildList),
            r"for\s+(?:.*?)\s+in\s+range\s*\((?:0\s*,\s*)?\s*10\):",
            "\nwe didn't detect that buildList has been changed to use a for loop",
        )

    def test_isPalindrome(self):
        """Ensures isPalindrome works on basic cases"""
        import exercise

        self.assertTrue(exercise.isPalindrome("123x321"), "\nisPalindrome should return true for 123x321")
        self.assertTrue(exercise.isPalindrome("123321"), "\nisPalindrome should return true for 123321")
        self.assertFalse(exercise.isPalindrome("12332"), "\nisPalindrome should return false for 12332")
        self.assertFalse(exercise.isPalindrome("Jonathan"), "\nisPalindrome shuold return false for Jonathan")

    def test_palindromeNames(self):
        """Ensures palindromeNames returns the correct answers given our test cases above"""
        import exercise

        self.assertEqual(["123x321", "123321"], exercise.palindromeNames(["123x321", "123321", "12332", "Jonathan"]))

    def test_palindromeNames_decomp(self):
        """Ensures palindromeNames uses isPalindrome"""
        import exercise

        self.assertIn(
            "isPalindrome(name)",
            inspect.getsource(exercise.palindromeNames),
            "\nwe didn't detect that palindromeNames was decomposed",
        )

if __name__ == '__main__':
    unittest.main()