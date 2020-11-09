import unittest
import create_regexp
import create_machine
import main
from constants import *


class TestWrongInput(unittest.TestCase):

    def test_invalid_input_symbols(self):
        with self.assertRaises(Exception):
            main.main('it is wrong input')

    def test_invalid_input_type(self):
        with self.assertRaises(Exception):
            main.main(['ab+c.', 'a', lambda x: x ** 2])

    def test_invalid_input_size(self):
        with self.assertRaises(Exception):
            main.main(['wrong', 'size'])


class TestCorrectTask(unittest.TestCase):

    def test_find_first_right_answer(self):
        self.assertEqual(main.main(['ab+c.aba.*.bac.+.+*', 'b', '2']), 'INF',
                         'Wrong answer for first test')

    def test_find_second_right_answer(self):
        self.assertEqual(main.main(['acb..bab.c.*.ab.ba.+.+*a.', 'a', '2']), '4',
                         'Wrong answer for second test')


class TestProgramMistakes(unittest.TestCase):

    def test_invalid_bracket_balance(self):
        with self.assertRaises(Exception):
            create_machine.GetExpressionAnderOperation('(a+b))')

    def test_invalid_plus_balance(self):
        with self.assertRaises(Exception):
            create_machine.GetExpressionAnderOperation('((a+b)+(a+b)+(a+b))')

    def test_first_invalid_operations_balance(self):
        with self.assertRaises(Exception):
            create_regexp.ParseRegExp('ab++')

    def test_second_invalid_operations_balance(self):
        with self.assertRaises(Exception):
            create_regexp.ParseRegExp('*')

    def test_third_invalid_operations_balance(self):
        with self.assertRaises(Exception):
            create_regexp.ParseRegExp('abc')


if __name__ == '__main__':
    unittest.main()
