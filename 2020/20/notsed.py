#!/usr/bin/python3

import re
import sys

subst = "O\\2O\\3OO\\4OO\\5OOO\\6O\\7O\\8O\\9O\\10O\\11O"

for test_str in sys.stdin:
    result = re.sub(sys.argv[1], subst, test_str, 0, re.MULTILINE)

    if result:
        print (result)
