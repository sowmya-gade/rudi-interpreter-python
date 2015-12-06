from collections import namedtuple
from programParser import evaluateLineByLine


Line = namedtuple('Line', 'line number')
program = [Line("input x", number=1), Line(line="stop", number=2), Line(line="input z", number=3)]

Variable = namedtuple('Variable', 'name value type')
variables = [Variable(name = 'X', value = 0, type = "integer"), Variable(name = 'Y', value = 0.0, type = "float"), Variable(name = 'Z', value = "", type = "string")]

evaluateLineByLine(program, variables)

