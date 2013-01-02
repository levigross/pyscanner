import ast
import _ast

test_file = open('main.py', 'r').read()

for n in ast.parse(test_file).body:
    if isinstance(n , _ast.Import):
        print u"Imported {0} Line {1}".format(n.names[0].name, n.lineno)
        continue
    if isinstance(n, _ast.ClassDef):
        print u"Class name: {0} Line {1}".format(n.name, n.lineno)
        continue
    if isinstance(n, _ast.FunctionDef):
        print u"Function name: {0} Line {1}".format(n.name, n.lineno)
        continue