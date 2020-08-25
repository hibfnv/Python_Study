"""通过导入test包来进行程序最后的测试过程"""
import unittest
from Chap11.user_names import get_formatted_name


class NamesTestCase(unittest.TestCase):
    """测试name_function.py"""

    def test_first_last_name(self):
        """能否正确处理像Joseph Colin这样的姓名吗"""
        formatted_name = get_formatted_name('Joseph', 'Colin')
        self.assertEqual(formatted_name, 'Joseph Colin')

    def test_first_last_middle_name(self):
        """能否正确处理像 Thomas Green Swift这样的姓名吗"""
        formatted_name = get_formatted_name("Thomas", "Green", "Swift")
        self.assertEqual(formatted_name, "Thomas Green Swift")


unittest.main()
