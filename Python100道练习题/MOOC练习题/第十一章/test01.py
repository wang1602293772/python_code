import unittest


def get_format_name(first, last):
    full_name = first + ' ' + last
    return full_name.title()


class Test_get_format_name(unittest.TestCase):
    def test_name(self):
        get_format = get_format_name('a', 'b')
        self.assertEqual(get_format, 'A B')


unittest.main(argv=['ignored', '-v'], exit=False)
