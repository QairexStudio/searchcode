import os
import sys
class Parse:
    def __init__(self, com):
        self.command = com
    def parse(self):
        add, got = {}, []
        for m in self.command:
            for t in sys.argv:
                if m == t:
                    add[m] = sys.argv.index(m)
        mader = sys.argv
        mader.remove("sc.py")
        for kalk in add.values():
            got.append(mader[kalk])
        for k in self.command:
            if k in got:
                got.remove(k)
        return got
