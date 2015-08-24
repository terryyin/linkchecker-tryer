import unittest
from linkchecker_tryer import parse_linkchecker_output, filter_out_good_links


raw_link_checker_output = '''
URL        `https://link'
Name       `name'
Parent URL parent_url
Check time 0.059 seconds
'''

raw_link_checker_output2 = '''
URL        `https://link'
Name       `name'
Parent URL parent_url 2
Check time 0.059 seconds
'''



class Test_parse_raw_output(unittest.TestCase):

    def test_parse_empty_output(self):
        result = parse_linkchecker_output("")
        self.assertEqual(result, [])

    def test_parse_one_link(self):
        result = parse_linkchecker_output(raw_link_checker_output)
        self.assertEqual(result, [{"url":"https://link", "name":"name", "parent_url":"parent_url"}])

    def test_no_duplicates(self):
        result = parse_linkchecker_output(raw_link_checker_output + raw_link_checker_output2)
        self.assertEqual(result, [{"url":"https://link", "name":"name", "parent_url":"parent_url 2"}])



