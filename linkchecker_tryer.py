import re, sys, time
from pprint import pprint
import fileinput
from subprocess import call


def parse_linkchecker_output(linkchecker_output):
    pattern = re.compile(r"^URL\s+\`(.*?)\'$\n" +
                         r"^Name\s+\`(.*?)\'$\n" +
                         r"^Parent URL\s+(.*?)$", flags=re.M + re.S)

    def read_one(block):
        return {"url":block[0], "name":block[1], "parent_url":block[2]}

    return {x[0]:read_one(x) for x in pattern.findall(linkchecker_output)}.values()


def bad_link(link):
    return call(["linkchecker", "-r0", link["url"]]) != 0


def filter_out_good_links(links, filter_function):
    if links: time.sleep(10)
    return filter(filter_function, links)


def input_lines():
    for line in fileinput.input():
        print line,
        yield line
def main():
    result = reduce(
            filter_out_good_links,
            [bad_link] * 3,
            parse_linkchecker_output(
                ''.join(input_lines())))
    pprint(result)
    if result: sys.exit(1)
