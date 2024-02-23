import unittest
import lfuncs

class TestCounterMethods(unittest.TestCase):

    def test_find_startswith_in_list(self):
        test_list = ["aa", "ab", "bc"]
        result = lfuncs.find_startswith_in_list("a", test_list)
        self.assertEqual(["ab"], result)

    def test_find_startswith_in_list_no_results(self):
        test_list = ["aa", "ab", "bc"]
        result = lfuncs.find_startswith_in_list("c", test_list)
        self.assertEqual([], result)

    def test_find_endswith_in_list(self):
        test_list = ["aa", "ab", "cb"]
        result = lfuncs.find_endswith_in_list("b", test_list)
        self.assertEqual(["ab", "cb"], result)

    def test_find_endswith_in_list_no_results(self):
        test_list = ["aa", "ab", "cb"]
        result = lfuncs.find_endswith_in_list("c", test_list)
        self.assertEqual([], result)

    def test_split_lists(self):
        test_list = ["aa", "ab", "cb"]
        result1, result2 = lfuncs.split_lists(test_list, "a")
        self.assertEqual(["aa", "ab"], result1)
        self.assertEqual(["cb"], result2)

    def test_split_lists_no_prefix(self):
        test_list = ["aa", "ab", "cb"]
        result1, result2 = lfuncs.split_lists(test_list, "b")
        self.assertEqual([], result1)
        self.assertEqual(["aa", "ab","cb"], result2)

if __name__ == '__main__':
    unittest.main()
