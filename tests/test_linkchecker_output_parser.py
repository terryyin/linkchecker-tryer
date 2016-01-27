import unittest
from linkchecker_tryer import parse_linkchecker_output, filter_out_good_links


raw_link_checker_output = '''
URL        `https://link'
Name       `name'
Parent URL parent_url
Check time 0.059 seconds
Result     Error: 404 Not Found
'''

raw_link_checker_output2 = '''
URL        `https://link'
Name       `name'
Parent URL parent_url 2
Check time 0.059 seconds
Result     Error: 404 Not Found
'''

raw_link_checker_output3 = '''
URL        `http://data-vocabulary.org/Event'
Parent URL parent_url
Real URL   http://data-vocabulary.org/Event
Check time 1.819 seconds
Size       49B
Result     Error: 404 Not Found
'''

expected_message = '''URL        http://data-vocabulary.org/Event
Parent URL parent_url
Real URL   http://data-vocabulary.org/Event
Check time 1.819 seconds
Size       49B
Result     Error: 404 Not Found'''





class Test_parse_raw_output(unittest.TestCase):

    def test_parse_empty_output(self):
        result = parse_linkchecker_output("")
        self.assertEqual(result, [])

    def test_parse_one_link(self):
        result = parse_linkchecker_output(raw_link_checker_output)
        del result[0]["message"]
        self.assertEqual(result, [{"url":"https://link", "name":"name", "parent_url":"parent_url"}])

    def test_no_duplicates(self):
        result = parse_linkchecker_output(raw_link_checker_output + "\n" +raw_link_checker_output2)
        del result[0]["message"]
        self.assertEqual(result, [{"url":"https://link", "name":"name", "parent_url":"parent_url 2"}])

    def test_when_no_name_given(self):
        result = parse_linkchecker_output(raw_link_checker_output3)
        del result[0]["message"]
        self.assertEqual(result, [{"url":"http://data-vocabulary.org/Event", "name":None, "parent_url":"parent_url"}])

    def test_when_no_name_given(self):
        result = parse_linkchecker_output(raw_link_checker_output3)
        self.assertEqual(result[0]["message"], expected_message)





