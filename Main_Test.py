from collections import namedtuple
from programParser import evaluateLineByLine

print ("Hello World!")

Line = namedtuple('Line', 'line number')
#program = [Line("input x", number=1), Line(line="input z", number=2), Line(line="if (False) then", number=3), Line(line="[", number=4), Line(line="print \"yay\"", number=5), Line(line="]", number=6), Line(line="else", number=7),Line(line="[", number=8),Line(line="print \"no!\"", number=9),Line(line="]", number=10),Line(line="print \"Not messing up anything else\"", number=11), Line(line="end", number=12)]

program = [Line("input x", number=1), Line(line="z = 2", number=2), Line(line="while (z:le:10)", number=3), Line(line="[", number=4), Line(line="print \"yay while works too\"", number=5), Line(line="z = z + 1", number=6), Line(line="]", number=7), Line(line="print \"Not messing up anything else\"", number=8), Line(line="end", number=9)]

Variable = namedtuple('Variable', 'name value type')
variables = [Variable(name = 'X', value = '', type = "INTEGER"), Variable(name = 'Z', value = '', type = "INTEGER")]

evaluateLineByLine(program, variables)

