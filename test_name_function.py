"""通过导入test包来进行程序最后的测试过程"""
import unittest
from Chap11.user_names import get_formatted_name


class NamesTestCase(unittest.TestCase):
    """测试name_function.py"""

    def test_file_last_name(self):
        formatted_name = get_formatted_name('Thomas', 'Colin')
        self.assertEqual(formatted_name, 'Thomas Colin')


unittest.main()
