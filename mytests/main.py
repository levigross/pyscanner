import urllib as something_else
from urlparse import urlsplit, urlparse, parse_qs as pq

class MySuperClass(object):
    def __init__(self):
        pass

    def _do_something(self):
        pass

    def add(self, a, b):
        return a + b

    def print_string(self, mystring='Hello World'):
        print mystring

    def compare_string(self, str1, str2):
        return str1 == str2


def func1():
    something_else.urlopen("{0}".format("www.google.com"))
    something_else.urlopen("%s" % "www.google.com")


def func2():
    pass


def func3():
    pass


def main():
    func1()
    func2()
    func3()
    MySuperClass().compare_string("Foo", "Bar")

if __name__ == '__main__':
    main()