# coding=utf8
import re

def convert_camelcase_to_snakecase(name):
    return convert_camelcase_to_delimitcase(name)


def convert_camelcase_to_hyphen(name):
    return convert_camelcase_to_delimitcase(name, '-')

def convert_camelcase_to_delimitcase(name, delimiter = '_'):
    s1 = re.sub('(.)([A-Z][a-z]+)', r'\1' + delimiter + r'\2', name)
    return re.sub('([a-z0-9])([A-Z])', r'\1' + delimiter + r'\2', s1).lower()

if __name__ == '__main__':
    import sys
    rv = convert_camelcase_to_hyphen(sys.argv[1])
    print(rv)
