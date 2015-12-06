from collections import namedtuple
from programParser import evaluateLineByLine

print "Hello World!"

Line = namedtuple('Line', 'line number')
program = [Line("input x", number=1), Line(line="input z", number=2), Line(line="if z:eq:2 then", number=3), Line(line="[", number=4), Line(line="print \"yay\"", number=5), Line(line="]", number=6)]

Variable = namedtuple('Variable', 'name value type')
variables = [Variable(name = 'X', value = 0, type = "integer"), Variable(name = 'Y', value = 0.0, type = "float"), Variable(name = 'Z', value = "", type = "string")]

evaluateLineByLine(program, variables)

