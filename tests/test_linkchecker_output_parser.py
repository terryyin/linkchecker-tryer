import unittest
from linkchecker_tryer import parse_linkchecker_output, filter_out_good_links


class Test_parse_raw_output(unittest.TestCase):

    def test_parse_empty_output(self):
        result = parse_linkchecker_output("")
        self.assertEqual(result, [])

    def test_parse_one_link(self):
        result = parse_linkchecker_output('''
URL        `https://link'
Name       `name'
Parent URL parent_url
Check time 0.059 seconds
''')
        self.assertEqual(result, [{"url":"https://link", "name":"name", "parent_url":"parent_url"}])


class Test_links_filter(unittest.TestCase):

    def test_should_return_empty_when_input_empty(self):
        result = filter_out_good_links([])
        self.assertEqual(result, [])

